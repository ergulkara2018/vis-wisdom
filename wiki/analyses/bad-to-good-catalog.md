---
title: Catalog of the book's bad plots and their fixes
type: analysis
tags: [analysis, catalog, iteration, bad-plots]
sources: [discrete-continuous.Rmd, distributions.Rmd, continuous-continuous.Rmd, time-series.Rmd, general-strategy.Rmd, _common.R]
updated: 2026-09-30
---

*Filed answer to: "Which poor plots does the book show, why are they poor, and what fixes them?"* The book marks many with a red **Bad** tag (`stamp("Bad")`, defined in `_common.R`); others are identified only in the text (marked † below). Each row is an instance of [iteration](../concepts/visualization-strategies.md).

## One discrete variable / two discrete variables

| Bad plot | Why it fails | Fix | Concept |
|---|---|---|---|
| Utah languages `geom_col()` with overlapping x labels † | can't connect category to number | `coord_flip()` | [Coordinate systems](../ggplot2/coordinate-systems.md) |
| …flipped but alphabetical † | can't compare numbers; eye darts back and forth | `fct_reorder()` | [Ordering categories](../concepts/ordering-categories.md) |
| 100 m final as bars from 0 † | implies "compared to 0"; hides the race | dots | [Compared to what?](../concepts/compared-to-what.md) |
| `mpg` stacked bars by year † | floating baselines → visual arithmetic | `position = "dodge"` | [Stacking problem](../concepts/stacking-problem.md) |
| Dodged bars with 10 `trans` levels † | can't remember colors; can't compare same-colored bars | facets (more-valued variable on axis) | [Faceting strategy](../concepts/faceting-strategy.md) |
| Buildings in alphabetical bars † | unordered amounts hard to compare | sort by height; dots | [Perceptual ranking](../concepts/perceptual-ranking.md) |
| Height by color or by size † | low-ranked encodings | position/length | [Perceptual ranking](../concepts/perceptual-ranking.md) |
| Country-vs-height strip † | first-time viewers can't see "China has most" | plot counts | [Visualization strategies](../concepts/visualization-strategies.md) |

## Distributions

| Bad plot | Why it fails | Fix | Concept |
|---|---|---|---|
| Histogram `binwidth = .1` | peaky; bars = one person | `binwidth = 5` | [Bin width](../concepts/bin-width.md) |
| Histogram `binwidth = 20` | too coarse | `binwidth = 5` | [Bin width](../concepts/bin-width.md) |
| Stacked histogram by party | can't read Democrat counts | vertical facets or overlaid freqpolys | [Stacking problem](../concepts/stacking-problem.md) |
| Column facets (side by side) | hard to compare across | `facet_grid(rows = ...)` | [Faceting strategy](../concepts/faceting-strategy.md) |
| Filled density, default opaque fill | curves hidden | `alpha = 0.5` (with enough data) | [Summary vs detail](../concepts/summary-vs-detail.md) |
| Freqpolys colored by 9 divisions | too many colors, overlap | boxplots | [Summary vs detail](../concepts/summary-vs-detail.md) |
| Boxplots with overlapping labels | labels unreadable | angle labels with `theme()` | [Theme](../ggplot2/theme.md) |
| …fixed with `coord_flip()` | harder to compare medians/box edges | keep vertical + angled labels | [Coordinate systems](../ggplot2/coordinate-systems.md) |
| Reference line drawn over boxplots † | obscures information | draw the line first | [Layering](../concepts/layering-and-reference-lines.md) |

## Continuous-continuous

| Bad plot | Why it fails | Fix | Concept |
|---|---|---|---|
| Asian populations on a linear axis | small countries look like 0 | `scale_x_log10()` | [Log scales](../concepts/log-scales.md) |
| GDP vs life expectancy, linear | data crushed at left edge | log scale | [Log scales](../concepts/log-scales.md) |
| …log scale, still many points | overplotting | `geom_hex()`/`alpha` | [Overplotting](../concepts/overplotting.md) |
| Points colored by region | can't see per-region relationship | smooths only | [Smoothing](../concepts/smoothing.md) |
| …with smooth lines over the points | lines lost among points | drop the points | [Smoothing](../concepts/smoothing.md) |
| Smooth legend in arbitrary order † | back-and-forth to decode | reorder legend; move legend | [Direct labeling](../concepts/direct-labeling-and-legends.md) |
| Paired scatter with unequal axis units † | confusing | `coord_fixed()` + `y = x` line | [Paired data](../concepts/paired-data.md) |
| Bubbles hiding one another † | large points cover small | `arrange(desc(population))`, `shape = 21` | [Overplotting](../concepts/overplotting.md) |

## Time series

| Bad plot | Why it fails | Fix | Concept |
|---|---|---|---|
| `geom_path()` with no direction | can't tell start/end | arrow (EDA) or year labels (presentation) | [Time-series guide](../guides/time-series.md) |
| Wheat price line with the wrong aspect ratio † | hides the trend you care about | choose aspect ratio for the goal | [Aspect ratio](../concepts/aspect-ratio-and-banking.md) |
| Hourly flights as point+line † | hides the nightly gaps, hard to tie points to hours | `geom_col()` / `geom_segment()` | [Time-series guide](../guides/time-series.md) |

† = identified as a problem in the text but not tagged "Bad" in the plot.

## Pattern

Most fixes are one of four moves: **remove a low-ranked encoding**, **give each comparison a shared baseline/axis**, **reduce what competes for attention** (fewer colors, drop points, summarize), or **make decoding direct** (labels near data, sorted order).

## Sources

The chapters in frontmatter; see the [source summaries](../sources/distributions.md).
