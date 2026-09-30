---
title: "Guide: discrete-continuous relationships"
type: guide
tags: [guide, bar-plots, dot-plots, categories]
sources: [discrete-continuous.Rmd, general-strategy.Rmd]
updated: 2026-09-30
---

Use when you want an **amount for each category** (sheep per state, speakers per language, race time per runner).

## Goals (from the book)

The plot should make it easy to (1) **connect categories with their numbers** and (2) **compare numbers to each other**. Treat the book's recipes as a starting point, "not the final word".

## Decision path

1. **One category, amounts given** → `geom_col()`; amounts implicit (counts) → `geom_bar()`.
2. **Labels overlap?** → `coord_flip()` so labels sit on the y-axis ([Coordinate systems](../ggplot2/coordinate-systems.md)).
3. **Sort** by the amount (`fct_reorder`, or `fct_infreq() %>% fct_rev()` for counts) ([Ordering categories](../concepts/ordering-categories.md)).
4. **Bars or dots?**
   - Bars → axis must start at 0 ([Zero baseline](../concepts/zero-baseline-for-bars.md)); good for values vs zero.
   - Dots (`geom_point`) → axis fitted to data; good when the question is how values compare to *each other* ([Compared to what?](../concepts/compared-to-what.md)).
5. **Second discrete variable:**
   - avoid stacked bars ([Stacking problem](../concepts/stacking-problem.md));
   - 2 levels → `position = "dodge"`;
   - more levels → facet; put the variable with more values on the axis; `facet_grid(rows = ...)` for shared x-axis ([Faceting strategy](../concepts/faceting-strategy.md)).
6. **Too many categories for one plot?** Filter to a subset (the book plots only Asia for the paired-life-expectancy differences) ([Paired data](../concepts/paired-data.md)).

## Worked example: Utah languages

Bars with overlapping labels (fails goal 1 and 2) → `coord_flip()` (goal 1 solved) → sorted by speakers (goal 2 solved) → optionally dots. See [Bad-to-good catalog](../analyses/bad-to-good-catalog.md) and [US languages](../datasets/us-languages.md).

## Related

[Choosing a plot](choosing-a-plot.md) · [General strategy source](../sources/general-strategy.md) · [Forcats](../ggplot2/forcats.md)

## Sources

`discrete-continuous.Rmd`. Summary: [Discrete-continuous](../sources/discrete-continuous.md).
