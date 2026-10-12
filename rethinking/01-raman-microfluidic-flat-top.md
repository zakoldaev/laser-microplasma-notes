# 01 — From beam correction to a Raman micro-probe

In 2017 we used laser-induced microplasma processing to fabricate multilevel phase plates directly in fused silica. The goal then was beam homogenization. A five-level plate reduced the measured intensity modulation relative to a binary plate, and the process demonstrated relief control on the order of tens of nanometres.

Reference: R. A. Zakoldaev *et al.*, “Fast Fabrication of Multilevel Phase Plates Used for Laser Beam Correction,” *Journal of Laser Micro/Nanoengineering* 12 (2017), 281–285. [DOI](https://doi.org/10.2961/jlmn.2017.03.0018)

Looking at that result now, I would use the same fabrication capability for a different problem: **making Raman excitation less sensitive to where a particle crosses the focus in a microfluidic channel.**

## The problem

A Gaussian focus gives high peak intensity, but the excitation changes rapidly with lateral position. Two nominally identical particles following slightly different trajectories can therefore produce different Raman amplitudes even if their composition is the same.

For flow measurements, a better probe may be one with a small flat central region and smooth edges. The aim is not maximum peak intensity; it is a more reproducible excitation volume.

## What I would fabricate now

I would not use a random phase plate. I would use a deterministic multilevel annular relief designed for a soft top-hat output.

The current numerical example uses:

```text
wavelength:                785 nm
input beam diameter:       12 mm
objective NA:              0.40
annular zones:             64
phase/depth levels:        12
zone width:                ~100 µm
nominal depth step:        ~140 nm
flat-core diameter:        ~4.2 µm
useful probe diameter:     ~6 µm
```

The soft edge is important. Forcing a sharp top-hat produced strong radial ringing in the first simulations. Giving the field a smooth roll-off made it possible to keep the central region flat while retaining useful energy and suppressing the first sidelobe.

## What the present model gives

For the default 64-zone / 12-level case, the scalar model gives approximately:

```text
energy inside the useful 6 µm probe:  ~0.83
CV inside the flat core:               ~0.011
min/max intensity in the flat core:    ~0.95
first-sidelobe energy:                  ~0.088
```

The optimized output is not a mathematically perfect top-hat. Small ripple remains in the plateau and weak sidelobes remain outside it. That is the useful result: the design is already much flatter than a Gaussian focus without pretending that the ideal target is exactly achieved.

These values are **simulation outputs, not experimental measurements**.

## Why this is interesting

A permanent fused-silica element has no moving parts, needs no active control and can sit directly in a fixed optical train. For a microfluidic Raman system, the practical question is whether this flatter probe reduces event-to-event variation enough to compensate for the lower peak intensity compared with a Gaussian focus.

The metric I would test is therefore not only Raman intensity, but

\[
\frac{\sigma(S)}{\langle S\rangle},
\]

for nominally identical particles under controlled flow.

## Next experiment

The next step is straightforward: fabricate the optimized relief, measure the real surface profile, image the focal field, and compare Raman burst distributions from the same particle suspension with and without the phase plate.

The simulation is intentionally editable. Beam diameter, numerical aperture, number of zones, number of depth levels and the requested output profile can all be changed before fabrication.

Reproducible code and proposed input parameters are in [`simulations/raman-flat-top`](../simulations/raman-flat-top/README.md).
