# Fused-silica phase gratings — laser microplasma processing for beam splitting

> **Summary:** This note follows the diffraction-grating branch of the project: periodic relief was written directly into fused silica, characterized by its depth and profile, and then used as a working beam-splitting element rather than treated only as a surface pattern.

The 2017 paper is also useful for understanding the terminology of this archive. Its title uses **laser microplasma**, while the fabrication route still refers to the earlier **laser-induced black-body heating** description. These names belong to the same experimental line, but they reflect how our interpretation of the process evolved [1].

## Why this experiment mattered

By this stage, changing the glass surface was no longer enough. The relief had to perform a predictable optical function.

The sequence was simple:

```text
laser processing at the glass–graphite interface
→ periodic fused-silica relief
→ phase modulation
→ diffraction
→ beam splitting
```

The practical question was therefore:

> Can the target-assisted nanosecond process create a periodic relief on fused silica that is controlled well enough to give useful diffraction?

## What we fabricated

The published study used an ytterbium-fiber laser at **1.064 µm** and the same general glass–graphite geometry developed in the earlier work [1]. Depending on the experiment, pulse duration ranged from about **4 to 200 ns** and repetition rate from about **10 to 100 kHz**.

The gratings had an approximately sinusoidal surface profile, with relief depths in the range of roughly **0.5–2 µm**. Fabrication time was typically about **1–5 min**, depending on grating size and period [1].

That depth range matters because the grating works mainly through optical phase. A visible groove is not enough; the relief has to be deep and regular enough to redistribute the transmitted light into diffraction orders.

## The optical test was the real result

After fabrication, the grating was not judged only by microscopy or profilometry. Its diffraction pattern was measured and compared with calculation, and the same element was then used in a beam-splitting configuration [1].

For me, this is the important part of the experiment. The chain from fabrication to optical function was complete:

1. create periodic relief in fused silica;
2. measure the resulting diffraction;
3. compare experiment with calculation;
4. use the element as a beam splitter.

That moved the method from surface microstructuring into functional phase optics.

## What was still not under full control

A working grating did not mean that the process itself was fully understood. Reproducibility still depended on focusing conditions, the glass–target gap, surface curvature and the condition of the graphite target. Those questions were studied later in more detail, especially the sensitivity of the interaction to focusing and target geometry [6].

The physical interpretation was also still developing. Later measurements of confined laser-induced microplasma showed that confinement changed the plasma conditions substantially compared with free expansion, including stronger pressure effects and higher particle temperatures. That supported the view that the interaction could not be described as simple heat transfer alone [4].

## The next step: more complex phase profiles

Once a periodic grating could be fabricated and used optically, the next question was whether the same depth-control idea could be extended beyond a single repeating profile.

In 2017 the process was used for multilevel phase plates [2], and automated fabrication was then applied to multilevel elements for laser-beam correction [3]. The same research line later reached spiral phase plates on fused silica for optical-vortex generation [5].

The progression became:

```text
periodic relief
→ diffraction grating
→ multilevel phase plate
→ beam correction
→ spiral phase plate / vortex generation
```

This is why the grating experiment is more than a single device example. It was the point where controllable relief became a platform for progressively more complex phase functions.

## Why this branch still matters

A fixed grating is much less flexible than a programmable spatial light modulator, but it also solves a different problem. Once fabricated, the fused-silica element is passive, compact and permanent, with no electronics or refresh cycle. For high-power or long-term optical systems, those properties can still be valuable.

The broader fabrication question is also still relevant: producing controlled, low-defect relief directly in fused silica remains difficult. So the historical value of this work is not only the grating design itself, but the demonstration that a relatively simple target-assisted nanosecond process could create a functional phase element directly in a hard transparent optical material.

Previous: [Note 02 — fused-silica relief and micro-optics](02-master-thesis-summary.md) · [Research map](../research-map.md)

## References

1. G. K. Kostyuk, **R. A. Zakoldaev**, V. V. Koval, M. M. Sergeev, V. S. Rymkevich, “Laser microplasma as a tool to fabricate phase grating applied for laser beam splitting,” *Optics and Lasers in Engineering* 92 (2017), 63–69. https://doi.org/10.1016/j.optlaseng.2016.12.013
2. V. S. Rymkevich, **R. A. Zakoldaev**, M. M. Sergeev, G. K. Kostyuk, “Using laser-induced microplasma for multilevel phase plate fabrication,” *Journal of Instrument Engineering* 60 (2017), 431–439. https://doi.org/10.17586/0021-3454-2017-60-5-431-439
3. **R. A. Zakoldaev**, G. K. Kostyuk, V. S. Rymkevich, V. V. Koval, M. M. Sergeev, V. P. Veiko, E. B. Yakovlev, A. N. Sivers, “Fast Fabrication of Multilevel Phase Plates Used for Laser Beam Correction,” *Journal of Laser Micro/Nanoengineering* 12 (2017), 281–285. https://doi.org/10.2961/jlmn.2017.03.0018
4. V. P. Veiko, S. A. Volkov, **R. A. Zakoldaev**, M. M. Sergeev, A. A. Samokhvalov, G. K. Kostyuk, K. A. Milyaev, “Laser-induced microplasma as a tool for microstructuring transparent media,” *Quantum Electronics* 47 (2017), 842–848. https://doi.org/10.1070/QEL16377
5. V. Shkuratova, G. K. Kostyuk, M. M. Sergeev, **R. A. Zakoldaev**, E. B. Yakovlev, O. Medvedev, “Rapid fabrication of spiral phase plate on fused silica by laser-induced microplasma,” *Applied Physics B* 126 (2020), 61. https://doi.org/10.1007/s00340-020-7410-x
6. V. S. Rymkevich, M. M. Sergeev, **R. A. Zakoldaev**, “Laser microplasma as a spot tool for glass processing: Focusing conditions,” *Journal of Materials Processing Technology* 292 (2021), 117061. https://doi.org/10.1016/j.jmatprotec.2021.117061
