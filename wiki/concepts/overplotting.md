---
title: Overplotting
type: concept
tags: [scatterplots, transparency, binning]
sources: [continuous-continuous.Rmd, time-series.Rmd]
updated: 2026-09-30
---

Overplotting: so many points overlap that you can't tell how many lie in an area. The book's remedies, roughly in order of how much data you have:

| Situation | Remedy | Note |
|---|---|---|
| Lots of data (Gapminder, 2500 rows) | **Bin** with `geom_hex()` (preferred) or `geom_bin2d()`; encode count with fill; add `scale_fill_viridis_c()` for contrast | hex gives finer resolution of the distribution's shape; adjust `bins`/`binwidth` |
| Moderate data | **Transparency**: `geom_point(alpha = 0.5)` | generally better than `shape = 21`; works even with heavy overlap |
| Few points, mild overlap | `shape = 21` (border + fill), e.g. black fill with white border | emphasizes individual values |
| Exact duplicates (mpg `displ` × `hwy`) | `geom_count()` — size encodes count at each location | |
| Different-sized points hiding each other | `arrange(desc(size_var))` so big points draw first; `shape = 21` | `geom_point()` draws in row order |

Binning is *not* always right: with only 2010 and 2015 (183 countries × 2 years) most hexagons held a single point, so `geom_hex()` was no better than points.

Also related: a linear scale can cause a form of overplotting by squashing many points at one edge — use a [log scale](log-scales.md). With too many groups of points, show only a [smooth](smoothing.md) per group.

## Related

[Color scales](color-scales.md) · [Geoms](../ggplot2/geoms.md) · [Continuous-continuous guide](../guides/continuous-continuous-relationships.md)

## Sources

`continuous-continuous.Rmd` — "Overplotting", "Three continuous variables"; `time-series.Rmd` — famine bubbles. Summary: [Continuous-continuous](../sources/continuous-continuous.md).
