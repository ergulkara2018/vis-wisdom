---
title: "Source: Continuous-continuous relationships (continuous-continuous.Rmd)"
type: source
tags: [scatterplots, overplotting, scales, smoothing, paired-data]
sources: [continuous-continuous.Rmd, references.bib]
updated: 2026-09-30
---

How to visualize associations between continuous variables, built around Gapminder life expectancy vs GDP per capita. The longest chapter: mechanics (annotations, log scales, color scales, size scales), two-variable plots (overplotting, smoothing, paired data), and three-variable plots.

## Structure and claims

- **Questions to ask:** is there a relationship, how strong, which direction, is it linear or does the benefit level off?
- **Mechanics:** annotations (R4DS link) → [Annotations and labels](../ggplot2/annotations-and-labels.md); **log scales** for data spanning orders of magnitude and for power laws (a straight line on log–log axes; word rank vs frequency in *War and Peace*) → [Log scales](../concepts/log-scales.md); **color scales** — sequential (`scale_*_gradient`, viridis for colorblind-friendly), diverging (`scale_*_gradient2`, sign + magnitude, `midpoint`) → [Color scales](../concepts/color-scales.md); **size scales** — `scale_size()` scales *area*, tune `breaks` and `range`. → [Scales](../ggplot2/scales.md)
- **Overplotting:** bin (`geom_bin2d`, `geom_hex` — prefer hex), transparency (`alpha`, generally better than `shape = 21` except for few points), `shape = 21` with white borders for small data, `geom_count()` for exact overlaps. → [Overplotting](../concepts/overplotting.md)
- **Smoothing:** `geom_smooth()` defaults to `gam` for >1000 points and `loess` for fewer; prefer `loess` unless data is very large; confidence band width = uncertainty; show only smooths when trends matter more than points, when comparing trends, or when there is too much data. Legend order should match line order (Wilke); move the legend (`legend.justification = "top"`). → [Smoothing](../concepts/smoothing.md) · [Direct labeling and legends](../concepts/direct-labeling-and-legends.md)
- **Paired data** (same measure at two points): scatter with `coord_fixed()` and a `y = x` reference line; label outliers with `ggrepel`; encode region with color; or compute the difference (→ discrete-continuous); or plot both values on one axis joined by `geom_segment()`. Different plots highlight different aspects. → [Paired data](../concepts/paired-data.md) · [Derived variables](../concepts/derived-variables.md)
- **Three continuous variables:** apply the [perceptual ranking](../concepts/perceptual-ranking.md) — two important variables to position, region to color, population to size; enlarge `range`, use `shape = 21` + `fill`, `arrange(desc(population))` so small points aren't hidden, custom `breaks = 10^(6:9)`. Caveat (Wilke): size makes the relationship between axis variables and the size variable hard to judge; create explicit relationship variables if that matters. Based on Gapminder bubbles and Hans Rosling's demonstration.

## Data

[Gapminder](../datasets/gapminder.md), [War and Peace word frequencies](../datasets/word-frequencies.md), [built-in R data sets](../datasets/builtin-r-datasets.md) (`diamonds`, `mpg`).

## Related

[Continuous-continuous guide](../guides/continuous-continuous-relationships.md) · [Time series source](time-series.md) · [Claus Wilke](../people/claus-wilke.md)

## Sources

`continuous-continuous.Rmd` — all sections; cites Cleveland & McGill (1985) and Wilke (2019).
