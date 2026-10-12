"""Compare Gaussian and soft-top-hat Raman probes for particles in flow.

This is an intentionally simple application-level model. It asks one question:
how much does the integrated Raman-event amplitude change when nominally
identical particles cross the probe at different lateral positions?

The shaped-beam model now uses a flat central core followed by a smooth cosine
roll-off. This better represents the design target used by the accompanying
LIMP phase-plate optimizer than an ideal hard-edged top-hat.

Only NumPy and Matplotlib are required.
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# USER INPUTS
# -----------------------------------------------------------------------------
CHANNEL_WIDTH_UM = 10.0
PARTICLE_STREAM_SIGMA_UM = 1.0   # hydrodynamic focusing; set larger for broad flow
GAUSSIAN_RADIUS_UM = 2.5         # excitation 1/e^2 intensity radius

# Current shaped-probe target used in the phase-plate design.
SOFT_TOP_CORE_DIAMETER_UM = 4.2
SOFT_TOP_USEFUL_DIAMETER_UM = 6.0

DETECTION_RADIUS_UM = 2.5        # Gaussian confocal collection 1/e^2 radius
N_PARTICLES = 100_000
RANDOM_SEED = 7

# Numerical integration range along the flow direction
FLOW_SPAN_UM = 12.0
N_X = 2401

# -----------------------------------------------------------------------------
# BEAM AND COLLECTION MODELS
# -----------------------------------------------------------------------------
def gaussian_intensity(x, y, radius_um):
    """Gaussian intensity with 1/e^2 radius = radius_um."""
    return np.exp(-2.0 * (x * x + y * y) / radius_um**2)


def soft_top_intensity(x, y, core_diameter_um, useful_diameter_um):
    """Flat core with a smooth cosine-squared radial roll-off.

    Intensity is 1 inside the core, falls smoothly between the core and useful
    radii, and is 0 outside the useful radius.
    """
    core_radius = core_diameter_um / 2.0
    useful_radius = useful_diameter_um / 2.0
    if useful_radius <= core_radius:
        raise ValueError("Useful diameter must be larger than core diameter.")

    r = np.sqrt(x * x + y * y)
    I = np.zeros_like(r, dtype=float)

    I[r <= core_radius] = 1.0
    transition = (r > core_radius) & (r < useful_radius)
    u = (r[transition] - core_radius) / (useful_radius - core_radius)
    I[transition] = np.cos(0.5 * np.pi * u) ** 2
    return I


def collection_weight(x, y, radius_um):
    """Simple Gaussian lateral confocal collection weighting."""
    return np.exp(-2.0 * (x * x + y * y) / radius_um**2)


def equal_power_normalization(profile, half_width_um=10.0, n=1001):
    """Numerically integrate a 2-D profile so beam cases use equal optical power."""
    g = np.linspace(-half_width_um, half_width_um, n)
    X, Y = np.meshgrid(g, g)
    dA = (g[1] - g[0]) ** 2
    return np.sum(profile(X, Y)) * dA


x = np.linspace(-FLOW_SPAN_UM / 2, FLOW_SPAN_UM / 2, N_X)
dx = x[1] - x[0]

profiles = {
    "Gaussian": lambda X, Y: gaussian_intensity(X, Y, GAUSSIAN_RADIUS_UM),
    "Soft top-hat": lambda X, Y: soft_top_intensity(
        X,
        Y,
        SOFT_TOP_CORE_DIAMETER_UM,
        SOFT_TOP_USEFUL_DIAMETER_UM,
    ),
}

normalization = {
    name: equal_power_normalization(fn) for name, fn in profiles.items()
}


def transit_signal(y0_um, name):
    """Integrated Raman-event signal for one straight particle trajectory."""
    y = np.full_like(x, y0_um)
    excitation = profiles[name](x, y) / normalization[name]
    detection = collection_weight(x, y, DETECTION_RADIUS_UM)
    return np.sum(excitation * detection) * dx


# -----------------------------------------------------------------------------
# PARTICLE TRAJECTORIES
# -----------------------------------------------------------------------------
rng = np.random.default_rng(RANDOM_SEED)

# Gaussian transverse stream, truncated at channel walls.
particles = []
while len(particles) < N_PARTICLES:
    draw = rng.normal(0.0, PARTICLE_STREAM_SIGMA_UM, N_PARTICLES)
    draw = draw[np.abs(draw) <= CHANNEL_WIDTH_UM / 2]
    particles.extend(draw.tolist())
particle_y = np.asarray(particles[:N_PARTICLES])

# Reference all amplitudes to the Gaussian center-line trajectory.
reference = transit_signal(0.0, "Gaussian")

results = {}
for name in profiles:
    signals = np.array([transit_signal(y0, name) for y0 in particle_y]) / reference
    results[name] = signals

    print(f"\n{name}")
    print(f"  mean relative event signal : {signals.mean():.4f}")
    print(f"  coefficient of variation   : {signals.std() / signals.mean():.4f}")
    print(f"  median                      : {np.median(signals):.4f}")
    print(
        f"  10th-90th percentile        : "
        f"{np.percentile(signals, 10):.4f} - {np.percentile(signals, 90):.4f}"
    )

# -----------------------------------------------------------------------------
# PLOTS
# -----------------------------------------------------------------------------
y_plot = np.linspace(-CHANNEL_WIDTH_UM / 2, CHANNEL_WIDTH_UM / 2, 801)

plt.figure(figsize=(7.2, 4.8))
for name in profiles:
    curve = np.array([transit_signal(y0, name) for y0 in y_plot]) / reference
    plt.plot(y_plot, curve, label=name)
plt.xlabel("Particle lateral position in channel (µm)")
plt.ylabel("Integrated Raman-event signal (relative)")
plt.title("Trajectory dependence of a confocal Raman flow measurement")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("raman_flow_position_dependence.png", dpi=180)

plt.figure(figsize=(7.2, 4.8))
bins = np.linspace(0, max(v.max() for v in results.values()) * 1.03, 100)
for name, signals in results.items():
    plt.hist(signals, bins=bins, density=True, histtype="step", linewidth=1.5, label=name)
plt.xlabel("Integrated Raman-event signal (relative)")
plt.ylabel("Probability density")
plt.title("Event-amplitude distribution for the same particle population")
plt.legend()
plt.tight_layout()
plt.savefig("raman_flow_event_distribution.png", dpi=180)
plt.show()

print("\nShaped-probe target")
print(f"  flat-core diameter  : {SOFT_TOP_CORE_DIAMETER_UM:.2f} µm")
print(f"  useful diameter     : {SOFT_TOP_USEFUL_DIAMETER_UM:.2f} µm")
print("\nSaved: raman_flow_position_dependence.png")
print("Saved: raman_flow_event_distribution.png")
