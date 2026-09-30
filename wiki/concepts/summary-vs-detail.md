---
title: Summary vs detail in distribution plots
type: concept
tags: [boxplot, violin, histogram, density, tradeoffs]
sources: [distributions.Rmd]
updated: 2026-09-30
---

Every plot of a distribution trades detail for clarity. The book's ladder, from most detail to most summary:

| Geom | Shows | Loses / needs | Book's advice |
|---|---|---|---|
| `geom_histogram()` | counts per bin; overall shape | you must choose `binwidth` ([Bin width](bin-width.md)) | generally a good bet for one simple distribution |
| `geom_freqpoly()` | same as histogram, as lines | same | better than histogram for *overlaying* 2–3 groups |
| `geom_density()` | smoothed shape | fine detail; misleading with little data | use in specific scenarios: simulated data, plenty of data, filled curves with `alpha` |
| `geom_violin()` | mirrored density per group | median unless `draw_quantiles`; needs enough data; not the amount of data | good when you care about shape across many groups |
| `geom_boxplot()` | median, middle 50%, whiskers (excluding outliers), outliers | distribution shape | good for many groups; a summary |

## Key points

- Summaries highlight important features but "don't provide a full picture" — sometimes the trade-off is worth it, sometimes not.
- **Switch to summaries when groups multiply:** with nine census divisions, colored freqpolys were unusable; boxplots revealed the differences. Boxplot box positions relative to medians hinted at different shapes; violins confirmed it.
- **Neither boxplots nor violins show sample size** — you can't tell New England has fewer members than the Pacific. "There are positives and negatives to every visualization decision."
- **Orientation:** keep boxplots vertical and angle the labels (`theme(axis.text.x = element_text(angle = -45, hjust = 0))`) rather than `coord_flip()`, because vertical median/box-edge segments are harder to compare than horizontal ones ([Coordinate systems](../ggplot2/coordinate-systems.md)).
- `geom_violin(draw_quantiles = 0.5)` computes quantiles differently from `geom_boxplot()`/`median()`, so lines may not line up exactly.

## Related

[Distributions guide](../guides/distributions.md) · [Mean vs median](mean-vs-median.md) · [Stacking problem](stacking-problem.md) · [Smoothing](smoothing.md)

## Sources

`distributions.Rmd` — "One distribution", "Multiple distributions". Summary: [Distributions](../sources/distributions.md).
