---
title: "Source: Time series (time-series.Rmd)"
type: source
tags: [time-series, aspect-ratio, trends, dates]
sources: [time-series.Rmd, references.bib]
updated: 2026-09-30
---

How to plot data over time, organized by *what you want the viewer to notice*: a long-term trend, short-term fluctuations, cycles, or individual values. Uses Gapminder life expectancy (especially South Africa), wheat prices, flights, and famines.

## Structure and claims

- **Mechanics — date/time scales:** `scale_*_date()`, `scale_*_datetime()`, `scale_*_time()` give meaningful breaks/labels; `date_breaks = "6 hours"` and `date_labels = "%a %I %p"` (strptime codes). lubridate helps with dates. → [Scales](../ggplot2/scales.md)
- **Banking to 45:** line-segment angles depend on aspect ratio; Cleveland, McGill & McGill (1988) found the most discriminable slopes when the average slope is 45°; Talbot et al. (2012) did not replicate it, so treat it as a heuristic — experiment with aspect ratio. → [Aspect ratio and banking to 45](../concepts/aspect-ratio-and-banking.md)
- **Trends:** add `geom_line()` to points; fewer points needed as data gets dense; add reference lines (`geom_vline` at 1994) to check hypotheses; **test a hypothesis by comparing** South Africa with neighbors — all four dropped in the early 1990s, so the dip is unlikely due to the end of apartheid; label lines directly and drop the legend (`guides(color = "none")`).
  - *Distributions over time:* many countries → alpha-faded lines + a `loess` smooth; subdivide Africa into regions (`region_gm8`); the Sub-Saharan dip is attributed (by the book) to the HIV/AIDS pandemic; boxplots per decade for distribution-over-time.
  - *Two response variables:* `geom_path()` connects points in data order (vs `geom_line()` in x order); needs arrows or year labels; arrows for EDA, labels for presentation.
  - *Multiple trend types:* wheat prices have a cycle and a long-term decline; aspect ratio decides which shows; `loess` shows only the long-term trend. → [Time-series guide](../guides/time-series.md)
- **Short-term fluctuations:** for discrete time units (hourly flight counts) columns or `geom_segment()` lines work better than point+line: they show gaps (no night flights), group days, and allow color (weekend).
- **Individual values:** when there's no trend to show (famines), treat the x-axis as a timeline of individual events: bubble plot (size = deaths, fill = region) or `geom_segment` spans for famine duration, with labels via `ggrepel`. → [Perceptual ranking](../concepts/perceptual-ranking.md) (size and position encodings) · [Log scales](../concepts/log-scales.md)

## Data

[Gapminder](../datasets/gapminder.md) (5-yearly + full 1800–2100 life expectancy), [Wheat prices](../datasets/wheat-prices.md), [Famines](../datasets/famines.md), [built-in R data sets](../datasets/builtin-r-datasets.md) (`nycflights13::flights`).

## Known problems in the source

Undefined objects (`flight_counts_feb_week1`, `countries`) and a text/code mismatch — see [lint 2026-09-30](../analyses/lint-2026-09-30.md).

## Sources

`time-series.Rmd` — all sections; cites Cleveland et al. (1988) and Talbot et al. (2012).
