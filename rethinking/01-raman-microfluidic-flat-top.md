# From random phase plates to a microfluidic Raman probe

## Why revisit this result?

The 2017 multilevel-phase-plate work demonstrated that laser-induced microplasma processing could form discrete relief levels in fused silica and that a five-level random phase plate improved beam homogenization relative to a binary plate. The reported plate used 200 µm cells; the π-phase depth for fused silica at 633 nm was about 0.69 µm; the demonstrated minimum relief/depth step was about 50 nm; and the roughness of processed cells was about 0.035–0.04 µm Ra. The binary plate produced about 25% intensity modulation, while the five-level plate reduced it to about 9%.

Reference: R. A. Zakoldaev *et al.*, “Fast Fabrication of Multilevel Phase Plates Used for Laser Beam Correction,” *Journal of Laser Micro/Nanoengineering* 12 (2017), 281–285. [DOI](https://doi.org/10.2961/jlmn.2017.03.0018)

The original problem was large-area beam homogenization. A question I would ask now is different: **can the same permanent fused-silica phase-relief technology improve the reproducibility of confocal Raman measurements from particles flowing through a microfluidic channel?**

## Gaussian focus versus a shaped micro-probe

A diffraction-limited Gaussian focus is useful when maximum peak intensity and spatial resolution are the main goals. It is less ideal when nominally identical nanoparticles or molecular aggregates cross the probe volume along slightly different trajectories. Their Raman burst amplitudes can vary simply because the local excitation intensity changes strongly with lateral position.

For a Gaussian beam,

\[
I(r)=I_0\exp\left(-\frac{2r^2}{w^2}\right).
\]

A particle passing close to the optical axis therefore experiences much stronger excitation than an identical particle displaced from the centre.

For a deliberately shaped quasi-flat-top probe,

\[
I(r)\approx \mathrm{constant}\qquad r<R,
\]

so particles crossing different trajectories inside the useful probe area can experience more similar excitation. The objective is not necessarily to increase the peak Raman signal. It is to reduce the part of the measured signal variation that comes from particle position rather than particle composition, concentration or residence time.

In a confocal instrument the relevant response is the overlap between excitation and collection:

\[
S \propto \int I_{\mathrm{exc}}(x,y,z)\,C_{\mathrm{det}}(x,y,z)\,\rho(x,y,z)\,dV.
\]

A shaped excitation area much larger than the confocal collection volume wastes optical power. The target should therefore be a **small micro-flat-top matched to the microfluidic stream and confocal detection volume**, not a large homogenized beam.

## First design question

For an illustrative 785 nm Raman system, I would start by comparing a normal Gaussian probe with shaped probes around 3–8 µm diameter for a hydrodynamically focused particle stream. A simple trajectory model already shows the expected trade-off: a very small flat-top preserves high intensity but remains sensitive to trajectory; a very large flat-top improves uniformity but spreads too much power outside the useful confocal volume. In the first exploratory calculation, a probe around **5 µm diameter** gave a useful compromise.

This is not yet an experimental result. It is a design hypothesis that should be recalculated for the actual objective numerical aperture, beam diameter, microfluidic-channel geometry, particle-position distribution and confocal collection function.

## What phase element would I fabricate now?

For this application I would not begin with a classical random phase plate. A random plate is designed to redistribute coherent light over a broad field and naturally produces speckle and sidelobes. For a compact Raman interrogation volume, the better problem formulation is:

> design the **LIMP-fabricable multilevel phase profile** that transforms the input beam into the required micro-scale intensity distribution while keeping sidelobes and sensitivity to fabrication errors low.

A first constrained numerical design used:

- fused silica at 785 nm;
- 8 discrete phase/depth levels;
- a 5 mm illuminated pupil;
- a target probe diameter of about 5 µm;
- concentric annular zones as a deliberately simple fabrication geometry;
- current working fabrication constraints of about 50 nm depth uncertainty and tens-of-nanometres surface roughness.

The resulting candidate is a deterministic annular multilevel phase plate rather than a random square-cell pattern. For the illustrative parameters, the full 2π fused-silica relief is about 1.73 µm and the 8-level depth increment is about 0.22 µm, comfortably larger than the depth step demonstrated in the earlier LIMP work.

The present calculation should be treated as a starting geometry, not a final optic. The optimum depends directly on the real microscope objective, entrance beam, focal geometry and required probe diameter.

## Reproducible simulations

Two small scripts accompany this note:

- [`compare_raman_flow.py`](../simulations/raman-flat-top/compare_raman_flow.py) — an application-level model showing why a Gaussian and a quasi-flat-top probe produce different trajectory-dependent Raman signals in microfluidic flow.
- [`optimize_limp_phase_plate.py`](../simulations/raman-flat-top/optimize_limp_phase_plate.py) — a compact radial model that searches for an 8-level annular fused-silica phase plate under editable optical and fabrication constraints.

The input parameters are grouped at the top of each script. The intention is that another reader can change the beam size, wavelength, target probe diameter, channel width, particle-stream width, numerical aperture, number of relief levels or fabrication uncertainty without rewriting the model.

## What should be tested experimentally?

The simulation becomes useful only if it predicts a measurable improvement. I would test the idea in stages:

1. measure the fabricated phase profile and compare it with the designed relief;
2. image the focal intensity distribution with and without the phase plate;
3. measure Raman bursts from a reproducible particle or bead suspension under flow;
4. compare the distribution of burst amplitudes for Gaussian and shaped excitation at the same incident optical power;
5. determine whether reduced trajectory-induced variance compensates for any loss in peak intensity or collection efficiency.

The key metric is therefore not only maximum Raman intensity. A more relevant quantity for flow measurements is the relative event-to-event variation,

\[
\frac{\sigma(S)}{\langle S\rangle},
\]

for nominally identical particles under controlled flow conditions.

If this quantity decreases without an unacceptable loss of signal-to-noise ratio, the phase-shaped probe has a practical advantage for quantitative Raman measurements in microfluidics.
