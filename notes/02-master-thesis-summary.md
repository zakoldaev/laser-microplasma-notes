# From controllable fused-silica relief to functional micro-optics

> **Summary:** This note follows the thesis-stage experiments on fused silica: finding a workable nanosecond-laser processing window, controlling relief from sub-micrometre to several-micrometre depth, and turning that control into microlenses, random phase plates and diffraction phase gratings that were tested optically.

This note starts where the porous-glass work ends. The main question was no longer whether the glass–graphite interaction could modify a transparent material, but whether the same approach could produce controlled relief and functional micro-optical elements on fused silica.

> Can a relatively simple nanosecond-laser setup create controlled surface relief in fused silica and turn that relief into working optical elements?

The experiments therefore progressed from identifying a usable processing window, to controlling relief depth, and then to fabricating and testing microlenses, random phase plates and diffraction phase gratings [1–5].

## Finding a usable window on fused silica

A polished fused-silica plate was placed in contact with pressed graphite. A ytterbium-fiber laser at about **1.064 µm** passed through the transparent glass and was focused at the glass–graphite interface. The pulse duration was varied from **50 to 200 ns**, with repetition rates between **20 and 100 kHz**. The beam was moved with a two-axis scanning system, and the focusing optics had a focal length of about **210 mm** [1,2].

The process window depended strongly on the glass composition. For fused silica, smooth structures without obvious cracks or chips were obtained around **15 W average power** and a scan speed of about **300 mm/s**. Similar conditions on other glasses such as BK7 or US-1 often produced cracking or local destruction. This showed that the useful regime could not be defined only by laser parameters; the thermal and mechanical properties of the glass also had to be considered [2].

Once a stable regime for fused silica was found, the next parameter was relief depth. Average power, pulse duration (**50, 100 and 200 ns**) and the number of passes (**one or three**) were varied. Across the investigated conditions, the formed relief ranged from roughly **0.2 to 5 µm**, and the depth changed approximately linearly with laser power over the tested ranges [2].

At this stage the process was no longer only a surface-modification experiment. The available depth range was sufficient to begin using the relief for optical phase control.

For larger patterns, fabrication was also relatively fast. A structured area of about **10 × 10 mm²** could typically be produced in roughly **5–15 min**, depending on the size and spacing of the elements. Graphite deposited during processing, so wet laser cleaning with distilled water became part of the fabrication sequence [1].

## Microlenses and the limits of the first design

Microlens arrays were used as the first test of whether the fabricated relief could perform a simple optical function.

Arrays were fabricated with lens diameters from about **50 to 500 µm** and periods from **10 to 1000 µm**. Profilometry showed typical lens heights of roughly **1–2 µm**. The written profiles were not ideal spherical caps; the central region tended to be comparatively flat [3].

For detailed optical testing, arrays with lens diameters of **150, 200 and 400 µm** were studied. Their measured focal lengths were about **30–35 mm**, with numerical apertures of **0.0025–0.0057**. The smallest measured focal spot was approximately **90 ± 10 µm**, larger than the simple theoretical estimate [3].

These parameters were insufficient for direct parallel laser micromachining with the microlenses alone. The optical scheme was therefore modified by adding a microscope objective after the array. With this configuration, the spot size in the processing plane was reduced substantially, and arrays of holes of about **10 µm** were produced in a **60 nm titanium film**.

The lens profile also indicated that an additional smoothing step could be useful. Chemical smoothing in hydrofluoric acid for about **15–30 min** rounded the initially flat-topped profile. A later study explored carbon-dioxide-laser smoothing as another route to improve the lens shape [4].

The microlens experiments therefore identified both the optical function and the main limitation of the initial surface profile, which directly motivated the next processing and optical modifications.

## Random phase plates and beam homogenization

The next test was more demanding: instead of making a lens, could the written relief redistribute an uneven laser beam? We fabricated random square cells with two phase levels, **0** and **π**, with the required relief estimated from `hπ = λ / [2(n − 1)]`.

The plates used cell sizes from **250 to 680 µm**. In the first test, with a **10 mm** beam and a **190 mm** collective lens, the **500 µm** plate gave the most uniform output. But when we repeated the concept with a more coherent **532 nm picosecond laser**, interference fringes became stronger and the best result shifted to the **250 µm** plate.

That change was the key result: **beam homogenization was controlled not only by the written phase pattern, but also by the coherence of the laser source.** Optical loss remained about **6.5–9.4%**, and the same fabrication concept later developed into multilevel phase plates for beam correction [1,6].

## Diffraction phase gratings and controlled beam splitting

The diffraction-grating experiments were aimed at a more deterministic function: periodic surface relief with predictable diffraction orders.

Gratings were fabricated with periods from about **55 to 400 µm** and relief depths from about **0.2 to 1.3 µm**. One grating studied in detail had a period of **100 µm**, a modified-width-to-period ratio of about **0.5**, and a relief depth near **0.5 µm**. Profilometry showed an approximately smooth periodic profile rather than a sharp binary trench. The roughness in the region most affected by the plasma reached roughly **0.02–0.03 µm**, while the central part of the written line remained close to the roughness of the original fused-silica surface.

The optical response was measured in the focal plane of a lens and compared with calculation. The agreement was sufficient to proceed to an application test, where the grating was used for simultaneous processing of a **20 nm titanium film**. Depending on the total patterned area, fabrication and cleaning of these diffraction elements took roughly **1–10 min** [5].

This branch later continued into multilevel phase plates for beam correction, where the same principle of controlled permanent surface relief was extended to more complex phase profiles [6].

## What this stage established

By the end of this stage, the glass–graphite process had moved from surface modification to controlled optical fabrication. The experiments established that permanent micrometre-scale relief could be written directly in fused silica over centimetre-scale areas, with relief depth adjusted across roughly **0.2–5 µm** under the investigated conditions.

That control was sufficient to fabricate and optically test three different classes of structures: microlenses, random phase plates and diffraction gratings. The measurements also exposed the main limitations of each approach — non-ideal microlens profiles, coherence-sensitive homogenization and the finite roughness of written grating structures — providing the basis for the later multilevel phase-plate work [1–6].

## Summary of the thesis-stage progression

The work established a useful fused-silica processing window around **15 W** and **300 mm/s** and showed relief control from roughly **0.2 to several micrometres**. That control was then used to fabricate microlenses, random phase plates and diffraction gratings. Optical testing identified the limitations of the first microlens profiles, showed the influence of beam coherence on random phase plates, and demonstrated multi-beam processing with diffraction gratings having periods between **55 and 400 µm**.

The progression from process-window studies to optical testing was important because each stage provided the parameters and limitations needed for the next one.

> [!NOTE]
> **Source:** this note is based on my Russian-language master’s thesis and the papers cited below. I am preparing a shorter English overview of the thesis; when that version is ready for public citation, I will link it here.

Previous: [Note 01 — porous-glass sealing and passivation](01-porous-glass-to-surface-structuring.md) · [Publication trail](03-publication-trail.md) · [Research map](../research-map.md)

## References

1. G. K. Kostyuk, M. M. Sergeev, **R. A. Zakoldaev**, E. B. Yakovlev, “Fast microstructuring of silica glasses surface by NIR laser radiation,” *Optics and Lasers in Engineering* 68 (2015), 16–24. https://doi.org/10.1016/j.optlaseng.2014.12.004
2. G. K. Kostyuk, **R. A. Zakoldaev**, M. M. Sergeev, V. P. Veiko, “Laser-induced glass surface structuring by LIBBH technology,” *Optical and Quantum Electronics* 48 (2016), 249. https://doi.org/10.1007/s11082-016-0531-0
3. G. K. Kostyuk, **R. A. Zakoldaev**, M. M. Sergeev, E. B. Yakovlev, “Microlens array fabrication on fused silica influenced by NIR laser,” *Applied Physics B* 122 (2016), 99. https://doi.org/10.1007/s00340-016-6379-y
4. **R. A. Zakoldaev**, G. K. Kostyuk, V. V. Koval, M. M. Sergeev, V. S. Rymkevich, E. B. Yakovlev, “Microlens array fabrication on fused silica by LIBBH technology with CO₂ laser smoothing,” *Journal of Instrument Engineering* 59 (2016), 400–406. https://doi.org/10.17586/0021-3454-2016-59-5-400-406
5. G. K. Kostyuk, **R. A. Zakoldaev**, V. V. Koval, M. M. Sergeev, V. S. Rymkevich, “Laser microplasma as a tool to fabricate phase grating applied for laser beam splitting,” *Optics and Lasers in Engineering* 92 (2017), 63–69. https://doi.org/10.1016/j.optlaseng.2016.12.013
6. **R. A. Zakoldaev**, G. K. Kostyuk, V. S. Rymkevich, V. V. Koval, M. M. Sergeev, V. P. Veiko, E. B. Yakovlev, A. N. Sivers, “Fast Fabrication of Multilevel Phase Plates Used for Laser Beam Correction,” *Journal of Laser Micro/Nanoengineering* 12 (2017), 281–285. https://doi.org/10.2961/jlmn.2017.03.0018
