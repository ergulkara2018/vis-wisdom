---
title: "Guide: distributions"
type: guide
tags: [guide, distributions, histogram, boxplot]
sources: [distributions.Rmd]
updated: 2026-09-30
---

Use when you want to see **how the values of a continuous variable are spread** — for everyone, or compared across groups. A common first EDA step.

## One distribution

- **Histogram** by default; choose `binwidth` deliberately ([Bin width](../concepts/bin-width.md)).
- Add a **median reference line** ([Mean vs median](../concepts/mean-vs-median.md), [Layering](../concepts/layering-and-reference-lines.md)).
- `geom_freqpoly()` if you'll later overlay groups; `geom_density()` only with plenty of data or simulated data.

## Several distributions

| # groups | Recommended | Avoid |
|---|---|---|
| 2–3 | overlaid `geom_freqpoly()` colored by group (use `y = ..density..` when sizes differ); or vertical facets (`facet_grid(rows = ...)`); filled `geom_density(alpha)` if enough data | stacked histograms; side-by-side (column) facets |
| many (e.g. 9 census divisions) | `geom_boxplot()` (summary) or `geom_violin()` (shape, needs enough data), ordered by median, with a median reference line under the boxes, angled x labels | colored freqpolys (too many colors) |

Boxplots/violins don't show group sizes. See [Summary vs detail](../concepts/summary-vs-detail.md), [Stacking problem](../concepts/stacking-problem.md), [Faceting strategy](../concepts/faceting-strategy.md).

## Worked example: ages in the 2019 Congress

Mean ≈ median ≈ 58–59; House slightly younger than Senate and more evenly distributed; Democrats more spread out and slightly older than Republicans; "Other" members older than either; divisions have similar medians but different shapes. See [Congress 2019](../datasets/congress-2019.md).

## Mechanics used

`theme(axis.text.x = element_text(angle = -45, hjust = 0))` ([Theme](../ggplot2/theme.md)); layering order; `stamp()`.

## Related

[Choosing a plot](choosing-a-plot.md) · [Geoms](../ggplot2/geoms.md)

## Sources

`distributions.Rmd`. Summary: [Distributions](../sources/distributions.md).
