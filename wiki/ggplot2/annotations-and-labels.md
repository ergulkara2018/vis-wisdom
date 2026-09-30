---
title: Annotations and labels
type: ggplot2
tags: [ggplot2, labels, annotations, ggrepel, reference]
sources: [general-strategy.Rmd, continuous-continuous.Rmd, time-series.Rmd, ggplot2-basics.Rmd]
updated: 2026-09-30
---

| Tool | Use in the book |
|---|---|
| `labs()` | title, subtitle, caption, axis and legend labels — crucial for presentation plots (R4DS "Label" section); e.g. `labs(x = "Building name", y = "Height (feet)", title = "Heights of the world's 10 tallest buildings")` ([EDA vs presentation](../concepts/eda-vs-presentation-plots.md)) |
| `annotate("text", x, y, label, hjust)` | free-floating text, e.g. "Life expectancy increased/decreased" on either side of the `y = x` line ([Paired data](../concepts/paired-data.md)) |
| `geom_text(data = …, aes(label = …), nudge_x)` | label selected rows, e.g. line ends ([Direct labeling](../concepts/direct-labeling-and-legends.md)) |
| `ggrepel::geom_text_repel()` | non-overlapping labels for outliers/events |
| `guides(color = "none")` | drop a legend after labeling directly |
| `arrow()` in `geom_path(arrow = …)` | show direction along a path |
| `stamp()` (from `_common.R`) | red "Bad" tag used in the book ([Book build and data](../sources/book-build-and-data.md)) |

The book links R4DS's *Annotations* section as the intro to effective annotations.

## Sources

`ggplot2-basics.Rmd` (labels), `continuous-continuous.Rmd` — "Annotations", `time-series.Rmd`. Summary: [Continuous-continuous](../sources/continuous-continuous.md).
