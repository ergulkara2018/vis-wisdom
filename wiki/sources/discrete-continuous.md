---
title: "Source: Discrete-continuous relationships (discrete-continuous.Rmd)"
type: source
tags: [bar-plots, dot-plots, coordinate-systems, factors]
sources: [discrete-continuous.Rmd, references.bib]
updated: 2026-09-30
---

How to plot a continuous amount against a discrete category (sheep per state, caffeine per drink). Introduces coordinate-system mechanics first, then works the Utah-languages example from a bad bar chart to a good one, compares bars with dots, and handles a second discrete variable.

## Structure and claims

- **Definition:** *discrete-continuous* = continuous variable against a discrete one. ggplot2 treats integers/doubles as continuous and only factors, characters and logicals as discrete (`count = c(1L, 2L)` still gets a continuous scale) — this later explains why `fill = year` fails until `year` becomes a factor.
- **Coordinate systems (mechanics):** `coord_cartesian()` is the default; `coord_fixed()` for aspect ratio (distorted star → correct star); zoom with `xlim`/`ylim` inside the coord function, *not* by filtering data; `coord_flip()`. → [Coordinate systems](../ggplot2/coordinate-systems.md)
- **Two goals for a discrete-continuous plot:** make it easy to (1) connect categories with their numbers and (2) compare numbers with each other. The chapter uses these to evaluate each plot. → [Discrete-continuous guide](../guides/discrete-continuous-relationships.md)
- **Effective bar plots:** flip to fix overlapping labels; **reorder** by the plotted amount (`fct_reorder()`), because ggplot2 sorts character variables alphabetically. `geom_bar()` for counts (`fct_infreq() %>% fct_rev()`). → [Ordering categories](../concepts/ordering-categories.md)
- **Bars vs dots:** bars encode length, so the axis must start at 0; dots encode position, so the axis can start anywhere. Bars compare to 0; dots compare values to each other. The Tufte question "Compared to what?" and the 100 m final: bars hide the story (Bolt far ahead, a pack, stragglers). → [Zero baseline](../concepts/zero-baseline-for-bars.md) · [Compared to what?](../concepts/compared-to-what.md)
- **Two discrete categories:** stacked bars are rarely a good idea ("visual arithmetic"); `position = "dodge"` helps for 2 fill values, not for 10 (`trans`); faceting is the fallback. Put the variable with *more* values on the axis and facet by the one with fewer; use `facet_grid(rows = ...)` so facets share an x-axis. → [Stacking problem](../concepts/stacking-problem.md) · [Faceting strategy](../concepts/faceting-strategy.md)

## Data

[Utah languages (US languages)](../datasets/us-languages.md), [Olympic 100 m final](../datasets/olympics-100m.md), [built-in R data sets](../datasets/builtin-r-datasets.md) (`mpg`).

## Related

[General strategy source](general-strategy.md) · [Bad-to-good catalog](../analyses/bad-to-good-catalog.md) · [Tufte](../people/edward-tufte.md)

## Sources

`discrete-continuous.Rmd` — all sections; cites Tufte (2001, p. 74). See [lint notes](../analyses/lint-2026-09-30.md) for a claim about what ggplot2 "requires" for bar axes.
