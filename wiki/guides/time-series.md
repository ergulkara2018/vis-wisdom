---
title: "Guide: time series"
type: guide
tags: [guide, time-series, trends, aspect-ratio]
sources: [time-series.Rmd]
updated: 2026-09-30
---

Use when one variable is **time**. First decide *what the viewer should notice* — the book organizes advice by that: long-term trend, short-term fluctuations, cyclical pattern, or individual values.

## By goal

| You care about | Use | Notes |
|---|---|---|
| **Long-term trend** | `geom_line()` (+ `geom_point()` if data are sparse/irregular or outliers are unclear) | fewer points needed as data gets dense; choose aspect ratio ([Aspect ratio](../concepts/aspect-ratio-and-banking.md)); reference line for an event |
| **Multiple trend types** (cycle + decline) | pick the important one and set aspect ratio to show it; `loess` shows only the long-term trend | wheat prices: wide → cycles, tall → decline |
| **Many series** | alpha-faded `geom_line(aes(group = name))` + smooth; or group by region with smooths; boxplots per time bin for distribution over time | see [Distributions](distributions.md) |
| **A few series** | color + `geom_line()`; label lines directly, `guides(color = "none")` | [Direct labeling](../concepts/direct-labeling-and-legends.md) |
| **Two response variables** | `geom_path()` of y1 vs y2 in data order (`arrange(year)`) | arrows for EDA; year labels at inflection points for presentation ([EDA vs presentation](../concepts/eda-vs-presentation-plots.md)) |
| **Short-term fluctuations, discrete time units** | `geom_col()` or `geom_segment()` (vertical segments from 0) | shows gaps (no night flights), groups days, allows color (weekend) |
| **Individual events** (no trend) | scatter/bubble by start date, or `geom_segment()` spans for duration; label with `ggrepel` | famines: size = deaths, fill = region |

## Testing a hypothesis by comparison

Life expectancy in South Africa fell around 1994 (end of apartheid). Adding neighbors (Botswana, Swaziland, Lesotho) showed the same early-1990s decline there, suggesting the dip was not due to apartheid's end; looking at Africa by sub-region tied it (per the book) to the HIV/AIDS pandemic in southern Africa; the big 1994 Rwanda drop is the genocide; the downward spike in 1918 in South Africa's series shows the effects of the 1918 influenza pandemic. The method — make a hypothesis visible with a reference line, then compare to other series — applies [Compared to what?](../concepts/compared-to-what.md).

## Mechanics

`scale_*_date()/_datetime()/_time()` with `date_breaks` and `date_labels` ([Scales](../ggplot2/scales.md)); `geom_path`, `geom_segment` ([Geoms](../ggplot2/geoms.md)).

## Related

[Choosing a plot](choosing-a-plot.md) · [Gapminder](../datasets/gapminder.md) · [Wheat prices](../datasets/wheat-prices.md) · [Famines](../datasets/famines.md)

## Sources

`time-series.Rmd`. Summary: [Time series](../sources/time-series.md). Source code problems: [lint 2026-09-30](../analyses/lint-2026-09-30.md).
