---
title: Log scales
type: concept
tags: [scales, transformation, power-law]
sources: [continuous-continuous.Rmd, time-series.Rmd]
updated: 2026-09-30
---

A log scale (`scale_x_log10()`, `scale_y_log10()`) is one of the most common uses of scale functions. The book gives two reasons to use one.

1. **Variables spanning several orders of magnitude.** On a linear axis, differences among small values vanish. Asian country populations: from Jordan to Micronesia all look alike and many look like 0; with `scale_x_log10()` small countries are distinguishable and readable. Same for GDP per capita in the Gapminder scatterplot (most points crushed at the left edge).
2. **Power laws.** When y ∝ x^k the relationship is a straight line on log–log axes. Word frequency vs rank in *War and Peace* is curved on linear axes and linear after `scale_x_log10() + scale_y_log10()`. Transforming both axes is also an easy *check* for a power law. The book describes the pattern as frequency being inversely proportional to rank for many collections of text.

Other uses in the book: famine deaths and GDP per capita over time (`scale_y_log10()` on `famines`); `diamonds` carat vs price with `geom_hex()`.

Note (wiki, not from the sources): reading values off a log axis requires the audience to know the axis is logarithmic — for presentation plots, label it ([EDA vs presentation](eda-vs-presentation-plots.md)).

## Related

[Scales](../ggplot2/scales.md) · [Overplotting](overplotting.md) · [Continuous-continuous guide](../guides/continuous-continuous-relationships.md)

## Sources

`continuous-continuous.Rmd` — "Log scales". Summary: [Continuous-continuous](../sources/continuous-continuous.md). Data: [Word frequencies](../datasets/word-frequencies.md), [Gapminder](../datasets/gapminder.md).
