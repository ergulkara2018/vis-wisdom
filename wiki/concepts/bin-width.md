---
title: Bin width
type: concept
tags: [histograms, parameters, distributions]
sources: [distributions.Rmd, continuous-continuous.Rmd]
updated: 2026-09-30
---

Histograms, frequency polygons, `geom_bin2d()` and `geom_hex()` all need a bin size: `bins` (number of bins, default 30) or `binwidth` (width in data units). `geom_histogram()` prints a message if you use the default — a reminder that you should *always* think about the binwidth and will rarely want the default.

## Congress ages example

| Binwidth | Verdict |
|---|---|
| 0.1 yr | "Bad": overall shape is hard to see, plot looks "peaky", many bars represent one person |
| 20 yr | "Bad": too coarse to be meaningful, loses information |
| ≈ 2 yr (default 30 bins) | "not too far off" |
| **5 yr** | chosen: minor adjustment so each bin is 5 years |

Too small → noise; too large → lost structure. Try several ([Visualization strategies](visualization-strategies.md): go for quantity).

For 2-D binning the default bin count "does a good job" for Gapminder ([Overplotting](overplotting.md)). The same choice applies to frequency polygons; the multi-division example used `binwidth = 8`.

## Related

[Summary vs detail](summary-vs-detail.md) · [Geoms](../ggplot2/geoms.md) · [Bad-to-good catalog](../analyses/bad-to-good-catalog.md)

## Sources

`distributions.Rmd` — "One distribution"; `continuous-continuous.Rmd` — "Overplotting". Summary: [Distributions](../sources/distributions.md).
