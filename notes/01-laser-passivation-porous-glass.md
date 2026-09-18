# Behind the experiment 01 — Laser passivation of porous glass

## Why this note comes first

This experiment is the starting point for the research line that later developed into laser-induced black-body heating (LIBBH), laser microplasma processing, and fabrication of functional micro-optical structures on glass.

The original result was first published in Russian in 2015 and subsequently appeared in English translation.

Rather than starting this archive from the later phase-grating work, this note records the earlier finding: a laser-assisted route to form thermally densified surface layers on porous glass while preserving the porous structure inside the material.

## Original publication

### Russian original

М. М. Сергеев, Г. К. Костюк, Р. А. Заколдаев, Е. Б. Яковлев  
«Лазерная пассивация пористого стекла для защиты от химической деградации и старения»  
*Физикохимия поверхности и защита материалов*  
2015, Т. 51, № 3, С. 314–322.  
DOI: https://doi.org/10.7868/S0044185615030201

### English translation

M. M. Sergeev, G. K. Kostyuk, R. A. Zakoldaev, E. B. Yakovlev  
“Laser-induced passivation of porous glass to protect it from chemical degradation and aging”  
*Protection of Metals and Physical Chemistry of Surfaces*  
2015, Vol. 51, pp. 427–434.  
DOI: https://doi.org/10.1134/S207020511503020X

The English publisher record explicitly identifies the paper as a translation of the original Russian article.

## Scientific problem

Porous glass has a highly developed internal surface and can absorb water, carbon dioxide, and organic molecules from the environment.

Those interactions are useful when porous glass is used as a host material, but they also create a practical problem: the material can undergo chemical degradation and aging, with changes in optical and physicochemical properties over time.

The question behind this work was therefore:

> Can we locally densify only the external surface of porous glass strongly enough to protect it, while preserving the porous structure inside?

This is an interesting materials-processing problem because complete sintering would destroy the pore network that gives porous glass many of its useful properties.

## Main finding

The work demonstrated the formation of thermally densified layers on the surfaces of porous-glass wafers.

The densified surface acted as a passivation layer, while the complex porous structure inside the glass was retained.

The published study reported that even approximately 10 months after the densified layers had been formed, the loss of optical transmittance across the measured wavelength range remained below about 5–7%.

This provided experimental evidence that localized laser-assisted thermal densification could be used not simply to modify porous glass, but to stabilize it against environmental aging.

## Published processing parameters

| Parameter | Published value |
| --- | --- |
| Laser type | Ytterbium fiber laser |
| Wavelength | ~1.06 µm |
| Pulse duration | 100 ns |
| Repetition frequency | 30–50 kHz |
| Material | Porous glass |
| Main result | Thermally densified surface layer |
| Function | Passivation against chemical degradation and aging |

The processing also involved graphite, which absorbed the incident near-infrared radiation and enabled strong localized heating near the glass surface.

A later goal of this archive is to reconstruct the exact geometry and process sequence from the original records.

## Why this result mattered later

This experiment introduced several ideas that became important in the later research:

1. transparent glass does not need to absorb the laser radiation strongly itself;
2. an absorbing material placed close to the glass can convert laser energy into highly localized heating;
3. the resulting high-temperature region can modify the glass surface;
4. the process can be spatially controlled by scanning the laser;
5. the resulting modification can have a useful optical or functional purpose.

Those principles later became the basis for broader LIBBH and laser-microplasma processing studies, including glass microstructuring and fabrication of micro-optical elements.

## From passivation to microstructuring

The important transition was conceptual.

In this first application, the goal was mainly functional surface stabilization:

laser interaction → local heating → densification → passivation.

Later, the same general processing idea was developed toward controlled surface shaping:

laser interaction → localized high-temperature region / microplasma → controlled relief → optical function.

That shift eventually enabled phase gratings, random phase plates, multilevel phase elements, and processing of other transparent materials.

## Experimental details to recover

The publication provides the validated scientific result, but the practical implementation should be reconstructed from original laboratory material where possible.

Important questions:

- What was the exact glass–graphite geometry?
- Was the graphite in direct contact with the glass for all experiments?
- What graphite material and surface preparation were used?
- What laser power and scanning speeds were used for individual samples?
- How many scans were required to form the densified layer?
- How was the focal plane positioned relative to the graphite and glass interface?
- What processing conditions produced incomplete densification?
- What conditions caused damage or excessive deformation?
- How uniform was the densified layer across the processed area?
- How reproducible was the passivation from sample to sample?

## Data and images to recover

Possible archive structure:

```text
data/
    transmission/
    surface-profiles/
    process-parameters/

images/
    setup/
    porous-glass-before/
    porous-glass-after/
    microscopy/
    scanning-probe-microscopy/
```

Priority items:

- photographs of the original setup;
- photographs of porous-glass samples;
- original transmission spectra;
- scanning-probe microscopy data;
- surface profiles;
- processing parameter tables;
- measurements performed immediately after processing;
- long-term measurements used to evaluate aging;
- unsuccessful or damaged samples.

## What did not fit into the paper?

This section will be completed from original records and personal recollection.

Potentially useful material includes:

- early attempts before a stable process window was found;
- samples that cracked or deformed;
- practical problems with graphite contamination;
- cleaning procedures;
- alignment sensitivity;
- variation between porous-glass batches;
- observations about the appearance of the heated region or plasma;
- reasons particular laser parameters were selected.

These details may be especially valuable for researchers trying to reproduce or reinterpret the process.

## Connection to the next papers

This result was followed by papers that expanded the same basic idea from passivation toward glass-surface modification and micro-optical fabrication.

Two important 2015 papers are:

R. A. Zakoldaev, M. M. Sergeev, G. K. Kostyuk, V. P. Veiko  
“Laser-induced Black-body Heating (LIBBH) as a Method for Glass Surface Modification”  
*Journal of Laser Micro/Nanoengineering* 10(1), 15–19 (2015).  
DOI: https://doi.org/10.2961/jlmn.2015.01.0003

G. K. Kostyuk, M. M. Sergeev, R. A. Zakoldaev, E. B. Yakovlev  
“Fast microstructuring of silica glasses surface by NIR laser radiation”  
*Optics and Lasers in Engineering* 68, 16–24 (2015).  
DOI: https://doi.org/10.1016/j.optlaseng.2014.12.004

Those studies moved the research from stabilization of porous glass toward deliberate surface microstructuring and fabrication of optical elements.

## What I would investigate today

This section is retrospective and is not part of the original published claims.

With current instrumentation, the experiment could be revisited using:

- high-speed or spectrally resolved imaging of the interaction region;
- thermal imaging of the glass–graphite interface;
- automated control of focal position;
- spatial mapping of densification depth;
- Raman or vibrational spectroscopy before and after processing;
- automated analysis of surface morphology;
- statistical process-window mapping;
- correlation between plasma/thermal signatures and resulting densification;
- long-term environmental aging tests under controlled humidity and temperature.

Such measurements could help connect the practical processing window to the underlying thermal and plasma-assisted physics.

## Status and provenance

Status: working scientific archive.

Information added here should be labelled as:

- **Published** — reported in the peer-reviewed publication.
- **Original data** — experimental files recovered from the project.
- **Laboratory record** — parameters or observations recovered from notebooks/logs.
- **Personal recollection** — retrospective observation, explicitly marked as such.
- **New analysis** — analysis performed after publication.

The aim is to preserve both the published science and the practical experimental knowledge around it without mixing original evidence with later interpretation.
