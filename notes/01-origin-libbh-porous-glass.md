# Behind the experiment 01 — From nanoporous-glass passivation to surface structuring

## Why these papers belong together

These two 2015 papers come from the same experimental family and should be read as one story.

Historically, the work started from **nanoporous glass**. The first question was whether the surface of porous glass could be locally densified to protect the material from chemical degradation and aging while preserving the porous structure inside.

The same experimental setup and physical idea were then developed into a broader method for modifying and structuring transparent glass.

The work was presented at **LPM 2014 in Vilnius** and then developed into two complementary 2015 publications:

1. porous-glass passivation and stabilization;
2. a broader method for glass surface modification and microstructuring.

Rather than repeating the same setup twice, this note keeps the experimental platform in one place and treats the two papers as two outcomes of the same research line.

---

## Publications

### 1. Porous-glass passivation

#### Russian original

М. М. Сергеев, Г. К. Костюк, Р. А. Заколдаев, Е. Б. Яковлев  
«Лазерная пассивация пористого стекла для защиты от химической деградации и старения»  
*Физикохимия поверхности и защита материалов*  
2015, Т. 51, № 3, С. 314–322.  
DOI: https://doi.org/10.7868/S0044185615030201

#### English translation

M. M. Sergeev, G. K. Kostyuk, R. A. Zakoldaev, E. B. Yakovlev  
“Laser-induced passivation of porous glass to protect it from chemical degradation and aging”  
*Protection of Metals and Physical Chemistry of Surfaces* 51 (2015), 427–434.  
DOI: https://doi.org/10.1134/S207020511503020X

### 2. Generalization toward glass surface modification

R. A. Zakoldaev, M. M. Sergeev, G. K. Kostyuk, V. P. Veiko  
“Laser-induced Black-body Heating (LIBBH) as a Method for Glass Surface Modification”  
*Journal of Laser Micro/Nanoengineering* 10(1) (2015), 15–19.  
DOI: https://doi.org/10.2961/jlmn.2015.01.0003

---

## Conference stage — LPM 2014, Vilnius

The work was presented at:

**LPM 2014 — 15th International Symposium on Laser Precision Microfabrication**  
Vilnius, Lithuania  
17–20 June 2014

This conference represents the transition between the early nanoporous-glass experiments and the two journal papers published in 2015.

Material to add later:

```text
conference/
    LPM2014/
        poster/
        photos/
        abstract/
        figures/
```

When available, it will be useful to compare:

- what results were already shown at LPM 2014;
- what was added before journal publication;
- whether terminology or interpretation changed;
- which figures or experimental details never appeared in the papers.

---

## Shared experimental concept

The same basic setup underlies both studies.

A transparent glass sample was placed in contact with, or very close to, an absorbing graphite target.

The near-infrared laser radiation passed through the transparent glass and was strongly absorbed by the graphite.

The graphite converted the laser energy into highly localized heating near the glass surface.

The basic sequence was therefore:

laser radiation  
→ transmission through glass  
→ absorption by graphite  
→ localized high-temperature region  
→ modification of the adjacent glass surface

The main difference between the experiments was not the setup itself, but the **material and intended function**.

| Material / experiment | Intended outcome |
| --- | --- |
| Nanoporous glass | Surface densification and passivation |
| Quartz / fused silica | Controlled surface modification and microstructuring |

This is why the two papers are best treated together.

---

## Where the research started: nanoporous glass

Porous glass was the historical starting point.

Because of its highly developed internal surface, porous glass can interact strongly with water, carbon dioxide, and other molecules from the environment. This is useful for infiltration and sensing, but it also makes the material vulnerable to chemical degradation and aging.

The first question was therefore:

> Can only the external surface be densified strongly enough to protect the glass while keeping the internal pore network intact?

The experiments showed that this was possible.

The densified surface acted as a protective layer while the porous structure inside the material remained.

The published study also reported long-term optical stability: after about 10 months, the loss of optical transmittance remained only a few percent across the measured spectral range.

That result established that the laser-assisted approach could create a functional surface layer without fully sintering the porous material.

---

## From one materials problem to a general method

The important next step was conceptual.

Once localized surface densification worked on porous glass, the same processing principle was considered more broadly:

> If localized heating can densify porous glass, can the same interaction be controlled to shape and modify other transparent glasses?

In the 2015 JLMN paper, this approach was described as **laser-induced black-body heating (LIBBH)**. Here that name is kept only as historical terminology associated with the paper.

The research direction therefore evolved as:

porous-glass aging problem  
→ local surface densification  
→ passivation  
→ broader target-assisted glass-processing concept  
→ controlled surface relief  
→ micro-optical structures

This transition is the main reason the two 2015 papers belong in one note.

---

## Published processing parameters

The porous-glass passivation work reports a ytterbium fiber laser around 1.06 µm with approximately 100 ns pulses and a repetition frequency in the tens of kilohertz.

The later 2015 surface-modification paper used the same general class of pulsed near-infrared fiber-laser processing with graphite as the absorber.

Exact parameter sets for each sample should be added from the original papers, notebooks, or data files rather than reconstructed from memory.

Important variables to recover later:

- laser power or pulse energy;
- pulse duration;
- repetition frequency;
- scanning speed;
- number of passes;
- focal position;
- glass–graphite separation/contact;
- graphite type and surface condition;
- glass thickness;
- sample cleaning;
- area processed per scan;
- conditions that caused incomplete modification or damage.

---

## What changed when the material changed?

This is one of the useful questions for the archive.

### Nanoporous glass

The goal was mainly densification and stabilization.

Useful data to recover:

- transmission spectra;
- aging measurements;
- microscopy;
- surface profiles;
- densification depth;
- before/after images;
- differences between glass batches.

### Quartz / fused silica

The goal shifted toward controlled relief formation and surface structuring.

Useful data to recover:

- profilometry;
- optical microscopy;
- relief depth;
- roughness;
- processing speed;
- micro-optical structures;
- failed or unstable regimes.

The setup remained largely the same, but the process window and desired outcome changed with the material.

---

## Practical questions worth reconstructing

This section will be filled gradually from original files and recollection.

Questions that are especially useful for somebody trying the method today:

- How critical was direct contact with graphite?
- How sensitive was the process to focal position?
- How quickly did the graphite surface change during processing?
- How much contamination reached the glass?
- What cleaning procedure worked best?
- Which glass types were easiest to process?
- Which regimes produced cracking, roughness, or excessive deformation?
- How reproducible was the densification from sample to sample?
- How did porous glass behave differently from dense silica?
- What did the interaction region look like during processing?
- Which parameters mattered most in everyday laboratory work?

---

## Material to recover

A compact archive could use one shared setup folder and separate material-specific folders:

```text
images/
    setup/
    porous-glass/
    quartz-glass/

data/
    porous-glass/
        transmission/
        aging/
        microscopy/
    quartz-glass/
        profilometry/
        microscopy/
        process-parameters/

conference/
    LPM2014/
        poster/
        photos/
        abstract/
        figures/
```

This avoids duplicating the same setup and processing description across several notes.

---

## What did not make it into the papers?

To be added later.

Potentially valuable material includes:

- early unsuccessful trials;
- damaged or cracked samples;
- unstable graphite–glass contact;
- contamination problems;
- preliminary processing regimes;
- abandoned parameter ranges;
- early photographs of the interaction zone;
- results shown at LPM 2014 but omitted from the final articles;
- practical observations about repeatability.

These details are likely to be more useful to new researchers than repeating the published conclusions.

---

## Connection to the next stage

After the broader processing concept had been established, the work moved toward more deliberate surface microstructuring and functional optical elements.

An important next paper was:

G. K. Kostyuk, M. M. Sergeev, R. A. Zakoldaev, E. B. Yakovlev  
“Fast microstructuring of silica glasses surface by NIR laser radiation”  
*Optics and Lasers in Engineering* 68 (2015), 16–24.  
DOI: https://doi.org/10.1016/j.optlaseng.2014.12.004

Later work continued toward phase gratings, random and multilevel phase structures, processing of crystalline materials, and a more explicit study of laser microplasma and focusing conditions.

---

## Status and provenance

Status: working scientific archive.

Information in this note should be identified as:

- **Published** — reported in the peer-reviewed papers.
- **Conference history** — material connected with LPM 2014.
- **Original data** — recovered experimental files.
- **Laboratory record** — information from notebooks or saved parameter logs.
- **Personal recollection** — retrospective observation, explicitly marked.
- **New analysis** — analysis performed after publication.

The purpose of this archive is not to reproduce the papers. It is to preserve the experimental development behind them in a compact and useful form.
