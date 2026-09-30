---
title: Theme
type: ggplot2
tags: [ggplot2, theme, reference]
sources: [distributions.Rmd, ggplot2-basics.Rmd, continuous-continuous.Rmd, general-strategy.Rmd]
updated: 2026-09-30
---

The theme controls everything unrelated to the data: background color, tick length, grid lines, text size/angle, legend placement. Every plot has a default theme (gray background, white grid lines). Theme is *not* part of the grammar of graphics but is an element of the recommended template ([Grammar](../concepts/grammar-of-graphics.md), [Plot template](plot-template.md)).

## Patterns used

- `theme(axis.text.x = element_text(angle = -45, hjust = 0))` — angle x labels; `hjust = 0` left-aligns text so labels move closer to the axis (`hjust = 1` right-aligns). Preferred over `coord_flip()` for boxplots ([Summary vs detail](../concepts/summary-vs-detail.md)).
- `theme(legend.justification = "top")` — legend near the lines ([Direct labeling](../concepts/direct-labeling-and-legends.md)).
- `theme(axis.text.x = element_blank(), axis.ticks.x = element_blank())` — hide an axis when it carries no information (color/size-only encodings).
- `theme_void()` — used for color-bar demos and the annotated boxplot diagram.
- `theme(plot.tag = ..., plot.tag.position = "topright")` inside `stamp()` — the book's "Bad" tag ([Book build and data](../sources/book-build-and-data.md)).

## Element functions

Most `theme()` arguments need an *element function*: `element_text()` for text (`axis.text.x`), `element_line()` for lines (`axis.line`), etc. The [theme documentation](https://ggplot2.tidyverse.org/reference/theme.html) groups arguments and names the right element function at the start of each group.

## Sources

`distributions.Rmd` — "`theme()`". Summary: [Distributions](../sources/distributions.md).
