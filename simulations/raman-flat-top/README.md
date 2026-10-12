# Raman flat-top simulations

These scripts support the exploratory note [From random phase plates to a microfluidic Raman probe](../../rethinking/01-raman-microfluidic-flat-top.md).

They are intentionally compact. The goal is not to reproduce a commercial Raman microscope in full detail, but to make the central design questions easy to inspect and modify.

## Requirements

Python 3 with:

```bash
pip install numpy scipy matplotlib
```

## Current recommended first-build design

For the present 785 nm microfluidic-Raman concept, the default design has been updated to:

```text
input beam diameter:   12 mm
annular zones:         64
phase/depth levels:    12
flat core:             ~4.2 µm diameter
useful probe:          ~6 µm diameter
zone width:            ~100 µm
nominal depth step:    ~140 nm
full 2π relief:        ~1.73 µm
```

The same script can be rerun with a 10 mm input beam simply by changing `PUPIL_DIAMETER_MM`.

### Why 64 zones?

With a 12 mm illuminated diameter, 64 equal radial zones correspond to about **94 µm per annulus**, rounded to **~100 µm** in the discussion. With a 10 mm beam, the same design gives about 78 µm per annulus. Both values remain far larger than a few-micrometre LIMP writing capability, so the geometry gives the optimizer substantially more phase freedom without approaching the minimum lateral fabrication scale.

### Why 12 depth levels?

At 785 nm the fused-silica full-2π relief in the model is about **1.73 µm**. Twelve phase states therefore give a nominal depth increment of about **0.14 µm (~140 nm)**. This remains comfortably larger than the ~50 nm depth-control scale demonstrated in the earlier LIMP work, while giving a finer phase approximation than the previous eight-level design.

A 16-level design would reduce the depth spacing to roughly 0.11 µm. That may still be practical, but it leaves less margin for local depth error, calibration drift and roughness. For a first fabrication, **64 zones / 12 levels** is therefore the present compromise between optical freedom and fabrication margin.

## Why the target is now a soft top-hat

The earlier hard-edged top-hat optimization produced visible radial ringing. This is expected when a finite circular pupil is forced to create an abrupt intensity edge.

The updated model instead targets:

```text
flat central core
→ smooth radial roll-off
→ low first sidelobe
```

The default target is approximately **4.2 µm flat-core diameter** followed by a smooth transition so that the useful probe is about **6 µm diameter**.

The optimizer now balances four quantities:

```text
core flatness
+ soft-edge agreement
+ useful energy inside the probe
+ first-sidelobe suppression
```

The intention is not to generate a mathematically perfect top-hat at any cost. The useful Raman design is the one that is flat enough to reduce trajectory sensitivity while still retaining enough excitation power inside the microfluidic detection region.

## 1. Compare Gaussian and shaped probes in flow

Run:

```bash
python compare_raman_flow.py
```

The script models a particle crossing a confocal Raman probe in a microfluidic channel. Raman event amplitude is approximated by the line integral of the excitation intensity multiplied by a Gaussian confocal collection weighting.

At the top of the file you can change:

- channel width;
- particle-stream width;
- Gaussian beam radius;
- desired flat-top diameter;
- confocal detection radius;
- number of simulated particles.

The useful comparison is not only peak signal. The script reports the mean Raman-event signal and the coefficient of variation across particle trajectories.

## 2. Optimize an annular LIMP phase plate

Run:

```bash
python optimize_limp_phase_plate.py
```

The script uses a scalar radial diffraction model and searches over discrete annular phase levels. The phase plate consists of concentric annular zones, each assigned one of a finite number of relief depths.

The default inputs are now:

```python
PUPIL_DIAMETER_MM = 12.0
N_ZONES = 64
N_PHASE_LEVELS = 12
FLAT_CORE_DIAMETER_UM = 4.2
USEFUL_DIAMETER_UM = 6.0
```

Editable parameters at the top include:

- wavelength;
- numerical aperture;
- illuminated pupil diameter;
- input Gaussian-beam radius;
- flat-core diameter;
- useful-probe diameter;
- soft-edge position and width;
- number of annular zones;
- number of phase/depth levels;
- assumed depth error;
- surface roughness;
- relative weights assigned to flatness, edge smoothness, useful energy and sidelobe suppression.

For a future fabrication decision, useful comparison cases are:

```text
beam diameter:  10, 12 mm
zones:          48, 64, 80
phase levels:   8, 12, 16
```

The current default is **12 mm / 64 zones / 12 levels**.

## What the model does not yet include

The model is scalar and axisymmetric. It does not include polarization, vectorial high-NA focusing, the exact microscope objective pupil, refractive-index interfaces in a real microfluidic chip, aberrations, Raman collection through the full optical train, or a measured LIMP surface map.

Those effects should be added when the actual microscope and microfluidic geometry are known. The present scripts are intended for design exploration and for making the assumptions explicit.
