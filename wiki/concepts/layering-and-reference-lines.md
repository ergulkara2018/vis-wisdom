---
title: Layering and reference lines
type: concept
tags: [layers, reference-lines, annotations]
sources: [distributions.Rmd, continuous-continuous.Rmd, time-series.Rmd]
updated: 2026-09-30
---

**Layers** are drawn in the order you add them; later layers sit on top. Layers may use different data (e.g. a small `tribble` of CAFE standards for `geom_hline()` alongside `mpg` for boxplots).

**Rule (book):** put reference lines *under* the data — a line on top of boxplots can obscure information.

## Reference lines the book uses

| Line | Geom | What it adds |
|---|---|---|
| Overall median across groups | `geom_hline(aes(yintercept = median(x)))` / `geom_vline` | compare each group/histogram to the whole ([Distributions guide](../guides/distributions.md)) |
| `y = x` | `geom_abline(slope = 1, intercept = 0)` | "no change" baseline in paired data; above = increased, below = decreased ([Paired data](paired-data.md)) |
| Event date | `geom_vline(xintercept = 1994)` | checks a hypothesis (end of apartheid) ([Time-series guide](../guides/time-series.md)) |
| External standard | `geom_hline(data = cafe_2008, aes(yintercept = mpg, color = class))` | bring in a benchmark from another dataset |

Reference lines operationalize [Compared to what?](compared-to-what.md).

Related ordering issue: `geom_point()` draws points in row order, so large bubbles can hide small ones — `arrange(desc(size))` first ([Overplotting](overplotting.md)).

## Related

[Geoms](../ggplot2/geoms.md) · [Annotations and labels](../ggplot2/annotations-and-labels.md) · [Mean vs median](mean-vs-median.md)

## Sources

`distributions.Rmd` — "Layering"; `continuous-continuous.Rmd` — "Paired data"; `time-series.Rmd` — "Trends". Summary: [Distributions](../sources/distributions.md).
