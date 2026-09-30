---
title: Faceting strategy
type: concept
tags: [facets, small-multiples, comparison]
sources: [discrete-continuous.Rmd, distributions.Rmd]
updated: 2026-09-30
---

Faceting splits a plot into panels (see [Facets](../ggplot2/facets.md) for syntax). The book's guidance on *which* variable to facet and *how* to lay the panels out:

1. **Comparisons are easier within a facet than across facets.** Decide what you want compared, and put *that* within a panel. Facet by transmission to see drivetrain numbers within a transmission; facet by drivetrain to see transmission numbers within a drivetrain.
2. **Put the variable with more values on the axis; facet by the one with fewer.**
3. **Align panels that share a scale.** `facet_grid(rows = vars(...))` stacks panels vertically so they share an x-axis, which makes distributions comparable; side-by-side (column) histograms of the same data were hard to compare. *Note (wiki inference, not stated in the book):* this fits item 2 of the [perceptual ranking](perceptual-ranking.md) (position along identical but nonaligned scales) — aligned panels keep comparisons on the better-ranked channel.
4. **Use facets when dodging fails:** dodging is fine for 2 fill values, not for 10 ([Stacking problem](stacking-problem.md)).

Faceting is also one of the rungs in the perceptual ranking: "position along identical but nonaligned scales" — the book skips it for `floors` vs `height_ft` because it doesn't make sense to facet by either.

## Related

[Distributions guide](../guides/distributions.md) · [Discrete-continuous guide](../guides/discrete-continuous-relationships.md)

## Sources

`discrete-continuous.Rmd` — "Color and facets"; `distributions.Rmd` — "Multiple distributions". Summary: [Discrete-continuous](../sources/discrete-continuous.md).
