---
title: Coordinate systems
type: ggplot2
tags: [ggplot2, coord, reference]
sources: [discrete-continuous.Rmd, time-series.Rmd, continuous-continuous.Rmd, distributions.Rmd]
updated: 2026-09-30
---

Every plot has a coordinate system; the default is `coord_cartesian()`, called implicitly. Usually you don't think about it, but sometimes you change it.

| Function | What it does | When (per the book) |
|---|---|---|
| `coord_cartesian(xlim, ylim)` | zoom the visible window | **Zooming**: use this, *not* `filter()` — filtering changes what's plotted (the star stops looking like a star) |
| `coord_fixed(ratio = 1)` | fixes the aspect ratio; default ratio 1 = square units | equal-unit axes (paired life expectancies, the star); experimenting with slope visibility ([Aspect ratio](../concepts/aspect-ratio-and-banking.md)); also accepts `xlim`/`ylim` |
| `coord_flip()` | swaps x and y | long category labels on bar/dot plots (discrete-continuous) |

**`coord_flip()` isn't always best:** for boxplots, flipping makes median lines and box edges harder to compare (vertical segments are harder than horizontal), so the book keeps boxplots vertical and angles labels with `theme()` instead ([Theme](theme.md), [Summary vs detail](../concepts/summary-vs-detail.md)).

Why `coord_fixed()` for the star: `coord_cartesian()` fills the available space (wider than tall), so equal numeric distances look unequal and the star is distorted.

Note: `coord_*()` comes after scales and before facets in the recommended ordering ([Plot template](plot-template.md)). Cheat-sheet section: "Coordinate systems".

## Sources

`discrete-continuous.Rmd` — "Coordinate systems"; `distributions.Rmd` — boxplot discussion; `time-series.Rmd`; `continuous-continuous.Rmd`. Summary: [Discrete-continuous](../sources/discrete-continuous.md).
