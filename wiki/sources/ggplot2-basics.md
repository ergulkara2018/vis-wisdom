---
title: "Source: ggplot2 basics (ggplot2-basics.Rmd)"
type: source
tags: [ggplot2, mechanics, grammar-of-graphics]
sources: [ggplot2-basics.Rmd, references.bib]
updated: 2026-09-30
---

A short on-ramp chapter: it points readers to sections of *R4DS* and the ggplot2 cheat sheet, then records where this book's conventions differ from them.

## Main points

- **Prerequisite reading** (links to R4DS): introduction, first steps, aesthetic mappings, common problems, facets, geometric objects, and the `labs()` label section. Cheat-sheet sections to locate: Basics, Geoms, Faceting, Labels. Advice: when you learn a function, find it on the cheat sheet.
- **Pipe-first style:** `mpg %>% ggplot(mapping = aes(x = displ, y = hwy)) + geom_point()`, not `ggplot(data = mpg) + geom_point(mapping = aes(...))`. The pipe shows which dataset is plotted and makes pre-plot manipulation (e.g. `filter()`) easy. Put aesthetics shared by all geoms in `ggplot()`, geom-specific ones in the geom. → [Plot template](../ggplot2/plot-template.md)
- **Updated facet syntax:** `facet_wrap(vars(class), nrow = 2)`, `facet_grid(rows = vars(year), cols = vars(class))` instead of `~` formulas. → [Facets](../ggplot2/facets.md)
- **Grammar of graphics:** a plot is assembled from eight elements (data, geoms, aesthetic mappings, facets + statistical transformation, position adjustment, coordinate system, scales); theme and labels are extra. Defaults fill unspecified elements. → [Grammar of graphics](../concepts/grammar-of-graphics.md)
- **Recommended code ordering:** data → `ggplot(aes())` → geoms → scales → coord → facet → theme → labels.

## Related

[Plot template](../ggplot2/plot-template.md) · [Facets](../ggplot2/facets.md) · [Grammar of graphics](../concepts/grammar-of-graphics.md) · [Hadley Wickham](../people/hadley-wickham.md) · [Theme](../ggplot2/theme.md)

## Sources

`ggplot2-basics.Rmd` — "Additional information": Pipes and aesthetics; Facet syntax; The grammar of graphics. Cites Wickham (2010) in `references.bib`.
