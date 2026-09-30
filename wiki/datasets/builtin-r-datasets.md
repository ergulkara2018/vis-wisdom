---
title: Built-in and package data sets
type: dataset
tags: [dataset, mpg, diamonds, nycflights13]
sources: [discrete-continuous.Rmd, distributions.Rmd, continuous-continuous.Rmd, time-series.Rmd, ggplot2-basics.Rmd]
updated: 2026-09-30
---

Data sets that ship with packages, used for short mechanics demos (not stored in `data/`).

| Data | Package | Used for |
|---|---|---|
| `mpg` | ggplot2 | facets and aesthetics ([ggplot2 basics](../sources/ggplot2-basics.md)); `geom_bar()` and dodge/facets with `drv`, `year`, `trans` ([Stacking problem](../concepts/stacking-problem.md)); boxplots by `class`/`manufacturer` ([Layering](../concepts/layering-and-reference-lines.md), [Theme](../ggplot2/theme.md)); `geom_count()` and size scales ([Overplotting](../concepts/overplotting.md)) |
| `diamonds` | ggplot2 | `geom_hex()` with log scales and viridis (carat vs price) ([Color scales](../concepts/color-scales.md)); ordered factor `clarity` as an intrinsic order ([Ordering categories](../concepts/ordering-categories.md)) |
| `nycflights13::flights` | nycflights13 | date-time scales, hourly counts of flights ([Time-series guide](../guides/time-series.md)) |

Also simulated data: `rnorm()` samples for density examples ([Summary vs detail](../concepts/summary-vs-detail.md)); `sim_3` for the annotated boxplot diagram; the star polygon for `coord_fixed()`.

## Sources

The chapters in frontmatter. Note that `time-series.Rmd` uses an object `flight_counts_feb_week1` that is never defined ([lint 2026-09-30](../analyses/lint-2026-09-30.md)).
