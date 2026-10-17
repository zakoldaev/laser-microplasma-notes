# From controllable fused-silica relief to functional micro-optics

> **Summary:** This note follows the thesis-stage experiments on fused silica: finding a workable nanosecond-laser processing window, controlling relief from sub-micrometre to several-micrometre depth, and turning that control into microlenses, random phase plates and diffraction phase gratings that were tested optically.

This note starts where the porous-glass work ends. By the time I was writing my master’s thesis, the main question was no longer whether the glass–graphite interaction could modify a transparent material, but whether the same approach could produce controlled relief and functional micro-optical elements on fused silica.

> Can a relatively simple nanosecond-laser setup create controlled surface relief in fused silica and turn that relief into working optical elements?

The experiments therefore progressed from identifying a usable processing window, to controlling relief depth, and then to fabricating and testing microlenses, random phase plates and diffraction phase gratings [1–5].

## Finding a usable window on fused silica

A polished fused-silica plate was placed in contact with pressed graphite. A ytterbium-fiber laser at about **1.064 µm** passed through the transparent glass and was focused at the glass–graphite interface. In the thesis experiments the pulse duration was varied from **50 to 200 ns**, with repetition rates between **20 and 100 kHz**. The beam was moved with a two-axis scanning system, and the focusing optics had a focal length of about **210 mm** [1,2].

The process window depended strongly on the glass composition. For fused silica, smooth structures without obvious cracks or chips were obtained around **15 W average power** and a scan speed of about **300 mm/s**. Similar conditions on other glasses such as BK7 or US-1 often produced cracking or local destruction. This showed that the useful regime could not be defined only by laser parameters; the thermal and mechanical properties of the glass also had to be considered [2].

Once a stable regime for fused silica was found, the next parameter was relief depth. In the thesis I varied average power, pulse duration (**50, 100 and 200 ns**) and the number of passes (**one or three**). Across the investigated conditions, the formed relief ranged from roughly **0.2 to 5 µm**, and the depth changed approximately linearly with laser power over the tested ranges [2].

At this stage the process was no longer only a surface-modification experiment. The available depth range was sufficient to begin using the relief for optical phase control.

For larger patterns, fabrication was also relatively fast. A structured area of about **10 × 10 mm²** could typically be produced in roughly **5–15 min**, depending on the size and spacing of the elements. Graphite deposited during processing, so wet laser cleaning with distilled water became part of the fabrication sequence [1].

## Microlenses and the limits of the first design

Microlens arrays were used as the first test of whether the fabricated relief could perform a simple optical function.

In the thesis, arrays were fabricated with lens diameters from about **50 to 500 µm** and periods from **10 to 1000 µm**. Profilometry showed typical lens heights of roughly **1–2 µm**. The written profiles were not ideal spherical caps; the central region tended to be comparatively flat [3].

For detailed optical testing, arrays with lens diameters of **150, 200 and 400 µm** were studied. Their measured focal lengths were about **30–35 mm**, with numerical apertures of **0.0025–0.0057**. The smallest measured focal spot was approximately **90 ± 10 µm**, larger than the simple theoretical estimate [3].

These parameters were insufficient for direct parallel laser micromachining with the microlenses alone. The optical scheme was therefore modified by adding a microscope objective after the array. With this configuration, the spot size in the processing plane was reduced substantially, and arrays of holes of about **10 µm** were produced in a **60 nm titanium film**.

The lens profile also indicated that an additional smoothing step could be useful. In the thesis I tested chemical smoothing in hydrofluoric acid for about **15–30 min**, which rounded the initially flat-topped profile. A later study explored carbon-dioxide-laser smoothing as another route to improve the lens shape [4].

The microlens experiments therefore identified both the optical function and the main limitation of the initial surface profile, which directly motivated the next processing and optical modifications.

## Random phase plates and beam homogenization

The random phase plates used in these experiments were binary phase elements designed to redistribute an inhomogeneous laser beam. Instead of blocking part of the beam, each plate divided its aperture into many small elements with two optical phase levels. In the simplest design, approximately half of the elements introduced no additional phase shift and the other half introduced a phase shift of **π radians**. After a collective lens, the elementary beams overlapped in the focal plane and their diffraction patterns interfered, redistributing energy away from the original central peak [10,11].

For a plate made by forming relief in a transparent material, a π phase shift is obtained when the optical path difference between the two levels is half a wavelength. The required relief depth can therefore be estimated as:

`hπ = λ / [2(n − 1)]`

where `λ` is the operating wavelength and `n` is the refractive index of the phase-plate material. This relation was used in the thesis to select the target depth of the fused-silica structures.

The lateral size of each random element also determines the optical response. For an element size `d_e`, a collective lens with focal length `f`, and wavelength `λ`, the approximate width of the diffraction envelope produced by one element is:

`d_p ≈ 2fλ / d_e`

The characteristic speckle size in the focal plane depends mainly on the illuminated beam diameter `D`:

`d_speckle ≈ 2fλ / D`

The number of elementary contributions overlapping in the focal plane can be estimated from the number of phase elements illuminated by the beam. For beam dimensions `D_x` and `D_y`, and phase-element dimensions `d_x` and `d_y`:

`N ≈ (D_x D_y) / (d_x d_y)`

For square elements and an approximately circular or square illuminated area, this gives the useful scaling `N ~ (D / d_e)²`. Smaller phase elements therefore increase the number of elementary beams contributing to the final distribution, although the final homogenization also depends strongly on the spatial coherence of the source [10,11].

The fabricated fused-silica plates used random square elements with lateral sizes between **250 and 680 µm**. The measured relief depths were about **0.685–0.700 µm** for operation near **635 nm**, and about **1.185–1.200 µm** for operation near **1.064 µm**. These values followed the π-phase-depth calculation above.

In the first optical tests, the beam was expanded to about **10 mm** and focused with a collective lens having a focal length of **190 mm**. For an element size of **500 µm**, the thesis estimated approximately **256 elementary beams** contributing in the focal plane. Among plates with element sizes of about **340, 500 and 680 µm**, the **500 µm** structure produced the most uniform distribution in that initial test.

The same approach was then tested with a more coherent picosecond laser at **532 nm**. In this case, interference fringes became pronounced and the optimum element size shifted; the best result in that series was obtained with the **250 µm** plate. The comparison showed that geometric parameters alone are not sufficient to predict performance: the coherence of the input beam strongly affects the final intensity distribution.

The measured optical loss through the phase-plate system was approximately **6.5–9.4%**, remaining below about **10%** in the tested cases. The structures were also tested directly in laser processing, where the phase plate changed the intensity distribution in the processed spot [1].

Programmable spatial light modulators now provide much greater flexibility for laboratory beam shaping, while fixed fused-silica phase plates remain relevant where a passive element, permanent alignment or higher optical power handling is required [7,8].

## Diffraction phase gratings and controlled beam splitting

The diffraction-grating experiments were aimed at a more deterministic function: periodic surface relief with predictable diffraction orders.

The thesis reports gratings with periods from about **55 to 400 µm** and relief depths from about **0.2 to 1.3 µm**. One grating studied in detail had a period of **100 µm**, a modified-width-to-period ratio of about **0.5**, and a relief depth near **0.5 µm**. Profilometry showed an approximately smooth periodic profile rather than a sharp binary trench. The roughness in the region most affected by the plasma reached roughly **0.02–0.03 µm**, while the central part of the written line remained close to the roughness of the original fused-silica surface.

The optical response was measured in the focal plane of a lens and compared with calculation. The agreement was sufficient to proceed to an application test, where the grating was used for simultaneous processing of a **20 nm titanium film**. Depending on the total patterned area, fabrication and cleaning of these diffraction elements took roughly **1–10 min** [5].

This branch continued after the thesis into multilevel phase plates for beam correction, where the same principle of controlled permanent surface relief was extended to more complex phase profiles [6].

Diffractive optical elements remain widely used for beam splitting, shaping and imaging, although the available fabrication routes now also include programmable modulators, metasurfaces and advanced lithography [7].

## Current relevance of the fabrication result

The main result to carry forward is the demonstrated ability to produce **permanent, micrometre-scale optical relief directly in fused silica** over centimetre-scale areas within minutes. Fused silica remains important for low-absorption, ultraviolet and high-power optics, while high-accuracy structuring without cracks, redeposition, subsurface damage or residual stress remains technically demanding [9].

## Summary of the thesis-stage progression

The work established a useful fused-silica processing window around **15 W** and **300 mm/s** and showed relief control from roughly **0.2 to several micrometres**. That control was then used to fabricate microlenses, random phase plates and diffraction gratings. Optical testing identified the limitations of the first microlens profiles, showed the influence of beam coherence on random phase plates, and demonstrated multi-beam processing with diffraction gratings having periods between **55 and 400 µm**.

The progression from process-window studies to optical testing was important because each stage provided the parameters and limitations needed for the next one.

> [!NOTE]
> **Source:** this note is based on my Russian-language master’s thesis and the papers cited below. I am preparing a shorter English overview of the thesis; when that version is ready for public citation, I will link it here.

Previous: [Note 01 — porous-glass sealing and passivation](01-porous-glass-to-surface-structuring.md) · [Publication trail](04-publication-trail.md) · [Research map](../research-map.md)

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
10. C. L. S. Lewis, I. Weaver, L. A. Doyle, G. W. Martin, T. Morrow, D. A. Pepler, C. N. Danson, I. N. Ross, “Use of a random phase plate as a KrF laser beam homogenizer for thin film deposition applications,” *Review of Scientific Instruments* 70 (1999), 2116.
11. C. Kopp, L. Ravel, P. Meyrueis, “Efficient beamshaper homogenizer design combining diffractive optical elements, microlens array and random phase plate,” *Journal of Optics A: Pure and Applied Optics* 1 (1999), 398.
