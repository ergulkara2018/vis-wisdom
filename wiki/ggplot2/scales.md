---
title: Scales used in the book
type: ggplot2
tags: [ggplot2, scales, reference]
sources: [continuous-continuous.Rmd, time-series.Rmd, general-strategy.Rmd]
updated: 2026-09-30
---

| Scale function | Purpose | Notes / concept |
|---|---|---|
| `scale_x_log10()`, `scale_y_log10()` | log axes | [Log scales](../concepts/log-scales.md) |
| `scale_*_gradient()` | sequential color; `low`, `high` | [Color scales](../concepts/color-scales.md) |
| `scale_*_gradient2()` | diverging color; `low`, `mid`, `high`, `midpoint` | [Color scales](../concepts/color-scales.md) |
| `scale_*_viridis_c()` (`_d` for discrete) | colorblind-friendly | [Color scales](../concepts/color-scales.md) |
| `scale_size()` | scales **area** (people judge area, not radius); `breaks`, `range` | [Perceptual ranking](../concepts/perceptual-ranking.md) |
| `scale_color_discrete(breaks = …)` | reorder legend entries | [Direct labeling](../concepts/direct-labeling-and-legends.md) |
| `scale_x_continuous(breaks = seq(...))` | custom breaks | boxplots over decades |
| `scale_*_date()`, `scale_*_datetime()`, `scale_*_time()` | date/time axes with sensible breaks/labels; `date_breaks = "6 hours"`, `date_labels = "%a %I %p"` (formats in `?strptime`) | [Time-series guide](../guides/time-series.md) |

- ggplot2 infers continuous vs discrete from the type: integers/doubles → continuous; factors/characters/logicals → discrete. Hence `fill = year` (integer) needs `as.factor(year)` for bars ([Discrete-continuous source](../sources/discrete-continuous.md)).
- In the recommended code order, scales come after geoms ([Plot template](plot-template.md)).
- Cheat-sheet section: "Scales".

## Sources

`continuous-continuous.Rmd` (Mechanics), `time-series.Rmd` (Date/time scales), `general-strategy.Rmd`. Summaries: [Continuous-continuous](../sources/continuous-continuous.md), [Time series](../sources/time-series.md).
