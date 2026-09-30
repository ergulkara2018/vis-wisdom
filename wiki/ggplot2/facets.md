---
title: Facets
type: ggplot2
tags: [ggplot2, facets, reference]
sources: [ggplot2-basics.Rmd, discrete-continuous.Rmd, distributions.Rmd]
updated: 2026-09-30
---

Syntax in this book (updated from R4DS's `~` formulas) — wrap the faceting variable in `vars()`:

```r
facet_wrap(vars(class), nrow = 2)                 # ribbon of panels; nrow/ncol control layout
facet_grid(rows = vars(year), cols = vars(class)) # explicit rows and columns
```

- `facet_wrap()` — replace `~ class` with `vars(class)`; `nrow`/`ncol` unchanged.
- `facet_grid()` — now has `rows` and `cols` arguments; again use `vars()`.
- `facet_grid(rows = vars(drv))` aligns panels vertically so they share an x-axis — used to compare distributions ([Faceting strategy](../concepts/faceting-strategy.md)).
- Faceting is a grammar element set by you ([Grammar of graphics](../concepts/grammar-of-graphics.md)) and sits after coords in the recommended order ([Plot template](plot-template.md)). Cheat-sheet section: "Faceting".

Strategy (which variable to facet, which layout) is in [Faceting strategy](../concepts/faceting-strategy.md); when to choose facets over dodging/stacking in [Stacking problem](../concepts/stacking-problem.md).

## Sources

`ggplot2-basics.Rmd` — "Facet syntax". Summary: [ggplot2 basics](../sources/ggplot2-basics.md).
