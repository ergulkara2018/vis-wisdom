---
title: Paired data
type: concept
tags: [scatterplots, comparison, reference-lines]
sources: [continuous-continuous.Rmd]
updated: 2026-09-30
---

**Paired data:** the same measure at two points (children's heights at age 3 and 5; life expectancy in 2010 and 2015 for each country). Reshape to one column per time (`spread(key = year, value = life_expectancy, sep = "_")`).

## Three views from the book (each highlights different things)

1. **Scatter of one time against the other** (`year_2010` vs `year_2015`):
   - `coord_fixed()` so equal units are equal lengths;
   - `geom_abline(slope = 1, intercept = 0)` reference line — *no change*; above = increased, below = decreased; annotate these regions with `annotate("text", …)`;
   - label outliers with `ggrepel::geom_text_repel()` (Haiti after the 2010 earthquake; Syria and Libya after their 2011 civil wars — hypotheses the plot prompts);
   - `color = region` shows many African countries started low but made some of the largest absolute gains.
   Weakness: exact change per country is hard to estimate because both values use position.
2. **Plot the difference** (`diff = year_2015 - year_2010`) — becomes a discrete-continuous problem (dot plot ordered by `diff`; limited to Asia because 183 countries is too many). Shows change, hides levels. See [Derived variables](derived-variables.md), [Discrete-continuous guide](../guides/discrete-continuous-relationships.md).
3. **Both values on one axis with connecting segments** (`geom_segment()`, colors for the two years, ordered by 2015): shows both levels and the change. Lines help "if the connection between points is important".

## Related

[Layering and reference lines](layering-and-reference-lines.md) · [Direct labeling and legends](direct-labeling-and-legends.md) · [Gapminder](../datasets/gapminder.md)

## Sources

`continuous-continuous.Rmd` — "Paired data". Summary: [Continuous-continuous](../sources/continuous-continuous.md).
