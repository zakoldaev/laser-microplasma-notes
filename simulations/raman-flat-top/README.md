# Raman flat-top simulations

These scripts support the exploratory note [From random phase plates to a microfluidic Raman probe](../../rethinking/01-raman-microfluidic-flat-top.md).

They are intentionally compact. The goal is not to reproduce a commercial Raman microscope in full detail, but to make the central design questions easy to inspect and modify.

## Requirements

Python 3 with:

```bash
pip install numpy scipy matplotlib
```

## Current recommended first-build design

For the illustrative 785 nm, 5 µm-probe case used in this repository, the present recommendation is **20 concentric annular zones and 8 discrete phase/depth levels**.

Why 20 zones? With a 5 mm illuminated pupil, 20 equal radial zones correspond to about **125 µm per annulus**. This gives the optimizer enough independent phase regions to reshape the focal profile while keeping every fabricated feature far wider than a few-micrometre LIMP writing limit. It is therefore a deliberately conservative geometry for a first physical optic.

Why 8 levels? At 785 nm the fused-silica full-2π relief in the present model is about **1.73 µm**, so 8 phase states are separated by about **0.217 µm in depth**. That spacing is comfortably larger than the ~50 nm depth-control scale demonstrated in the earlier LIMP work. The nominal relief levels are approximately:

```text
0.000, 0.217, 0.433, 0.650,
0.866, 1.083, 1.300, 1.516 µm
```

This should be read as the **recommended first-build compromise**, not a universal optimum. If the optic is going to be fabricated, rerun the model with the real beam and microscope parameters and compare a small sweep such as:

```text
zones:        12, 16, 20, 24, 32
phase levels: 4, 8, 16
```

If the real setup remains close to the illustrative case, **20 zones / 8 levels is the configuration to fabricate first**.

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

The script uses a scalar radial diffraction model and searches over discrete annular phase levels. It is a deliberately simple fabrication-aware model: the phase plate consists of concentric annular zones, each assigned one of a finite number of relief depths.

Editable parameters at the top include:

- wavelength;
- numerical aperture;
- illuminated pupil diameter;
- input Gaussian-beam radius;
- desired flat-top diameter;
- number of annular zones;
- number of phase/depth levels;
- assumed depth error;
- surface roughness.

The optimizer minimizes intensity variation inside the desired probe while penalizing light immediately outside it. It then evaluates fabrication tolerance with Monte-Carlo depth errors.

## What the model does not yet include

The model is scalar and axisymmetric. It does not include polarization, vectorial high-NA focusing, the exact microscope objective pupil, refractive-index interfaces in a real microfluidic chip, aberrations, Raman collection through the full optical train, or a measured LIMP surface map.

Those effects should be added when the actual microscope and microfluidic geometry are known. The present scripts are intended for design exploration and for making the assumptions explicit.
