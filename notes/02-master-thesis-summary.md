# From controllable fused-silica relief to functional micro-optics — what the thesis actually showed

> **Summary:** This note follows the thesis-stage experiments on fused silica: finding a workable nanosecond-laser processing window, controlling relief from sub-micrometre to several-micrometre depth, and turning that control into microlenses, random phase plates and diffraction phase gratings that were tested optically.

This note starts where the porous-glass story ends. By the time I was writing my master’s thesis, the question was no longer simply whether the glass–graphite interaction could modify a transparent material. I wanted to know how far the same idea could be pushed on fused silica:

> Can a relatively simple nanosecond-laser setup create controlled surface relief in fused silica and turn that relief into working optical elements?

That question led to a sequence of experiments: first finding a usable processing window, then controlling relief depth, then fabricating microlenses, random phase plates and diffraction phase gratings, and finally testing whether these structures actually changed or divided a laser beam in a useful way [1–5].

## Finding a usable window on fused silica

The setup was still very simple in principle. A polished fused-silica plate was placed in contact with pressed graphite. A ytterbium-fiber laser at about **1.064 µm** passed through the transparent glass and was focused at the glass–graphite interface. In the thesis experiments the pulse duration was varied from **50 to 200 ns**, with repetition rates between **20 and 100 kHz**. The beam was moved with a two-axis scanning system, and the focusing optics had a focal length of about **210 mm** [1,2].

The important lesson was that the process window was narrow enough to matter. For fused silica, smooth structures without obvious cracks or chips were obtained around **15 W average power** and a scan speed of about **300 mm/s**. Using similar conditions on other glasses such as BK7 or US-1 often produced cracking or even local destruction. That was one of the first clear signs that the process could not be described only by laser parameters: the mechanical and thermal properties of the glass were equally important [2].

Once the fused-silica window was found, relief depth became the next control parameter. In the thesis I varied average power, pulse duration (**50, 100 and 200 ns**) and the number of passes (**one or three**). Across the investigated conditions, the formed relief ranged from roughly **0.2 to 5 µm**, and its depth changed approximately linearly with laser power over the tested ranges [2].

That was the point where the method stopped being only a surface-modification experiment. A few micrometres of controllable relief is enough to start thinking in terms of optical phase rather than simply material damage.

For larger patterns, fabrication was also reasonably fast. A structured area of about **10 × 10 mm²** could typically be produced in roughly **5–15 min**, depending on the size and spacing of the elements. Graphite deposited during processing, so wet laser cleaning with distilled water became part of the fabrication sequence rather than a separate cosmetic step [1].

## Microlenses: the first useful limitation

Microlens arrays were the most intuitive place to start because the optical function is easy to understand: create a curved surface and see whether it focuses light.

In the thesis, arrays were fabricated with lens diameters from about **50 to 500 µm** and periods from **10 to 1000 µm**. Profilometry showed typical lens heights of roughly **1–2 µm**. The problem was visible immediately: the laser-written lenses were not ideal spherical caps. Their central region tended to be rather flat [3].

For detailed optical testing, arrays with lens diameters of **150, 200 and 400 µm** were studied. Their measured focal lengths were about **30–35 mm**, with numerical apertures of only **0.0025–0.0057**. The smallest measured focal spot was approximately **90 ± 10 µm**, noticeably larger than the simple theoretical estimate [3].

That result was useful because it told us exactly what was wrong. The structures were definitely lenses, but not yet good lenses for direct parallel laser micromachining. Instead of hiding that limitation, we changed the optical scheme. By using the fabricated array together with an additional microscope objective, the spot size in the processing plane could be reduced strongly, and arrays of holes of about **10 µm** were produced in a **60 nm titanium film**.

The surface profile also suggested the next fabrication step. In the thesis I tested chemical smoothing in hydrofluoric acid for about **15–30 min**, which rounded the initially flat-topped profile. A later study explored carbon-dioxide-laser smoothing as another route to improve the lens shape [4].

Looking back, this is one of the parts of the thesis I still like most: the first device did not meet the original target, but the optical test immediately showed what needed to change.

## Random phase plates: when coherence became the problem

The next structures were random phase plates intended to redistribute an inhomogeneous beam into a more uniform intensity pattern.

The fabricated elements used random square features with lateral sizes between **250 and 680 µm**. The relief depth was chosen to produce approximately the required phase shift: around **0.685–0.700 µm** for operation near **635 nm**, and around **1.185–1.200 µm** for operation near **1.064 µm**.

The first tests were encouraging. Among plates with element sizes around **340, 500 and 680 µm**, the **500 µm** structure produced the most uniform distribution in the initial optical test. The same element was then taken into a more demanding experiment with a picosecond laser at **532 nm**.

That experiment exposed a limitation that was more interesting than a clean success. With the more coherent beam, interference fringes appeared in the homogenized field. Changing the random-element size changed the fringe structure, and the best result in that series was obtained with the **250 µm** element. In other words, the plate was doing what a phase element should do, but beam coherence became a dominant part of the final result.

The optical losses were relatively small: measured power changes through the phase-plate system were approximately **6.5–9.4%**, remaining below about **10%** in the tested cases. The structures were also tested directly in laser processing, where using the phase plate visibly changed and homogenized the processed spot [1].

At the time, making a fixed phase plate directly in fused silica was an attractive way to obtain passive beam shaping without a complicated active optical system. Today I would describe this branch more carefully. Programmable spatial light modulators can now reproduce many beam-shaping functions dynamically and can switch patterns without fabricating a new optic. That makes a simple fixed random plate less exciting for a flexible laboratory setup than it was a decade ago. But it does not make passive phase optics obsolete. Spatial light modulators still have power-handling and thermal limits, especially in high-power laser processing, while a fused-silica element is passive, compact and has no refresh electronics [7,8].

## Diffraction phase gratings: the branch that remained technologically attractive

The diffraction-grating experiments were more directly connected to controlled beam splitting. Here the goal was not a random redistribution of intensity but a periodic surface profile with predictable diffraction orders.

The thesis reports gratings with periods from about **55 to 400 µm** and relief depths from about **0.2 to 1.3 µm**. One grating studied in detail had a period of **100 µm**, a modified-width-to-period ratio of about **0.5**, and a relief depth near **0.5 µm**. Profilometry showed an approximately smooth periodic profile rather than a sharp binary trench. The roughness in the region most affected by the plasma reached roughly **0.02–0.03 µm**, while the central part of the written line remained close to the roughness of the original fused-silica surface.

The optical response was then measured in the focal plane of a lens and compared with calculation. The agreement was good enough to continue to an application test: the grating was used for simultaneous processing of a **20 nm titanium film**. Depending on the total patterned area, fabrication and cleaning of these diffraction elements took roughly **1–10 min** [5].

This branch continued after the thesis into multilevel phase plates for beam correction, where the same idea of controlling permanent surface relief was pushed toward more complex phase profiles [6].

This branch did not become historical in the same way that a simple fixed homogenizer partly did. Diffractive optical elements are still widely used for beam splitting, shaping, imaging and free-space optical systems [7]. What has changed is the design landscape: programmable modulators, metasurfaces and more advanced lithographic fabrication now offer many additional routes.

## Why fused silica is still interesting — and still difficult

One reason I think this old work remains worth documenting is the material itself. Fused silica is still a key optical material when low absorption, thermal stability, ultraviolet transparency and high laser-damage resistance matter. At the same time, it is a hard and brittle material, and high-quality structuring without subsurface damage, redeposition, cracks or residual stress remains difficult. A recent review of fused-silica optical manufacturing still describes high-accuracy, low-defect processing as a major engineering challenge, particularly for high-power laser optics [9].

So I would not present the thesis today as a competition with programmable beam shaping. The more interesting point is different: we showed that a very simple target-assisted nanosecond process could create **permanent, micrometre-scale optical relief directly in fused silica**, over centimetre-scale areas, within minutes rather than hours. Some of the individual optical concepts have since become easier to realize by other means, but efficient permanent structuring of fused silica is still a non-trivial fabrication problem.

## What I take from the thesis now

The thesis was not one perfect device. It was a progression of increasingly demanding questions.

We first found that fused silica had a useful processing window around **15 W** and **300 mm/s**. Then we showed that the relief could be tuned from roughly **0.2 to several micrometres**. We turned that control into microlenses, found that their **30–35 mm** focal lengths and low numerical apertures limited direct use, and changed the optical scheme. We fabricated random phase plates with **250–680 µm** features and learned that coherence could dominate the homogenization result. Finally, we made diffraction gratings with **55–400 µm** periods and used them for real multi-beam processing of a thin metal film.

For me, that is the real story of this stage of the project: not simply that several optical elements were fabricated, but that every optical test pushed the fabrication method toward the next question.

> [!NOTE]
> **Source:** this note is based on my Russian-language master’s thesis and the papers cited below. I am preparing a shorter English overview of the thesis; when that version is ready for public citation, I will link it here.

Next: [Note 03 — fused-silica phase gratings](03-phase-grating.md) · Previous: [Note 01 — porous-glass sealing and passivation](01-porous-glass-to-surface-structuring.md) · [Research map](../research-map.md)

## References

1. G. K. Kostyuk, M. M. Sergeev, **R. A. Zakoldaev**, E. B. Yakovlev, “Fast microstructuring of silica glasses surface by NIR laser radiation,” *Optics and Lasers in Engineering* 68 (2015), 16–24. https://doi.org/10.1016/j.optlaseng.2014.12.004
2. G. K. Kostyuk, **R. A. Zakoldaev**, M. M. Sergeev, V. P. Veiko, “Laser-induced glass surface structuring by LIBBH technology,” *Optical and Quantum Electronics* 48 (2016), 249. https://doi.org/10.1007/s11082-016-0531-0
3. G. K. Kostyuk, **R. A. Zakoldaev**, M. M. Sergeev, E. B. Yakovlev, “Microlens array fabrication on fused silica influenced by NIR laser,” *Applied Physics B* 122 (2016), 99. https://doi.org/10.1007/s00340-016-6379-y
4. **R. A. Zakoldaev**, G. K. Kostyuk, V. V. Koval, M. M. Sergeev, V. S. Rymkevich, E. B. Yakovlev, “Microlens array fabrication on fused silica by LIBBH technology with CO₂ laser smoothing,” *Journal of Instrument Engineering* 59 (2016), 400–406. https://doi.org/10.17586/0021-3454-2016-59-5-400-406
5. G. K. Kostyuk, **R. A. Zakoldaev**, V. V. Koval, M. M. Sergeev, V. S. Rymkevich, “Laser microplasma as a tool to fabricate phase grating applied for laser beam splitting,” *Optics and Lasers in Engineering* 92 (2017), 63–69. https://doi.org/10.1016/j.optlaseng.2016.12.013
6. **R. A. Zakoldaev**, G. K. Kostyuk, V. S. Rymkevich, V. V. Koval, M. M. Sergeev, V. P. Veiko, E. B. Yakovlev, A. N. Sivers, “Fast Fabrication of Multilevel Phase Plates Used for Laser Beam Correction,” *Journal of Laser Micro/Nanoengineering* 12 (2017), 281–285. https://doi.org/10.2961/jlmn.2017.03.0018
7. S. N. Khonina, N. L. Kazanskiy, M. A. Butt, “Exploring Diffractive Optical Elements and Their Potential in Free Space Optics and Imaging — A Comprehensive Review,” *Laser & Photonics Reviews* 18 (2024), 2400377. https://doi.org/10.1002/lpor.202400377
8. Y. Tang et al., “Extending the operational limit of a cooled spatial light modulator exposed to 200 W average power for holographic picosecond laser materials processing,” *Optics & Laser Technology* 181 (2025), 111589. https://doi.org/10.1016/j.optlastec.2024.111589
9. J. Cheng et al., “Challenges of optical manufacturing techniques applied in improving the laser damage resistance of hard-brittle fused silica optics,” *Optics & Laser Technology* 192 (2025), 113475. https://doi.org/10.1016/j.optlastec.2025.113475
