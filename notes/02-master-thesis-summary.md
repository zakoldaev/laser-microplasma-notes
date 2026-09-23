# Glass micro-optics by laser microplasma processing — thesis map, surface relief and beam shaping

This note uses my master’s thesis as a map of the early laser microplasma processing work: porous-glass stabilization, fused-silica surface relief, microlens arrays, random phase plates and diffraction gratings.

## Why this note exists

By the time I completed the thesis, the work had moved beyond one porous-glass experiment. The larger question became:

> Could the same glass–carbon geometry become a practical platform for modifying transparent glass and fabricating functional optical structures?

The thesis is useful because it connects results that later appeared as separate publications. It shows one experimental platform branching into several directions: passivation, surface microstructuring, beam homogenization, beam splitting and parallel laser processing.

This page is not a second publication of the thesis. It is a readable map for the GitHub archive.

## Publication trail, 2015–2017

Selected papers connected to the thesis period:

| Year | Topic | Publication |
| --- | --- | --- |
| 2015 | Glass surface modification | R. A. Zakoldaev et al., “Laser-induced Black-body Heating (LIBBH) as a Method for Glass Surface Modification,” *JLMN*. DOI: https://doi.org/10.2961/jlmn.2015.01.0003 |
| 2015 | Porous-glass passivation | M. M. Sergeev et al., “Laser Induced Passivation of Porous Glass to Protect It from Chemical Degradation and Aging,” *Protection of Metals and Physical Chemistry of Surfaces*. DOI: https://doi.org/10.1134/S207020511503020X |
| 2015 | Fast microstructuring and optical testing | G. K. Kostyuk et al., “Fast microstructuring of silica glasses surface by NIR laser radiation,” *Optics and Lasers in Engineering*. DOI: https://doi.org/10.1016/j.optlaseng.2014.12.004 |
| 2016 | Process window and relief control | G. K. Kostyuk et al., “Laser-induced glass surface structuring by LIBBH technology,” *Optical and Quantum Electronics*. DOI: https://doi.org/10.1007/s11082-016-0531-0 |
| 2016 | Microlens arrays | G. K. Kostyuk et al., “Microlens array fabrication on fused silica influenced by NIR laser,” *Applied Physics B*. DOI: https://doi.org/10.1007/s00340-016-6379-y |
| 2017 | Phase gratings and beam splitting | G. K. Kostyuk et al., “Laser microplasma as a tool to fabricate phase grating applied for laser beam splitting,” *Optics and Lasers in Engineering*. DOI: https://doi.org/10.1016/j.optlaseng.2016.12.013 |
| 2017 | Process physics | V. P. Veiko et al., “Laser-induced microplasma as a tool for microstructuring transparent media,” *Quantum Electronics*. DOI: https://doi.org/10.1070/QEL16377 |

Full publication profile: https://scholar.google.com/citations?user=TcIkX-kAAAAJ&hl=en

## One processing platform

The basic geometry was simple:

```text
pulsed NIR laser
→ transparent glass
→ graphite target
→ localized heating / ablation / microplasma
→ modified glass surface
```

The thesis reports a pulsed ytterbium-fiber laser at 1.064 µm, pulse durations of about 50–200 ns, repetition rates of 20–100 kHz, galvanometric beam scanning, and focusing through transparent glass onto pressed graphite.

The exact roles of heat transfer, graphite ablation, plasma dynamics, shock waves and deposited carbon particles were not fully resolved in the thesis. That uncertainty is important: it later became part of the process-physics research direction.

## 1. Processing window for fused silica

One useful thesis result was that glass composition mattered strongly.

For fused silica, a typical successful condition was around 15 W average power and a scanning speed of about 300 mm/s, producing smooth microstructures without visible cracking or chipping. Similar conditions could damage other glasses such as BK7 or US-1.

The relief depth in fused silica could be tuned approximately from 0.2 to 5 µm by changing laser power, pulse duration and number of passes. This mattered because phase optical elements require not only lateral patterning, but controlled relief depth.

## 2. Porous-glass stabilization

The historical starting point was porous glass. The thesis explored whether only the outer surface could be densified while the internal pore network remained available.

Typical porous-glass processing conditions were:

| Parameter | Thesis range |
| --- | --- |
| Average power | ~10–14 W |
| Repetition rate | 20 or 50 kHz |
| Scan speed | ~0.3–0.7 m/s |
| Line overlap | ~15–35 µm |

The treated surface formed a densified layer. Cross-sectional microscopy showed a layer around 30–35 µm thick under the tested multipulse conditions, while the deeper porous structure remained.

The practical result was the long-term stability test: treated and untreated samples were stored for 10 months in laboratory air. Treated samples remained essentially stable over the measured spectral range, while untreated porous-glass samples degraded.

## 3. From surface features to micro-optics

The same laser microplasma processing platform was then used to fabricate functional surface-relief elements in fused silica.

The thesis reports fabrication of 10 × 10 mm² micro-optical arrays in about 5–15 minutes, depending on element size and spacing. A wet laser-cleaning step using distilled water was developed to remove graphite particles deposited during processing.

This practical cleaning step is exactly the kind of detail worth preserving in the archive: it turns an interesting interaction into a usable fabrication workflow.

## 4. Optical functions demonstrated

### Microlens arrays

Microlens arrays were fabricated on fused silica with lens diameters from about 50 to 500 µm. The directly fabricated lenses had low numerical aperture and focal spots larger than ideal predictions, which showed that the first profiles were not yet sufficient for direct high-quality focusing.

That limitation led to follow-up work on CO₂-laser smoothing and reflow.

### Random phase plates

Random phase plates with characteristic element sizes of roughly 250–680 µm were fabricated and tested for beam homogenization. The important result was not a single “best” plate, but the demonstration that laser-written surface relief could redistribute light and act as a functional phase element.

### Diffraction phase gratings

Diffraction gratings were fabricated with periods from about 55 to 400 µm and relief depths around 0.2–1.3 µm.

A representative grating had a period of about 100 µm and a relief depth of about 0.5 µm. The ±1 diffraction orders reached about 95% of the zero-order intensity. The grating was also used for simultaneous processing of a thin titanium film in a three-beam geometry.

This branch later developed into the dedicated phase-grating and beam-splitting paper.

## What the thesis added beyond the papers

Looking back, the thesis was useful because it connected separate papers into one experimental story:

- the same glass–carbon geometry worked with both porous and dense glasses;
- processing conditions depended strongly on glass type;
- relief depth could be tuned over the micrometer range;
- porous-glass surfaces could be stabilized for long-term storage;
- fabricated structures could perform real optical functions;
- some optical elements did not work as well as expected, and those limitations shaped the next experiments;
- unresolved mechanism questions later became a separate process-physics direction.

## Raw data — to add later

Planned location:

```text
data/master-thesis/
    process-window/
    profilometry/
    porous-glass-transmission/
    microscopy/
    microlens-arrays/
    random-phase-plates/
    diffraction-gratings/
    parallel-processing/
```

Priority files to recover:

- profilometer traces behind the relief-depth plots;
- raw transmission spectra from the porous-glass stability study;
- microscopy and scanning-probe microscopy data;
- laser-processing parameter tables;
- CCD intensity distributions;
- diffraction-order measurements;
- images from titanium-film processing tests;
- failed or damaged samples, if documented.

Each dataset should get a short README explaining what it contains, which figure or result it relates to, and whether it was published, unpublished or re-analysed later.

## Source and provenance

Primary source for this note: my Russian-language master’s thesis.

The thesis describes collaborative research performed by the team. Formal scientific credit and authorship should be taken from the corresponding papers and their published records.

This GitHub note is a retrospective explanation intended to make the experimental development easier to understand and to preserve details that were distributed across the thesis, papers, conference material and laboratory records.
