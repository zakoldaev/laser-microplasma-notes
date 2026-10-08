# Porous-glass sealing and passivation — surface densification by laser microplasma processing

This note covers the first practical material result in the archive: forming thermally densified surface layers on porous glass to slow aging while preserving the internal pore network.

The 2015 passivation paper described the result in terms of **thermal densification** using a graphite target. In this repository, it is treated as the first application in the broader laser microplasma processing story because the same glass–graphite geometry later developed into LIBBH/LIMP studies and micro-optical fabrication.

## The practical question

Porous glass is useful because its connected nanoscale pore network can host liquids, molecules and functional materials. The same open structure also makes it vulnerable to environmental adsorption and gradual changes in optical properties.

The question was therefore:

> Can the outer surface be densified enough to slow aging without sintering the porous structure throughout the whole sample?

The experiment used porous glass in tight contact with compacted graphite. A pulsed ytterbium-fiber laser passed through the glass and was absorbed by the graphite, producing a localized high-temperature interaction at the interface.

There is little photographic documentation from this early stage. At the time, everyday phone cameras were not yet good enough for useful laboratory documentation, and most of the digital material around the project came later. If I recover photographs, scans or other material that genuinely belongs to this experiment, I will add it here.

The published passivation study reports a wavelength of about 1.06 µm, pulse duration of 100 ns and repetition rate of 30–50 kHz for formation of the thermally densified layer.

## What the paper demonstrated

The result was not simply a laser mark. The treatment produced a functional near-surface modification while the deeper porous structure remained.

The main findings were:

- a modified near-surface region was observed after laser treatment;
- the published cross-sectional images show a region extending roughly 30–35 µm under the reported multipulse conditions, but this dimension should not automatically be interpreted as the true depth of laser-induced densification;
- the internal porous structure remained below the modified surface region;
- graphite contamination could be removed on the same laser system using a wet-cleaning step with distilled water;
- optical stability during storage improved strongly compared with untreated porous glass.

Looking back at those cross sections, there is an important ambiguity. Porous glass itself is produced by chemical leaching, which creates a porous near-surface region, and at the magnification used in the published cross-sectional images it is difficult to separate that pre-existing chemically modified region from the much thinner zone affected directly by the laser-driven interaction. The actual plasma- and heat-induced structural change may therefore have been confined to a substantially thinner, micron-scale surface layer. I now treat the reported 30–35 µm value as the extent of the visible cross-sectional region rather than a precise measurement of the laser-modified depth.

The transmission result needs one important distinction. Forming the densified layers initially reduced the transmission coefficient by less than about **5–10%** across the measured range. The treated samples were then stored in laboratory air with relative humidity above 70% for 10 months, and the paper reports no significant additional decrease in transmission over that period.

## Cleaning was part of the method

Graphite particles deposited during processing were a practical problem. The published work used a thin layer of distilled water and laser scanning to remove them.

This detail matters because it shows the difference between observing an interesting glass–target interaction and developing a usable processing route. Surface modification, contamination and cleaning had to be considered together.

A later 2017 paper returned specifically to the spectral changes caused by laser-microplasma processing of quartz glass and compared wet laser cleaning, thermal treatment and chemical cleaning [4]. That work confirmed that cleaning and surface condition were important for preserving optical transmission.

## From porous-glass passivation to dense-glass structuring

Once a localized surface modification could be produced in porous glass, the next question was whether the same target-assisted geometry could shape dense transparent glass.

The purpose changed:

```text
porous glass → stabilize the material
fused silica → create controlled surface relief
```

The early glass-surface-modification paper used the historical term **laser-induced black-body heating (LIBBH)**. The following *Optics and Lasers in Engineering* paper then demonstrated fast microstructuring of fused silica and other silica glasses and tested the fabricated relief as diffraction gratings and random phase plates.

This was the transition from passivation to micro-optical fabrication.

## First public presentation of the technology

LPM 2014 in Vilnius was the first time I presented this technology at a conference. The conference record already shows both parts of the idea emerging: **laser densification of porous glass** and **LIBBH as a method for surface stabilization and modification of porous glass** [5,6]. The journal papers followed in 2015.

For me, this was the point where the work first moved out of the laboratory and became a research direction that we could present publicly, discuss with the community and develop further.

> [!IMPORTANT]
> **TODO:** Add the original LPM 2014 presentation and a few photographs from the conference when I recover and prepare them for the repository.

## Connection to the next note

[Note 02](02-master-thesis-summary.md) uses the master’s thesis as a map of the next stage: process-window studies in fused silica, microlens arrays, random phase plates, diffraction gratings and beam shaping.

## References

1. M. M. Sergeev, G. K. Kostyuk, **R. A. Zakoldaev**, E. B. Yakovlev, “Laser-induced passivation of porous glass to protect it from chemical degradation and aging,” *Protection of Metals and Physical Chemistry of Surfaces* 51 (2015), 427–434. https://doi.org/10.1134/S207020511503020X
2. **R. A. Zakoldaev**, M. M. Sergeev, G. K. Kostyuk, V. P. Veiko, “Laser-induced Black-body Heating (LIBBH) as a Method for Glass Surface Modification,” *Journal of Laser Micro/Nanoengineering* 10 (2015), 15–19. https://doi.org/10.2961/jlmn.2015.01.0003
3. G. K. Kostyuk, M. M. Sergeev, **R. A. Zakoldaev**, E. B. Yakovlev, “Fast microstructuring of silica glasses surface by NIR laser radiation,” *Optics and Lasers in Engineering* 68 (2015), 16–24. https://doi.org/10.1016/j.optlaseng.2014.12.004
4. V. V. Koval, M. M. Sergeev, **R. A. Zakoldaev**, G. K. Kostyuk, “Changes in the spectral characteristics of quartz-glass plates when they are processed with laser-induced plasma,” *Journal of Optical Technology* 84 (2017), 447–452. https://doi.org/10.1364/JOT.84.000447
5. G. K. Kostyuk, M. M. Sergeev, V. P. Veiko, E. B. Yakovlev, **R. A. Zakoldaev**, “Laser Densification of Porous Glasses for Multiple Photonics Applications,” *15th International Symposium on Laser Precision Microfabrication (LPM 2014)*, Vilnius, Lithuania, abstract p. 137.
6. V. P. Veiko, **R. A. Zakoldaev**, G. K. Kostyuk, M. M. Sergeev, “Laser Induced Black Body Heating (LIBBH) – the New Method for Surface Stabilization and Modification of Porous Glasses,” *15th International Symposium on Laser Precision Microfabrication (LPM 2014)*, Vilnius, Lithuania, abstract p. 139.
