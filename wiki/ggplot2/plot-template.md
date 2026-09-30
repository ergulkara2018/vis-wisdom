---
title: Plot code template and style
type: ggplot2
tags: [ggplot2, style, template, pipes]
sources: [ggplot2-basics.Rmd]
updated: 2026-09-30
---

The book's recommended construction order (verbatim idea):

```r
<DATA> %>%
  ggplot(mapping = aes(<MAPPINGS>)) +
  <GEOM(s)> +
  <SCALE_FUNCTION(s)> +
  <COORDINATE_FUNCTION> +
  <FACET_FUNCTION> +
  <THEME> +
  <LABELS>
```

## Style rules

- **Pipe the data in** (`mpg %>% ggplot(...)`): shows which dataset is plotted and lets you `filter()`/`mutate()` first. The pipe passes the data to `ggplot()`'s `data` argument.
- **Shared aesthetics go in `ggplot()`; geom-specific ones in the geom call.**
- **Position adjustments and stat transformations** are usually unique to a geom — specify them in the geom call (`geom_bar(position = "dodge")`).
- Name arguments the way the book does: `mapping = aes(...)`; facets via `vars()` ([Facets](facets.md)).

Mapping to concepts: [Grammar of graphics](../concepts/grammar-of-graphics.md). Element pages: [Geoms](geoms.md), [Scales](scales.md), [Coordinate systems](coordinate-systems.md), [Facets](facets.md), [Theme](theme.md), [Annotations and labels](annotations-and-labels.md).

## Sources

`ggplot2-basics.Rmd` — "Pipes and aesthetics", "The grammar of graphics". Summary: [ggplot2 basics](../sources/ggplot2-basics.md).
