# Raman flat-top simulations

These scripts support the exploratory note [From random phase plates to a microfluidic Raman probe](../../rethinking/01-raman-microfluidic-flat-top.md).

They are intentionally compact. The goal is not to reproduce a commercial Raman microscope in full detail, but to make the central design questions easy to inspect and modify.

## Requirements

Python 3 with:

```bash
pip install numpy scipy matplotlib
```

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
