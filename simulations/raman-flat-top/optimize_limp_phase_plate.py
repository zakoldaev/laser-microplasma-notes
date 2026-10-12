"""Optimize a simple LIMP-fabricable multilevel annular phase plate.

The model is scalar and axisymmetric. A Gaussian input beam illuminates a fused-
silica phase plate divided into concentric annular zones. Each zone can take one
of a finite number of phase/depth levels.

The default design is intended for a 785 nm Raman probe in microfluidic flow.
Instead of forcing a hard-edged top-hat, the optimizer targets a flat central
core followed by a smooth roll-off. The objective balances four quantities:

1. flatness inside the central core;
2. agreement with the soft edge;
3. optical energy retained inside the useful Raman probe;
4. light in the first sidelobe region.

The inputs are grouped below so the script can be reused for another wavelength,
beam diameter, target probe size, number of zones or number of relief levels.

Dependencies: numpy, scipy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j0

# -----------------------------------------------------------------------------
# USER INPUTS
# -----------------------------------------------------------------------------
WAVELENGTH_NM = 785.0
REFRACTIVE_INDEX = 1.453
NA = 0.40

# Expanded beam / illuminated phase-plate aperture.
# A 10 mm beam can also be tested simply by changing this value.
PUPIL_DIAMETER_MM = 12.0
INPUT_GAUSSIAN_RADIUS_MM = 4.8  # field-amplitude 1/e radius

# Soft-top-hat target in the sample plane.
# Default: about 4.2 µm flat core and about 6 µm useful probe diameter.
FLAT_CORE_DIAMETER_UM = 4.2
USEFUL_DIAMETER_UM = 6.0
SOFT_EDGE_CENTER_UM = 2.65
SOFT_EDGE_WIDTH_UM = 0.22

# Recommended first-build design.
N_ZONES = 64
N_PHASE_LEVELS = 12

# Fabrication-tolerance assumptions.
DEPTH_ERROR_NM = 50.0
SURFACE_RA_NM = 37.5

# Optimizer settings. Increase restarts/passes for a more thorough search.
N_RESTARTS = 6
MAX_GREEDY_PASSES = 5
RANDOM_SEED = 20261012

# Focal-plane range used to assess the design.
FOCAL_RADIUS_UM = 12.0

# Objective weights: flat core + smooth edge + enough energy.
W_CORE_FLATNESS = 1.25
W_EDGE_SHAPE = 0.85
W_USEFUL_ENERGY = 1.25
W_SIDELOBE = 0.65

# -----------------------------------------------------------------------------
# PREPARE RADIAL DIFFRACTION MODEL
# -----------------------------------------------------------------------------
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

rho = np.linspace(0.0, FOCAL_RADIUS_UM * 1e-6, 801)
area_weight = np.maximum(rho, rho[1] / 2.0)

r = np.linspace(0.0, rmax, 3000)
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

# Soft target: unit intensity in the core, then a logistic roll-off.
target = np.ones_like(rho)
edge_mask = rho > core_radius
target[edge_mask] = 1.0 / (
    1.0 + np.exp(np.clip((rho[edge_mask] - edge_center) / edge_width, -60, 60))
)


def field_from_codes(codes):
    """Focal-plane complex field for integer phase-level codes."""
    return np.sum(C * np.exp(1j * phase_values[codes])[:, None], axis=0)


def intensity_from_codes(codes):
    return np.abs(field_from_codes(codes)) ** 2


def metrics(I):
    """Return useful energy and shape metrics for one radial intensity profile."""
    total_energy = np.sum(I * area_weight)
    useful_energy = np.sum(I[useful] * area_weight[useful]) / total_energy

    core_mean = np.sum(I[core] * area_weight[core]) / np.sum(area_weight[core])
    In = I / core_mean

    core_cv = np.sqrt(
        np.sum((In[core] - 1.0) ** 2 * area_weight[core])
        / np.sum(area_weight[core])
    )

    if np.any(transition):
        edge_rmse = np.sqrt(
            np.sum((In[transition] - target[transition]) ** 2 * area_weight[transition])
            / np.sum(area_weight[transition])
        )
    else:
        edge_rmse = 0.0

    sidelobe_energy = (
        np.sum(I[sidelobe_region] * area_weight[sidelobe_region]) / total_energy
        if np.any(sidelobe_region)
        else 0.0
    )

    core_minmax = I[core].min() / I[core].max()
    return useful_energy, core_cv, edge_rmse, sidelobe_energy, core_minmax


def score(codes):
    """Balanced objective: flat core + smooth edge + enough energy."""
    useful_energy, core_cv, edge_rmse, sidelobe_energy, _ = metrics(
        intensity_from_codes(codes)
    )

    return (
        W_CORE_FLATNESS * core_cv
        + W_EDGE_SHAPE * edge_rmse
        + W_USEFUL_ENERGY * (1.0 - useful_energy)
        + W_SIDELOBE * sidelobe_energy
    )


# -----------------------------------------------------------------------------
# SIMPLE DISCRETE OPTIMIZER
# -----------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------
# CONVERT PHASE LEVELS TO FUSED-SILICA RELIEF DEPTHS
# -----------------------------------------------------------------------------
h_2pi = lam / (n - 1.0)
depth_step = h_2pi / N_PHASE_LEVELS
depths = best_codes * depth_step

I_ref = intensity_from_codes(np.zeros(N_ZONES, dtype=int))
I_opt = intensity_from_codes(best_codes)

# -----------------------------------------------------------------------------
# MONTE-CARLO DEPTH TOLERANCE
# -----------------------------------------------------------------------------
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

# Roughness is reported separately as an approximate coherent-efficiency factor.
Rq = SURFACE_RA_NM * 1e-9 * np.sqrt(np.pi / 2.0)
sigma_phi = 2.0 * np.pi * (n - 1.0) * Rq / lam
roughness_coherent_efficiency = np.exp(-sigma_phi**2)

# -----------------------------------------------------------------------------
# RESULTS
# -----------------------------------------------------------------------------
print("\nOptical assumptions")
print(f"  wavelength                  : {WAVELENGTH_NM:.1f} nm")
print(f"  NA                          : {NA:.3f}")
print(f"  effective focal length      : {f * 1e3:.3f} mm")
print(f"  illuminated pupil diameter  : {PUPIL_DIAMETER_MM:.3f} mm")
print(f"  flat-core diameter          : {FLAT_CORE_DIAMETER_UM:.3f} µm")
print(f"  useful-probe diameter       : {USEFUL_DIAMETER_UM:.3f} µm")

print("\nFabrication design")
print(f"  annular zones               : {N_ZONES}")
print(f"  zone width                  : {zone_width * 1e6:.1f} µm")
print(f"  phase/depth levels          : {N_PHASE_LEVELS}")
print(f"  full 2π relief depth        : {h_2pi * 1e6:.3f} µm")
print(f"  nominal depth increment     : {depth_step * 1e9:.1f} nm")
print(f"  optimizer score             : {best_score:.5f}")

for label, I in [("Gaussian / no plate", I_ref), ("Optimized phase plate", I_opt)]:
    useful_energy, core_cv, edge_rmse, sidelobe_energy, core_minmax = metrics(I)
    print(f"\n{label}")
    print(f"  energy in useful probe      : {useful_energy:.4f}")
    print(f"  CV in flat core             : {core_cv:.4f}")
    print(f"  soft-edge RMSE              : {edge_rmse:.4f}")
    print(f"  first-sidelobe energy       : {sidelobe_energy:.4f}")
    print(f"  min/max in flat core        : {core_minmax:.4f}")

print("\nDepth-error Monte Carlo")
print(f"  assumed zone error          : ±{DEPTH_ERROR_NM:.1f} nm")
print(f"  median core CV              : {np.median(mc_metrics[:,1]):.4f}")
print(
    f"  5th-95th percentile core CV: {np.percentile(mc_metrics[:,1],5):.4f} - "
    f"{np.percentile(mc_metrics[:,1],95):.4f}"
)
print(f"  roughness coherent factor   : {roughness_coherent_efficiency:.4f}")

print("\nZone design")
print("zone, inner_mm, outer_mm, phase_code, depth_um")
for z in range(N_ZONES):
    print(
        f"{z+1:02d}, {zone_edges[z]*1e3:.4f}, {zone_edges[z+1]*1e3:.4f}, "
        f"{best_codes[z]}, {depths[z]*1e6:.4f}"
    )

# -----------------------------------------------------------------------------
# PLOTS
# -----------------------------------------------------------------------------
# Normalize both profiles by the mean intensity in the requested flat core.
def core_normalized(I):
    mean_core = np.sum(I[core] * area_weight[core]) / np.sum(area_weight[core])
    return I / mean_core

plt.figure(figsize=(7.4, 4.8))
plt.plot(rho * 1e6, core_normalized(I_ref), label="Gaussian / no plate")
plt.plot(rho * 1e6, core_normalized(I_opt), label="Optimized multilevel plate")
plt.plot(rho * 1e6, target, "--", label="soft top-hat target")
plt.axvline(core_radius * 1e6, linestyle=":", linewidth=1, label="flat-core radius")
plt.axvline(useful_radius * 1e6, linestyle="--", linewidth=1, label="useful radius")
plt.xlabel("Radius in sample plane (µm)")
plt.ylabel("Intensity normalized to flat-core mean")
plt.title("Gaussian vs LIMP-shaped Raman probe")
plt.xlim(0, min(8.0, FOCAL_RADIUS_UM))
plt.ylim(0, 1.8)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("gaussian_vs_soft_tophat_raman.png", dpi=180)

zone_centers = 0.5 * (zone_edges[:-1] + zone_edges[1:])
plt.figure(figsize=(7.4, 4.8))
plt.step(zone_centers * 1e3, depths * 1e6, where="mid")
plt.xlabel("Radial position on plate (mm)")
plt.ylabel("Relief depth (µm)")
plt.title("64-zone / 12-level LIMP phase plate")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("optimized_limp_phaseplate_depths.png", dpi=180)
plt.show()

print("\nSaved: gaussian_vs_soft_tophat_raman.png")
print("Saved: optimized_limp_phaseplate_depths.png")
