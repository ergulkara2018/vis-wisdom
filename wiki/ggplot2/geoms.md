---
title: Geoms used in the book
type: ggplot2
tags: [ggplot2, geoms, reference]
sources: [discrete-continuous.Rmd, distributions.Rmd, continuous-continuous.Rmd, time-series.Rmd, general-strategy.Rmd]
updated: 2026-09-30
---

Quick index of every geom the book uses: what it's for, the book's advice, and the concept page that explains the why.

| Geom | Use | Book's advice | Concept |
|---|---|---|---|
| `geom_point()` | dots; scatter; bubble (with `size`); `shape = 21` has border + fill; `alpha` | dots allow non-zero axes; draw order = row order | [Zero baseline](../concepts/zero-baseline-for-bars.md), [Overplotting](../concepts/overplotting.md) |
| `geom_col()` | bars from a given value | axis must start at 0; sort categories | [Zero baseline](../concepts/zero-baseline-for-bars.md) |
| `geom_bar()` | bars of counts (only `x`) | special case of `geom_col`; `position = "dodge"`; avoid stack | [Stacking problem](../concepts/stacking-problem.md) |
| `geom_histogram()` | binned counts | always pick `binwidth` | [Bin width](../concepts/bin-width.md) |
| `geom_freqpoly()` | histogram as a line | best for overlays; `y = ..density..` | [Stacking problem](../concepts/stacking-problem.md) |
| `geom_density()` | smoothed histogram | only with enough data/simulation; fill needs `alpha` | [Summary vs detail](../concepts/summary-vs-detail.md) |
| `geom_boxplot()` | five-number-ish summary | many groups; no shape or n | [Summary vs detail](../concepts/summary-vs-detail.md) |
| `geom_violin()` | mirrored density | needs enough data; `draw_quantiles` | [Summary vs detail](../concepts/summary-vs-detail.md) |
| `geom_hline/vline/abline()` | reference lines | draw under data | [Layering](../concepts/layering-and-reference-lines.md) |
| `geom_hex()` / `geom_bin2d()` | binned 2-D counts | prefer hex + viridis | [Overplotting](../concepts/overplotting.md) |
| `geom_count()` | size = count at identical points | for complete overlap | [Overplotting](../concepts/overplotting.md) |
| `geom_smooth()` | trend + confidence band | `method = "loess"` unless huge data | [Smoothing](../concepts/smoothing.md) |
| `geom_line()` | connect in x order | add points when sparse | [Time-series guide](../guides/time-series.md) |
| `geom_path()` | connect in data order | arrows/labels; `arrange()` first | [Time-series guide](../guides/time-series.md) |
| `geom_segment()` | segments (`x, xend, y, yend`) | discrete time units; paired data | [Paired data](../concepts/paired-data.md) |
| `geom_text()` / `ggrepel::geom_text_repel()` | labels | label selected points/lines | [Direct labeling](../concepts/direct-labeling-and-legends.md) |
| `annotate("text", …)` | one-off text | region labels | [Annotations](annotations-and-labels.md) |

Stat/position live inside geoms: `position = "dodge"`, `stat` via computed `..density..`/`..count..`. See [Grammar of graphics](../concepts/grammar-of-graphics.md). The [ggplot2 cheat sheet](https://github.com/rstudio/cheatsheets/blob/master/data-visualization-2.1.pdf) "Geoms" section is the book's suggested lookup.

## Sources

The chapters listed in frontmatter; see the [source summaries](../sources/discrete-continuous.md) for the sections.
