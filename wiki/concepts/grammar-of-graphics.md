---
title: Grammar of graphics (as used in this book)
type: concept
tags: [ggplot2, theory, wickham]
sources: [ggplot2-basics.Rmd, references.bib]
updated: 2026-09-30
---

The book explains ggplot2 through the **grammar of graphics**, citing [Wickham (2010)](../people/hadley-wickham.md): like a sentence is built by choosing a determiner, noun and verb ("The cat slept."), *any* plot is built by choosing values for a fixed set of plot elements.

## The eight elements

Specified by you most of the time:

1. Data
2. Geom(s)
3. Aesthetic mappings
4. Faceting scheme

Working "in the background" (defaults unless you change them):

5. Statistical transformation
6. Position adjustment
7. Coordinate system
8. Scales

**Not technically part of the grammar:** theme and labels (`theme()`, `labs()`).

A plot can specify only three (data, geom, mapping); `ggplot()` supplies defaults for the rest — e.g. `coord_cartesian()` is implicit ([Coordinate systems](../ggplot2/coordinate-systems.md)).

## Why it matters for wisdom

The elements are the *encoding choices* of a visualization ([Encoding and decoding](encoding-and-decoding.md)): aesthetics and geoms choose the visual channel, scales map data to it, coords and facets arrange it. Where each element is introduced in the book: stat/position in `geom_bar`/`position = "dodge"` ([Geoms](../ggplot2/geoms.md)), coordinates ([Coordinate systems](../ggplot2/coordinate-systems.md)), scales ([Scales](../ggplot2/scales.md)), theme ([Theme](../ggplot2/theme.md)), labels ([Annotations and labels](../ggplot2/annotations-and-labels.md)).

Recommended code order follows the elements: see [Plot template](../ggplot2/plot-template.md).

## Sources

`ggplot2-basics.Rmd` — "The grammar of graphics". Summary: [ggplot2 basics](../sources/ggplot2-basics.md).
