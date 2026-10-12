"""Optimize a LIMP-fabricable multilevel annular phase plate for a Raman probe.

The model is scalar and axisymmetric. A Gaussian beam illuminates a fused-silica
phase plate divided into concentric annular zones. Each zone is assigned one of
a finite number of phase/depth levels.

The default case is the current proposed first-build design:

- wavelength: 785 nm
- illuminated aperture: 12 mm
- 64 annular zones
- 12 phase/depth levels
- ~4.2 µm flat core
- ~6 µm useful probe diameter

The optimizer does NOT force a mathematically sharp top hat. Instead it searches
for an ACTUAL phase-shaped output with a flat central region, smooth roll-off,
useful optical energy and limited first sidelobes.

The script saves:

1. figure_a_phaseplate_and_focal_field.png
   2-D phase-plate relief map + resulting focal field.
2. figure_b_gaussian_vs_optimized_output.png
   Only two profiles: Gaussian focus and the actual optimized output.
3. optimized_phaseplate_design.csv
   Zone radii, phase codes and relief depths.
4. optimized_phaseplate_metrics.csv
   Main output metrics for the Gaussian and optimized cases.

Dependencies: numpy, scipy, matplotlib
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j0

# =============================================================================
# USER INPUTS: OPTICAL SYSTEM
# =============================================================================
WAVELENGTH_NM = 785.0
REFRACTIVE_INDEX = 1.453  # fused silica, illustrative value at 785 nm
NA = 0.40

# Expanded beam / illuminated phase-plate aperture.
PUPIL_DIAMETER_MM = 12.0
INPUT_GAUSSIAN_RADIUS_MM = 4.8  # field-amplitude 1/e radius

# =============================================================================
# USER INPUTS: DESIRED OUTPUT
# =============================================================================
# We ask for a flat central Raman probe followed by a soft edge.
FLAT_CORE_DIAMETER_UM = 4.2
USEFUL_DIAMETER_UM = 6.0
SOFT_EDGE_CENTER_UM = 2.65
SOFT_EDGE_WIDTH_UM = 0.22

# =============================================================================
# USER INPUTS: FABRICATION DESIGN
# =============================================================================
N_ZONES = 64
N_PHASE_LEVELS = 12

# Fabrication-tolerance assumptions.
DEPTH_ERROR_NM = 50.0
SURFACE_RA_NM = 37.5

# =============================================================================
# USER INPUTS: OPTIMIZER
# =============================================================================
# These defaults reproduce the example used in the repository discussion.
N_RESTARTS = 4
MAX_GREEDY_PASSES = 4
RANDOM_SEED = 20261012

# Focal-plane range used to assess the design.
FOCAL_RADIUS_UM = 12.0

# Objective weights: flat core + smooth edge + enough energy + low sidelobes.
W_CORE_FLATNESS = 1.25
W_EDGE_SHAPE = 0.85
W_USEFUL_ENERGY = 1.25
W_SIDELOBE = 0.65

# Numerical grids. Increase these for a slower convergence check.
N_FOCAL_POINTS = 601
N_PUPIL_POINTS = 2200

# =============================================================================
# PREPARE RADIAL DIFFRACTION MODEL
# =============================================================================
lam = WAVELENGTH_NM * 1e-9
n = REFRACTIVE_INDEX
D = PUPIL_DIAMETER_MM * 1e-3
rmax = D / 2.0
f = D / (2.0 * NA)  # paraxial relation D ≈ 2 f NA
beam_radius = INPUT_GAUSSIAN_RADIUS_MM * 1e-3

core_radius = FLAT_CORE_DIAMETER_UM * 1e-6 / 2.0
useful_radius = USEFUL_DIAMETER_UM * 1e-6 / 2.0
edge_center = SOFT_EDGE_CENTER_UM * 1e-6
edge_width = SOFT_EDGE_WIDTH_UM * 1e-6

zone_edges = np.linspace(0.0, rmax, N_ZONES + 1)
zone_width = zone_edges[1] - zone_edges[0]

rho = np.linspace(0.0, FOCAL_RADIUS_UM * 1e-6, N_FOCAL_POINTS)
area_weight = np.maximum(rho, rho[1] / 2.0)

r = np.linspace(0.0, rmax, N_PUPIL_POINTS)
input_amplitude = np.exp(-(r / beam_radius) ** 2)

k = 2.0 * np.pi / lam
J = j0((k / f) * np.outer(rho, r))

# Complex focal-field contribution from every annular zone.
C = np.zeros((N_ZONES, len(rho)), dtype=complex)
for z in range(N_ZONES):
    if z < N_ZONES - 1:
        mask = (r >= zone_edges[z]) & (r < zone_edges[z + 1])
    else:
        mask = (r >= zone_edges[z]) & (r <= zone_edges[z + 1])

    C[z] = np.trapezoid(
        J[:, mask] * (input_amplitude[mask] * r[mask])[None, :],
        r[mask],
        axis=1,
    )

phase_values = 2.0 * np.pi * np.arange(N_PHASE_LEVELS) / N_PHASE_LEVELS

core = rho <= core_radius
transition = (rho > core_radius) & (rho <= useful_radius)
sidelobe_region = (rho > useful_radius) & (rho <= 2.0 * useful_radius)
useful = rho <= useful_radius

# The TARGET is used only by the optimizer. Figure B below shows the ACTUAL
# optimized output, not this ideal target curve.
target = np.ones_like(rho)
edge_mask = rho > core_radius
target[edge_mask] = 1.0 / (
    1.0
    + np.exp(
        np.clip((rho[edge_mask] - edge_center) / edge_width, -60.0, 60.0)
    )
)


def field_from_codes(codes):
    """Return the focal-plane complex field for integer phase-level codes."""
    return np.sum(C * np.exp(1j * phase_values[codes])[:, None], axis=0)


def intensity_from_codes(codes):
    """Return radial focal-plane intensity."""
    return np.abs(field_from_codes(codes)) ** 2


def metrics(I):
    """Return useful-energy and shape metrics for one radial intensity profile."""
    total_energy = np.sum(I * area_weight)
    useful_energy = np.sum(I[useful] * area_weight[useful]) / total_energy

    core_mean = np.sum(I[core] * area_weight[core]) / np.sum(area_weight[core])
    In = I / core_mean

    core_cv = np.sqrt(
        np.sum((In[core] - 1.0) ** 2 * area_weight[core])
        / np.sum(area_weight[core])
    )

    edge_rmse = np.sqrt(
        np.sum((In[transition] - target[transition]) ** 2 * area_weight[transition])
        / np.sum(area_weight[transition])
    )

    sidelobe_energy = (
        np.sum(I[sidelobe_region] * area_weight[sidelobe_region]) / total_energy
    )

    core_minmax = I[core].min() / I[core].max()
    return useful_energy, core_cv, edge_rmse, sidelobe_energy, core_minmax


def score(codes):
    """Balanced objective: flat core + smooth edge + useful energy + low sidelobes."""
    useful_energy, core_cv, edge_rmse, sidelobe_energy, _ = metrics(
        intensity_from_codes(codes)
    )

    return (
        W_CORE_FLATNESS * core_cv
        + W_EDGE_SHAPE * edge_rmse
        + W_USEFUL_ENERGY * (1.0 - useful_energy)
        + W_SIDELOBE * sidelobe_energy
    )


# =============================================================================
# DISCRETE OPTIMIZER
# =============================================================================
rng = np.random.default_rng(RANDOM_SEED)
best_codes = None
best_score = np.inf

for restart in range(N_RESTARTS):
    codes = rng.integers(0, N_PHASE_LEVELS, size=N_ZONES)
    current_score = score(codes)

    for _ in range(MAX_GREEDY_PASSES):
        improved = False

        for zone in range(N_ZONES):
            old_code = codes[zone]
            local_code = old_code
            local_score = current_score

            for candidate in range(N_PHASE_LEVELS):
                if candidate == old_code:
                    continue

                codes[zone] = candidate
                candidate_score = score(codes)

                if candidate_score < local_score:
                    local_score = candidate_score
                    local_code = candidate

            codes[zone] = local_code

            if local_score < current_score - 1e-12:
                current_score = local_score
                improved = True

        if not improved:
            break

    if current_score < best_score:
        best_score = current_score
        best_codes = codes.copy()

# =============================================================================
# CONVERT PHASE CODES TO FUSED-SILICA RELIEF DEPTHS
# =============================================================================
h_2pi = lam / (n - 1.0)
depth_step = h_2pi / N_PHASE_LEVELS
depths = best_codes * depth_step

I_gaussian = intensity_from_codes(np.zeros(N_ZONES, dtype=int))
I_optimized = intensity_from_codes(best_codes)

metrics_gaussian = metrics(I_gaussian)
metrics_optimized = metrics(I_optimized)

# =============================================================================
# MONTE-CARLO DEPTH TOLERANCE
# =============================================================================
n_mc = 300
mc_metrics = []

for _ in range(n_mc):
    jitter = rng.uniform(
        -DEPTH_ERROR_NM * 1e-9,
        DEPTH_ERROR_NM * 1e-9,
        size=N_ZONES,
    )
    phase = 2.0 * np.pi * (n - 1.0) * (depths + jitter) / lam
    E = np.sum(C * np.exp(1j * phase)[:, None], axis=0)
    mc_metrics.append(metrics(np.abs(E) ** 2))

mc_metrics = np.asarray(mc_metrics)

# Approximate coherent-efficiency factor associated with roughness.
Rq = SURFACE_RA_NM * 1e-9 * np.sqrt(np.pi / 2.0)
sigma_phi = 2.0 * np.pi * (n - 1.0) * Rq / lam
roughness_coherent_efficiency = np.exp(-sigma_phi**2)

# =============================================================================
# TEXT RESULTS
# =============================================================================
print("\nPROPOSED INPUT PARAMETERS")
print(f"  wavelength                  : {WAVELENGTH_NM:.1f} nm")
print(f"  NA                          : {NA:.3f}")
print(f"  illuminated pupil diameter  : {PUPIL_DIAMETER_MM:.1f} mm")
print(f"  Gaussian amplitude radius   : {INPUT_GAUSSIAN_RADIUS_MM:.1f} mm")

print("\nDESIRED OUTPUT")
print(f"  flat-core diameter          : {FLAT_CORE_DIAMETER_UM:.1f} µm")
print(f"  useful-probe diameter       : {USEFUL_DIAMETER_UM:.1f} µm")
print("  edge                        : smooth roll-off, not a hard top-hat")

print("\nFABRICATION DESIGN")
print(f"  annular zones               : {N_ZONES}")
print(f"  exact radial zone width     : {zone_width * 1e6:.1f} µm")
print(f"  rounded zone width          : ~{round(zone_width * 1e6 / 10) * 10:.0f} µm")
print(f"  phase/depth levels          : {N_PHASE_LEVELS}")
print(f"  full 2π relief depth        : {h_2pi * 1e6:.3f} µm")
print(f"  exact depth increment       : {depth_step * 1e9:.1f} nm")
print(f"  rounded depth increment     : ~{round(depth_step * 1e9 / 10) * 10:.0f} nm")
print(f"  optimizer score             : {best_score:.5f}")

for label, values in [
    ("Gaussian / no plate", metrics_gaussian),
    ("Optimized phase-shaped output", metrics_optimized),
]:
    useful_energy, core_cv, edge_rmse, sidelobe_energy, core_minmax = values
    print(f"\n{label}")
    print(f"  energy in useful probe      : {useful_energy:.4f}")
    print(f"  CV in flat core             : {core_cv:.4f}")
    print(f"  soft-edge RMSE              : {edge_rmse:.4f}")
    print(f"  first-sidelobe energy       : {sidelobe_energy:.4f}")
    print(f"  min/max in flat core        : {core_minmax:.4f}")

print("\nDEPTH-ERROR MONTE CARLO")
print(f"  assumed independent error   : ±{DEPTH_ERROR_NM:.1f} nm per zone")
print(f"  median core CV              : {np.median(mc_metrics[:, 1]):.4f}")
print(
    f"  5th-95th percentile core CV: {np.percentile(mc_metrics[:, 1], 5):.4f} - "
    f"{np.percentile(mc_metrics[:, 1], 95):.4f}"
)
print(f"  roughness coherent factor   : {roughness_coherent_efficiency:.4f}")

# =============================================================================
# SAVE NUMERICAL OUTPUTS
# =============================================================================
with open("optimized_phaseplate_design.csv", "w", newline="", encoding="utf-8") as fcsv:
    writer = csv.writer(fcsv)
    writer.writerow(
        ["zone", "inner_radius_mm", "outer_radius_mm", "phase_code", "depth_um"]
    )
    for z in range(N_ZONES):
        writer.writerow(
            [
                z + 1,
                zone_edges[z] * 1e3,
                zone_edges[z + 1] * 1e3,
                int(best_codes[z]),
                depths[z] * 1e6,
            ]
        )

with open("optimized_phaseplate_metrics.csv", "w", newline="", encoding="utf-8") as fcsv:
    writer = csv.writer(fcsv)
    writer.writerow(
        [
            "case",
            "useful_energy_fraction",
            "core_cv",
            "soft_edge_rmse",
            "first_sidelobe_energy_fraction",
            "core_minmax",
        ]
    )
    writer.writerow(["Gaussian / no plate", *metrics_gaussian])
    writer.writerow(["Optimized phase-shaped output", *metrics_optimized])

# =============================================================================
# FIGURE A: RELIEF MAP + ACTUAL RESULTING FOCAL FIELD
# =============================================================================
NN = 700
x = np.linspace(-rmax, rmax, NN)
X, Y = np.meshgrid(x, x)
R = np.sqrt(X**2 + Y**2)
H = np.full_like(R, np.nan)

for z in range(N_ZONES):
    if z < N_ZONES - 1:
        mask = (R >= zone_edges[z]) & (R < zone_edges[z + 1])
    else:
        mask = (R >= zone_edges[z]) & (R <= zone_edges[z + 1])
    H[mask] = depths[z] * 1e6

x2 = np.linspace(-6e-6, 6e-6, 401)
X2, Y2 = np.meshgrid(x2, x2)
R2 = np.sqrt(X2**2 + Y2**2)
I2 = np.interp(
    R2,
    rho,
    I_optimized / I_optimized.max(),
    left=I_optimized[0] / I_optimized.max(),
    right=0.0,
)

fig = plt.figure(figsize=(10.2, 4.9))

ax1 = fig.add_axes([0.06, 0.14, 0.42, 0.76])
im1 = ax1.imshow(
    H,
    origin="lower",
    extent=[-rmax * 1e3, rmax * 1e3, -rmax * 1e3, rmax * 1e3],
)
ax1.set_xlabel("x on plate (mm)")
ax1.set_ylabel("y on plate (mm)")
ax1.set_title("64-zone / 12-level phase-plate relief map")

cax1 = fig.add_axes([0.49, 0.14, 0.018, 0.76])
cb1 = fig.colorbar(im1, cax=cax1)
cb1.set_label("Relief depth (µm)")

ax2 = fig.add_axes([0.60, 0.24, 0.28, 0.56])
im2 = ax2.imshow(
    I2,
    origin="lower",
    extent=[x2[0] * 1e6, x2[-1] * 1e6, x2[0] * 1e6, x2[-1] * 1e6],
)
ax2.set_xlabel("x in sample plane (µm)")
ax2.set_ylabel("y in sample plane (µm)")
ax2.set_title("Actual optimized focal field")

cax2 = fig.add_axes([0.90, 0.24, 0.018, 0.56])
cb2 = fig.colorbar(im2, cax=cax2)
cb2.set_label("Normalized intensity")

plt.savefig("figure_a_phaseplate_and_focal_field.png", dpi=200)
plt.close(fig)

# =============================================================================
# FIGURE B: ONLY GAUSSIAN VS ACTUAL OPTIMIZED OUTPUT
# =============================================================================
x_um = np.linspace(-6.0, 6.0, 1201)
abs_r_m = np.abs(x_um) * 1e-6

gaussian_line = np.interp(abs_r_m, rho, I_gaussian)
optimized_line = np.interp(abs_r_m, rho, I_optimized)

# Normalize each profile to its own maximum so the shapes are directly visible.
gaussian_line /= gaussian_line.max()
optimized_line /= optimized_line.max()

fig, ax = plt.subplots(figsize=(7.4, 4.8))
ax.plot(x_um, gaussian_line, linewidth=2.2, label="Gaussian focus")
ax.plot(
    x_um,
    optimized_line,
    linewidth=2.2,
    label="Optimized phase-shaped output",
)
ax.set_xlabel("Lateral position in sample plane (µm)")
ax.set_ylabel("Normalized intensity")
ax.set_title("Gaussian focus vs optimized phase-shaped output")
ax.set_xlim(-6.0, 6.0)
ax.set_ylim(0.0, 1.08)
ax.grid(alpha=0.25)
ax.legend()
fig.tight_layout()
fig.savefig("figure_b_gaussian_vs_optimized_output.png", dpi=200)
plt.close(fig)

print("\nSaved:")
print("  figure_a_phaseplate_and_focal_field.png")
print("  figure_b_gaussian_vs_optimized_output.png")
print("  optimized_phaseplate_design.csv")
print("  optimized_phaseplate_metrics.csv")
