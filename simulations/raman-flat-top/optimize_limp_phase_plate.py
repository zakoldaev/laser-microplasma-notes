"""Optimize a simple LIMP-fabricable multilevel annular phase plate.

The model is scalar and axisymmetric. A Gaussian input beam illuminates a fused-
silica phase plate divided into concentric annular zones. Each zone can take one
of a finite number of phase/depth levels. A small discrete optimizer searches
for a profile that is approximately flat inside the requested Raman probe and
penalizes light immediately outside it.

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
PUPIL_DIAMETER_MM = 5.0
INPUT_GAUSSIAN_RADIUS_MM = 2.0  # field-amplitude 1/e radius
TARGET_DIAMETER_UM = 5.0

N_ZONES = 20
N_PHASE_LEVELS = 8
DEPTH_ERROR_NM = 50.0
SURFACE_RA_NM = 37.5

# Optimizer settings. Increase restarts for a more thorough search.
N_RESTARTS = 8
MAX_GREEDY_PASSES = 6
RANDOM_SEED = 20261012

# Focal-plane range used to assess the design.
FOCAL_RADIUS_UM = 12.0

# -----------------------------------------------------------------------------
# PREPARE RADIAL DIFFRACTION MODEL
# -----------------------------------------------------------------------------
lam = WAVELENGTH_NM * 1e-9
n = REFRACTIVE_INDEX
D = PUPIL_DIAMETER_MM * 1e-3
rmax = D / 2.0
f = D / (2.0 * NA)  # paraxial relation D ≈ 2 f NA
beam_radius = INPUT_GAUSSIAN_RADIUS_MM * 1e-3

target_radius = TARGET_DIAMETER_UM * 1e-6 / 2.0
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
inside = rho <= target_radius
guard = (rho > target_radius) & (rho <= 2.4 * target_radius)


def field_from_codes(codes):
    """Focal-plane complex field for integer phase-level codes."""
    return np.sum(C * np.exp(1j * phase_values[codes])[:, None], axis=0)


def intensity_from_codes(codes):
    return np.abs(field_from_codes(codes)) ** 2


def score(codes):
    """Flatness inside target + penalty for nearby sidelobes."""
    I = intensity_from_codes(codes)
    mean_inside = np.sum(I[inside] * area_weight[inside]) / np.sum(area_weight[inside])
    if mean_inside <= 0:
        return 1e12
    In = I / mean_inside

    flat_rmse = np.sqrt(
        np.sum((In[inside] - 1.0) ** 2 * area_weight[inside])
        / np.sum(area_weight[inside])
    )
    nearby_light = (
        np.sum(In[guard] * area_weight[guard]) / np.sum(area_weight[guard])
    )
    return flat_rmse + 0.55 * nearby_light


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


def metrics(I):
    total = np.sum(I * area_weight)
    in_energy = np.sum(I[inside] * area_weight[inside]) / total

    vals = I[inside]
    w = area_weight[inside]
    mean = np.sum(vals * w) / np.sum(w)
    cv = np.sqrt(np.sum((vals - mean) ** 2 * w) / np.sum(w)) / mean

    normalized = vals / vals.max()
    uniformity = normalized.min() / normalized.max()
    return in_energy, cv, uniformity


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
print(f"  wavelength                 : {WAVELENGTH_NM:.1f} nm")
print(f"  NA                         : {NA:.3f}")
print(f"  effective focal length     : {f * 1e3:.3f} mm")
print(f"  illuminated pupil diameter : {PUPIL_DIAMETER_MM:.3f} mm")
print(f"  desired probe diameter     : {TARGET_DIAMETER_UM:.3f} µm")

print("\nFabrication design")
print(f"  annular zones              : {N_ZONES}")
print(f"  zone width                 : {zone_width * 1e6:.1f} µm")
print(f"  phase/depth levels         : {N_PHASE_LEVELS}")
print(f"  full 2π relief depth       : {h_2pi * 1e6:.3f} µm")
print(f"  nominal depth increment    : {depth_step * 1e9:.1f} nm")
print(f"  optimizer score            : {best_score:.5f}")

for label, I in [("Gaussian / no plate", I_ref), ("Optimized phase plate", I_opt)]:
    energy, cv, uniformity = metrics(I)
    print(f"\n{label}")
    print(f"  energy in target disk      : {energy:.4f}")
    print(f"  CV inside target disk      : {cv:.4f}")
    print(f"  min/max radial uniformity  : {uniformity:.4f}")

print("\nDepth-error Monte Carlo")
print(f"  assumed zone error         : ±{DEPTH_ERROR_NM:.1f} nm")
print(f"  median CV                  : {np.median(mc_metrics[:,1]):.4f}")
print(f"  5th-95th percentile CV     : {np.percentile(mc_metrics[:,1],5):.4f} - "
      f"{np.percentile(mc_metrics[:,1],95):.4f}")
print(f"  roughness coherent factor  : {roughness_coherent_efficiency:.4f}")

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
plt.figure(figsize=(7.4, 4.8))
plt.plot(rho * 1e6, I_ref / I_ref.max(), label="Gaussian / no plate")
plt.plot(rho * 1e6, I_opt / I_opt.max(), label="Optimized multilevel plate")
plt.axvline(target_radius * 1e6, linestyle="--", linewidth=1, label="target radius")
plt.xlabel("Radius in sample plane (µm)")
plt.ylabel("Normalized intensity")
plt.title("LIMP-fabricable Raman beam shaping")
plt.xlim(0, min(10.0, FOCAL_RADIUS_UM))
plt.ylim(0, 1.05)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("optimized_limp_raman_profile.png", dpi=180)

zone_centers = 0.5 * (zone_edges[:-1] + zone_edges[1:])
plt.figure(figsize=(7.4, 4.8))
plt.step(zone_centers * 1e3, depths * 1e6, where="mid")
plt.xlabel("Radial position on plate (mm)")
plt.ylabel("Relief depth (µm)")
plt.title("Optimized annular multilevel phase plate")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("optimized_limp_phaseplate_depths.png", dpi=180)
plt.show()

print("\nSaved: optimized_limp_raman_profile.png")
print("Saved: optimized_limp_phaseplate_depths.png")
