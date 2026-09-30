---
title: Aspect ratio and banking to 45°
type: concept
tags: [time-series, slope, cleveland, aspect-ratio]
sources: [time-series.Rmd, discrete-continuous.Rmd, continuous-continuous.Rmd, references.bib]
updated: 2026-09-30
---

In a line plot you judge each segment's *slope* against the x-axis, and the aspect ratio of the plot changes every angle. Taller plots make slopes steeper; wider plots flatten them.

## The "bank to 45" heuristic

- Cleveland, McGill & McGill (1988): the aspect ratio that makes the **average slope of all segments 45°** makes different slopes easiest to discriminate.
- Talbot et al. (2012): the book reports that a second group of researchers **failed to replicate** the 1988 result, so it is "not clear that the bank to 45 rule is really a rule".
- The default ggplot2 aspect ratio comes fairly close to it for the South Africa plot.
- **Practical advice:** don't compute angles; experiment with the aspect ratio, notice which features become visible, and choose the ratio that highlights what you think is most important. (`coord_fixed(ratio)` controls it; `fig.asp`/`fig.width` in knitr chunks also do.)

## Examples

- South Africa life expectancy: the faster rise 1980–1990 than 1950–1980 is easier to see in the tall plot and harder in the wide plot (slopes look more alike when flattened).
- Wheat prices: a *wide* ratio highlights the cyclical trend; a *tall* ratio highlights the long-term downward trend; the book picks a slightly-taller-than-default ratio to stress the decline from the early 1900s. See [Time-series guide](../guides/time-series.md).

## Related uses of `coord_fixed()`

- Equal units on both axes (the star; paired life expectancies) — set ratio 1 so distances aren't distorted. See [Coordinate systems](../ggplot2/coordinate-systems.md), [Paired data](paired-data.md).

## Related

[Perceptual ranking](perceptual-ranking.md) (slope is ranked 5th) · [William Cleveland](../people/william-cleveland.md) · [Talbot, Gerth & Hanrahan](../people/talbot-gerth-hanrahan.md)

## Sources

`time-series.Rmd` — "Banking to 45", "Multiple trend-types". Summary: [Time series](../sources/time-series.md).
