---
title: Encoding and decoding
type: concept
tags: [perception, cleveland, theory]
sources: [general-strategy.Rmd, references.bib]
updated: 2026-09-30
---

Data is not visual by default. **Encoding** maps data values onto visual elements (position, length, color, size…); **decoding** is the viewer's act of reading those elements back into data. The book (following [William Cleveland](../people/william-cleveland.md), 1985) holds that *a plot succeeds only if decoding goes well* — a visually stunning plot that nobody can decode has failed.

## In practice

- In ggplot2 terms, the aesthetic mappings, geoms, scales and coordinates are your encoding choices ([Grammar of graphics](grammar-of-graphics.md)). Example: `buildings_10` could be drawn as pictures, as bars (`geom_col`, length), or as dots (`geom_point` + `coord_flip`, position).
- Decoding is a sequence of perceptual steps. To learn "Burj Khalifa is tallest" from the dot plot you must notice the rightmost dot, then connect it to its label.
- For a presentation plot, decoding should lose as little as possible; the audience should leave with the understanding you started with.
- Decoding can fail in ways the author doesn't notice: see "look at your plots" in [Visualization strategies](visualization-strategies.md).
- Worked failures: bars in alphabetical order (hard to compare unordered amounts; see [Ordering categories](ordering-categories.md)); color or size for height (see [Perceptual ranking](perceptual-ranking.md)); overlapping x labels (see [Coordinate systems](../ggplot2/coordinate-systems.md)); bars vs points for the 100 m final ([Compared to what?](compared-to-what.md)).

The human visual system does the decoding, so which encodings work is an empirical question — see [Perceptual ranking](perceptual-ranking.md).

## Related

[EDA vs presentation](eda-vs-presentation-plots.md) · [Derived variables](derived-variables.md)

## Sources

`general-strategy.Rmd` — "Encoding and decoding". Cleveland & McGill (1985) via `references.bib` (not in `raw/`). Summary: [General strategy](../sources/general-strategy.md).
