---
title: "Guide: continuous-continuous relationships"
type: guide
tags: [guide, scatterplots, overplotting, smoothing]
sources: [continuous-continuous.Rmd, general-strategy.Rmd]
updated: 2026-09-30
---

Use when you want to see **how two or three continuous variables are associated**. Questions to ask first: is there a relationship, how strong, which direction, linear or levelling off?

## Two continuous variables

1. Start with a **scatterplot** (`geom_point`).
2. If values span orders of magnitude, use a **log scale** ([Log scales](../concepts/log-scales.md)).
3. If points pile up, fix [overplotting](../concepts/overplotting.md): `geom_hex()` (+ viridis) for lots of data, `alpha` for moderate data, `shape = 21` for few, `geom_count()` for exact duplicates.
4. Add a **`geom_smooth(method = "loess")`** if the trend isn't obvious ([Smoothing](../concepts/smoothing.md)); show smooths only when comparing trends or when there's too much data; order/position the legend or label lines directly ([Direct labeling](../concepts/direct-labeling-and-legends.md)).
5. **Same measure at two times?** Use the [paired data](../concepts/paired-data.md) recipes (`coord_fixed()` + `y = x` line; difference plot; segments).

## Three continuous variables

Apply the [perceptual ranking](../concepts/perceptual-ranking.md): two most important → x and y position; discrete category → color; third continuous → **size** (area). Then:

- widen `scale_size(range = c(0.5, 20))`, set legend `breaks`;
- `shape = 21` with `fill` for overlap; `arrange(desc(size_var))` so big points don't cover small ones;
- know the limit: readers can't judge the relationship between the size variable and the axes; create explicit [derived variables](../concepts/derived-variables.md) if that matters.

Based on the Gapminder bubble charts and Hans Rosling's demonstration ([Gapminder](../datasets/gapminder.md)).

## Related

[Choosing a plot](choosing-a-plot.md) · [Scales](../ggplot2/scales.md) · [Color scales](../concepts/color-scales.md) · [Time-series guide](time-series.md) (adds time)

## Sources

`continuous-continuous.Rmd`. Summary: [Continuous-continuous](../sources/continuous-continuous.md).
