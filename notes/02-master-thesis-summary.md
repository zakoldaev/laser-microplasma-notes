# Research story 02 — Master’s thesis: from one glass-processing setup to several optical functions

## Where this thesis sits in the story

By the time I completed my master’s thesis, our team had already moved from the first experiments on nanoporous glass to a broader question:

> Could the same simple target–glass geometry be used as a practical platform for modifying different transparent glasses and fabricating functional optical structures?

The thesis brought together several strands that had developed through the earlier experiments, the LPM 2014 conference in Vilnius, and the first 2015 publications. Its value was not one single optical element. It was the attempt to understand one processing platform as a family of applications: porous-glass stabilization, controlled surface relief, beam homogenization, beam splitting, and parallel laser processing.

This note is a short English retrospective for a broad scientific audience. It does not reproduce the full Russian thesis. It highlights the main experimental logic, the most useful quantitative results, and the parts that connect directly to the published papers.

## What was available at the time

Around 2014–2015, glass microstructuring already had several established routes. Lithography combined with reactive-ion etching could produce high-quality micro-optical structures, but required multiple fabrication steps and dedicated infrastructure. Ion exchange was well established for refractive-index engineering, while direct laser writing, femtosecond processing, laser-assisted chemical etching, and backside laser-processing methods were expanding the range of structures that could be made in glass.

The motivation of our work was therefore not that glass structuring was impossible. It was to explore whether a much simpler, maskless processing route could be useful: a laser, transparent glass, an absorbing target, beam scanning, and post-processing only when needed.

Retrospectively, this is what makes the approach interesting for me today: it points toward affordable, potentially cleanroom-free glass microstructuring rather than a replacement for mature lithographic fabrication.

## One processing platform

The basic experimental geometry was simple.

A pulsed ytterbium-fiber laser at 1.064 µm was focused through the transparent glass onto the interface between the glass and a plate of pressed graphite. The thesis reports pulse durations of about 50–200 ns, repetition rates of 20–100 kHz, galvanometric beam scanning, and a focusing lens with a focal length of about 210 mm.

The glass transmitted most of the processing radiation, while graphite acted as the strong broadband absorber.

The process can be summarized as:

laser beam  
→ transmission through glass  
→ absorption by graphite  
→ rapid local heating / graphite ablation / plasma formation  
→ modification of the adjacent glass surface

The exact physical contribution of heating, ablation, plasma, shock waves, and material transfer was not fully resolved in the thesis. That uncertainty is important to preserve rather than rewrite retrospectively.

The thesis estimated very high transient temperatures from the laser-energy balance, but also noted that the graphite thermal properties made this estimate uncertain. A thermal camera with insufficient temporal resolution to capture the pulse itself measured average temperatures of roughly 450–650 °C close to the processing zone. Formation of carbon foam-like material was also used as an experimental indication that much higher local temperatures occurred during the interaction.

## 1. Mapping a practical processing window

One of the useful results of the thesis was that glass composition mattered strongly.

For fused silica, a typical successful condition was around 15 W average power and a scanning speed of about 300 mm/s, producing smooth microstructures without visible cracking or chipping.

The same conditions could cause cracks or even severe damage in other glasses such as BK7 or US-1. The thesis therefore treated the process not as a universal recipe, but as a material-dependent window controlled by laser power, scan speed, pulse duration, repetition rate, and the thermomechanical properties of the glass.

For fused silica, the relief depth could be adjusted approximately from 0.2 to 5 µm by changing the laser power, pulse duration, and number of passes. Over the tested range, relief depth was approximately linear with laser power.

This tunability was important because phase optical elements require not only lateral patterning, but controlled relief depth.

## 2. Stabilizing nanoporous glass

The historical starting point of this work was nanoporous glass.

Porous glass can absorb water, carbon dioxide, and organic molecules from air. Over time this can change its optical properties and produce visible aging. The thesis explored whether only the outer surface could be densified while the internal pore network remained available.

Typical processing conditions for porous glass were:

| Parameter | Thesis range |
| --- | --- |
| Average power | ~10–14 W |
| Repetition rate | 20 or 50 kHz |
| Scan speed | ~0.3–0.7 m/s |
| Line overlap | ~15–35 µm |

The laser-treated surface formed a densified layer. Cross-sectional microscopy showed a layer around 30–35 µm thick under the tested multipulse conditions, while the deeper porous structure remained.

The strongest practical result was the long-term stability test. Treated and untreated samples were stored for 10 months in laboratory air at relative humidity above 70%. Creating densified layers initially reduced transmission by roughly 5–10%, but the treated samples then remained essentially stable over the measured spectral range. Untreated porous-glass samples showed clear degradation with storage time.

The thesis also included nanoscale surface images showing open pores before treatment, pore closure after treatment, and preservation of the densified surface after 10 months.

Related publication:

M. M. Sergeev, G. K. Kostyuk, R. A. Zakoldaev, E. B. Yakovlev,  
“Laser Induced Passivation of Porous Glass to Protect It from Chemical Degradation and Aging,”  
*Protection of Metals and Physical Chemistry of Surfaces* 51 (2015), 427–435.  
DOI: https://doi.org/10.1134/S207020511503020X

The original Russian version was published in *Fizikokhimiya Poverkhnosti i Zashchita Materialov*.

## 3. Turning the same setup into a fabrication tool

The same platform was then applied to dense silicate glass and fused silica.

This was the transition from solving one porous-material problem to using the geometry as a general surface-structuring tool.

The thesis reports fabrication of 10 × 10 mm² micro-optical arrays in approximately 5–15 minutes, depending on element size and spacing. A wet laser-cleaning step was developed to remove graphite particles deposited during processing.

That cleaning step used distilled water on the processed surface and a different laser-scanning regime. One reported condition was about 3500 mm/s scanning speed, 20 kHz repetition rate, 10–12 W average power, 200 ns pulses, and 1–3 passes.

This practical detail is easy to overlook in a journal paper, but it is exactly the kind of information that makes an experimental method usable.

Related publication:

R. A. Zakoldaev, M. M. Sergeev, G. K. Kostyuk, V. P. Veiko,  
“Laser-induced Black-body Heating (LIBBH) as a Method for Glass Surface Modification,”  
*Journal of Laser Micro/Nanoengineering* 10 (2015), 15–19.  
DOI: https://doi.org/10.2961/jlmn.2015.01.0003

The acronym above is retained because it is the terminology used in that publication. In this repository I prefer descriptive language for the broader research direction.

## 4. Functional micro-optics, not only surface features

A major part of the thesis was to show that the fabricated structures could perform optical functions.

### Microlens arrays

Microlens arrays were fabricated on fused silica with typical lens diameters from about 50 to 500 µm and array periods from about 10 to 1000 µm.

For representative arrays with lens diameters of 150–400 µm, measured numerical apertures were about 0.0025–0.0057 and focal lengths about 30–35 mm. The smallest directly measured focal spots were around 90 ± 10 µm, larger than ideal geometric-optics predictions.

This negative result was useful: the fabricated microlenses were not good enough for direct parallel microprocessing simply by focusing with the lenses themselves.

The team therefore tested them in a non-imaging integrator configuration. With an additional microscope objective, the system produced much smaller processing spots and was used to create arrays of holes in a thin titanium film. Feature sizes down to about 10 µm were demonstrated.

### Random phase plates

Random phase plates with characteristic element sizes of roughly 250–680 µm were fabricated and tested for beam homogenization.

The thesis deliberately distorted the input beam and then examined how the fabricated phase plate redistributed the intensity. Beam homogenization was demonstrated experimentally.

Measured optical losses through the phase-plate system were approximately 6.6–9.4%, depending on the measurement condition.

The thesis contains some internal variation in which element size is described as giving the “best” homogenization in different parts of the text, so I do not select one optimum value here. The robust result is that several structures were fabricated and beam homogenization was experimentally demonstrated.

### Diffraction phase gratings

Diffraction phase gratings were fabricated with periods from about 55 to 400 µm and relief depths around 0.2–1.3 µm.

A representative grating had:

- period: ~100 µm
- relief depth: ~0.5 µm
- approximately equal filling of modified and unmodified regions

When tested optically, the ±1 diffraction orders reached about 95% of the intensity of the zero order. The measured spot diameter was about 60 µm and the separation between spots about 1200 µm, close to the corresponding theoretical estimates of about 48 µm and 1210 µm.

The grating was then used for simultaneous processing of a 20 nm titanium film, producing three holes in a single exposure geometry.

Related publication:

G. K. Kostyuk, M. M. Sergeev, R. A. Zakoldaev, E. B. Yakovlev,  
“Fast microstructuring of silica glasses surface by NIR laser radiation,”  
*Optics and Lasers in Engineering* 68 (2015), 16–24.  
DOI: https://doi.org/10.1016/j.optlaseng.2014.12.004

## What the thesis added beyond the papers

Looking back, the thesis was useful because it connected results that otherwise appeared as separate papers.

It showed that:

- the same target–glass geometry could be used with porous and dense glasses;
- processing conditions had to be adapted to the thermomechanical properties of each glass;
- relief depth could be tuned over the micrometer range;
- porous-glass surfaces could be stabilized for long-term storage;
- the same processing platform could fabricate several classes of micro-optical elements;
- those elements could then be tested in real optical functions rather than characterized only by microscopy;
- some designs did not work as well as expected, and the optical testing directly revealed those limitations.

The thesis also made clear what was still unresolved. The relative roles of thermal transfer, graphite ablation, plasma-plume dynamics, shock waves, and deposited carbon particles needed dedicated experiments and modelling.

That open question became part of the later research direction.

## Published and thesis-stage outputs

The thesis publication list includes three papers already published in 2015:

1. “Laser-induced Black-body Heating (LIBBH) as a Method for Glass Surface Modification”
2. “Laser Induced Passivation of Porous Glass to Protect It from Chemical Degradation and Aging”
3. “Fast microstructuring of silica glasses surface by NIR laser radiation”

It also lists two microlens-related manuscripts as under review at the time of thesis submission, plus patent and conference activity.

For this GitHub archive, the peer-reviewed papers remain the primary references. The thesis is useful as the document that connects the experiments and preserves additional detail around them.

## One illustration I would use

Suggested title:

“From one target-assisted laser-processing setup to several functions”

I would make one composite figure, not a collage of many thesis pages.

Center:
- simplified redraw of the common laser → glass → graphite geometry from thesis Fig. 17

Three branches:
- porous glass → densified surface → stable transmission after 10 months
- fused silica → controlled relief → microlens / random phase element
- fused silica → diffraction grating → three-beam parallel processing

The point of the figure should be visible in one second:

> one experimental platform, several materials and optical functions.

I would redraw the setup cleanly and use only one small experimental image for each branch.

## Raw data — to add later

I still have original files from this project that can be added to the repository when I recover them.

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

Priority files to look for:

- original profilometer traces behind the relief-depth plots;
- raw transmission spectra from the 10-month porous-glass study;
- microscopy / scanning-probe microscopy data;
- laser-processing parameter tables;
- CCD intensity distributions;
- diffraction-order measurements;
- original images from the titanium-film processing tests;
- failed or damaged samples, if documented.

When these files are added, each dataset should get a short README explaining what it contains, which figure or result it relates to, and whether it was published, unpublished, or re-analysed later.

## Source and provenance

Primary source for this note: my Russian-language master’s thesis.

The thesis describes collaborative research performed by the team. Formal scientific credit and authorship should be taken from the corresponding papers and their published records.

This GitHub note is a retrospective explanation intended to make the experimental development easier to understand and to preserve details that were distributed across the thesis, papers, conference material, and laboratory records.
