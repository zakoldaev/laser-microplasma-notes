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

## Updated design target: flat core + smooth edges + enough energy

The first 20-zone / 8-level calculation was useful for establishing that a permanent LIMP-fabricated element could flatten the central Raman probe. It also showed the main limitation of a coarse annular design: strong radial structure appears when the optimizer is forced to concentrate energy into a small hard-edged top-hat.

The updated target is therefore not a mathematically sharp top-hat. It is a **soft top-hat** with three simultaneous goals:

1. a flat central excitation region;
2. a smooth radial roll-off rather than a sharp edge that produces ringing;
3. enough optical energy retained inside the useful Raman probe.

For the present 785 nm concept I would target a flat core of about **4–4.5 µm diameter**, followed by a smooth roll-off so that the useful probe is about **5.5–6 µm diameter**. This is still small enough to match a hydrodynamically focused microfluidic stream, while giving the optimizer more freedom to suppress rings and sidelobes.

## What phase element would I fabricate now?

For this application I would not begin with a classical random phase plate. A random plate is designed to redistribute coherent light over a broad field and naturally produces speckle and sidelobes. For a compact Raman interrogation volume, the better problem formulation is:

> design the **LIMP-fabricable multilevel phase profile** that transforms the input Gaussian beam into a soft micro-flat-top while balancing flatness, edge smoothness, useful energy and fabrication tolerance.

### Recommended first-build geometry

The present first-build recommendation is:

- **785 nm** operation;
- an expanded input beam of about **10–12 mm diameter**;
- **64 concentric annular zones**;
- **12 discrete phase/depth levels**;
- a soft top-hat target with a **4–4.5 µm flat core** and **5.5–6 µm useful diameter**;
- optimization that explicitly penalizes radial ripple and light in the first sidelobe region.

For a 12 mm illuminated diameter, 64 radial zones correspond to a nominal zone width of about **94 µm**, which I would round to **~100 µm** in the discussion. For a 10 mm beam the same 64-zone design gives about 78 µm per zone. Both are still far larger than the few-micrometre lateral feature size available to the LIMP process, so the geometry remains conservative from the fabrication side.

At 785 nm, using fused silica with refractive index about 1.453, the full 2π relief is approximately **1.73 µm**. Twelve equally spaced phase states give a nominal depth increment of about **0.14 µm**, or **~140 nm**. This remains comfortably larger than the roughly 50 nm depth-control scale demonstrated in the earlier LIMP work, while giving substantially more phase freedom than the earlier eight-level design.

I would therefore choose **64 zones / 12 levels** before moving to a still finer design. A 16-level element is possible in principle, but its depth spacing is only about 0.11 µm, leaving less margin for depth calibration, local roughness and drift. Likewise, using many more radial zones would increase the optimization freedom but is not obviously necessary while each ~100 µm annulus already remains easy to resolve by the LIMP process.

### Why expand the beam to 10–12 mm?

The larger illuminated diameter gives the phase plate more independent radial degrees of freedom without forcing very narrow fabricated structures. The objective can therefore redistribute phase more smoothly across the pupil instead of making large changes over a small number of broad zones.

For this design, the beam expansion is not intended simply to increase spot size. It is used to give the phase plate a larger optical aperture over which to synthesize a smoother focal distribution.

### What the optimizer should minimize

The revised model no longer minimizes only the intensity variation inside a hard target disk. It balances four terms:

\[
F = w_1\,\mathrm{CV}_{\mathrm{core}}
  + w_2\,(1-\eta_{\mathrm{useful}})
  + w_3\,E_{\mathrm{sidelobe}}
  + w_4\,P_{\mathrm{ripple}}.
\]

Here, \(\mathrm{CV}_{\mathrm{core}}\) measures the flatness of the central region, \(\eta_{\mathrm{useful}}\) is the fraction of optical energy retained in the useful probe, \(E_{\mathrm{sidelobe}}\) penalizes light just outside the target, and \(P_{\mathrm{ripple}}\) penalizes radial oscillation and an excessively sharp edge.

The purpose is not to obtain the flattest possible mathematical profile at any cost. The useful Raman design is the one that gives a sufficiently uniform probe while retaining enough optical power and remaining tolerant to realistic LIMP depth errors.

## If I wanted to fabricate it later

Before making the optic, I would rerun the optimizer with the real microscope parameters and compare a narrow design sweep around the present recommendation:

- **beam diameter:** 10 and 12 mm;
- **zones:** 48, 64 and 80;
- **phase levels:** 8, 12 and 16;
- actual incident Gaussian radius;
- actual objective numerical aperture;
- measured LIMP depth calibration and roughness;
- required flat-core and useful-probe diameters in the microfluidic channel.

The current default is **12 mm / 64 zones / 12 levels** because it gives a practical balance between optical freedom and fabrication margin. The exact optimum should still be recalculated for the real Raman microscope before fabrication.

## Reproducible simulations

Two small scripts accompany this note:

- [`compare_raman_flow.py`](../simulations/raman-flat-top/compare_raman_flow.py) — an application-level model showing why a Gaussian and a quasi-flat-top probe produce different trajectory-dependent Raman signals in microfluidic flow.
- [`optimize_limp_phase_plate.py`](../simulations/raman-flat-top/optimize_limp_phase_plate.py) — a compact radial model that now defaults to a 12 mm beam, 64 annular zones, 12 phase/depth levels and a soft-top-hat target.

The input parameters are grouped at the top of each script. Another reader can change the beam size, wavelength, flat-core diameter, useful-probe diameter, channel width, particle-stream width, numerical aperture, number of relief levels or fabrication uncertainty without rewriting the model.

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
