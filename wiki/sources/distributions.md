---
title: "Source: Distributions (distributions.Rmd)"
type: source
tags: [distributions, histogram, boxplot, density, theme]
sources: [distributions.Rmd]
updated: 2026-09-30
---

How to visualize one or several distributions of a continuous variable, using the ages of the 2019 US Congress. Mechanics first (layering, `theme()`), then one distribution, then many.

## Structure and claims

- **Motivation:** examining distributions is a common first EDA step; the chapter frames three hypotheses about Congress ages to show what distributions can reveal.
- **Mechanics — layering:** geoms are drawn in the order added, so put reference lines (`geom_hline`/`geom_vline`/`geom_abline`) *under* the data geoms; layers may use different data. → [Layering and reference lines](../concepts/layering-and-reference-lines.md)
- **Mechanics — `theme()`:** element functions (`element_text()`, `element_line()`); angle x labels with `axis.text.x = element_text(angle = -45, hjust = 0)`. → [Theme](../ggplot2/theme.md)
- **One distribution:** mean vs median (medians preferred because robust to outliers); summary statistics; histograms need a deliberate `binwidth` (0.1 and 20 years are both "Bad"; 5 years works); `geom_freqpoly()` = "histograms with lines"; `geom_density()` = smoothed histogram, recommended only in specific scenarios (e.g. simulated data, lots of data). → [Mean vs median](../concepts/mean-vs-median.md) · [Bin width](../concepts/bin-width.md)
- **Multiple distributions:** stacked histograms are bad; side-by-side (column) facets are hard to compare, vertical facets are better; overlaid frequency polygons are best for 2–3 groups; use `y = ..density..` when group sizes differ (House vs Senate); filled densities need `alpha` and enough data; with many groups (9 census divisions) switch to boxplots. → [Stacking problem](../concepts/stacking-problem.md) · [Faceting strategy](../concepts/faceting-strategy.md)
- **Boxplots vs violins:** boxplots summarize (50% box, whiskers excluding outliers, median) and lose shape; violins show shape but need sufficient data; neither shows the amount of data behind each group. `coord_flip()` makes median lines/box edges harder to compare (vertical segments are harder than horizontal), so angle labels instead. → [Summary vs detail](../concepts/summary-vs-detail.md)
- Uses the `stamp("Bad")` red tag (defined in `_common.R`) to label poor plots.

## Data

[Congress 2019](../datasets/congress-2019.md); [built-in R data sets](../datasets/builtin-r-datasets.md) (`mpg`); simulated normals.

## Related

[Distributions guide](../guides/distributions.md) · [Geoms](../ggplot2/geoms.md) · [Bad-to-good catalog](../analyses/bad-to-good-catalog.md)

## Sources

`distributions.Rmd` — all sections.
