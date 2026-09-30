---
title: Factors with forcats
type: ggplot2
tags: [ggplot2, forcats, factors, reference]
sources: [discrete-continuous.Rmd, general-strategy.Rmd, distributions.Rmd]
updated: 2026-09-30
---

ggplot2 plots character variables alphabetically (bottom to top on a flipped axis); factor levels control any other order. A *factor* is a categorical variable with a fixed set of values ("levels"). The book points to the R4DS *Factors* chapter.

| Function | Effect | Example in the book |
|---|---|---|
| `fct_reorder(f, x)` | order levels by another variable | `mutate(language = fct_reorder(language, speakers))` |
| `fct_reorder(f, -x)` | reverse that order | `fct_reorder(name, -time)` (fastest at top) |
| `fct_reorder(f, x / y)` | order by a computed quantity | `fct_reorder(building, height_ft / floors)` |
| `fct_infreq(f)` | order by frequency (most common first) | `mpg %>% mutate(drv = fct_infreq(drv))` |
| `fct_rev()` | reverse level order | `fct_infreq(drv) %>% fct_rev()` (low → high, needed with `coord_flip()`) |
| `as.factor(x)` | make an integer discrete for fill/color | `as.factor(year)` |

Also: for bar `fill`, the variable must be discrete, so integers like `year` must be converted.

Why ordering matters: [Ordering categories](../concepts/ordering-categories.md).

## Sources

`discrete-continuous.Rmd` — "Effective bar plots", "`geom_bar()`", "Color and facets". Summary: [Discrete-continuous](../sources/discrete-continuous.md).
