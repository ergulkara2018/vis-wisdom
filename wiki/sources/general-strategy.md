---
title: "Source: General strategy (general-strategy.Rmd)"
type: source
tags: [strategy, perception, encoding, cleveland]
sources: [general-strategy.Rmd, references.bib]
updated: 2026-09-30
---

The book's conceptual core. It frames visualization as *encoding* data into visual elements that a viewer must *decode*, ranks encodings by how accurately humans decode them (Cleveland & McGill), and ends with four practical strategies that apply to every plot.

## Structure and claims

1. **The goals of visualization**
   - Two kinds of plots: *EDA plots* (quick, for yourself, to answer questions) vs *presentation plots* (slow, for others, to transfer an idea as effectively as possible). → [EDA vs presentation plots](../concepts/eda-vs-presentation-plots.md)
   - *Encoding and decoding*: data isn't visual by default; you encode values into visual elements and the viewer decodes them. Cleveland's view: a plot succeeds only if decoding goes well. Worked examples: `geom_col()` vs `geom_point()` for the 100 m final; alphabetical vs sorted tallest-buildings bars. → [Encoding and decoding](../concepts/encoding-and-decoding.md)
2. **Perception**
   - Demonstration: building height encoded as position or length is easy to read; as color or size it is much harder. The Cleveland–McGill ranking of ten encodings for *continuous* variables. → [Perceptual ranking](../concepts/perceptual-ranking.md)
   - Method: rank variables by importance and give the most important ones the top-ranked encodings; walk down the list, rejecting options that don't make sense (faceting, length, angle) until area works (`floors` as point size).
   - Insight: *create new variables* instead of encoding several at once — plotting `height_ft / floors` directly shows *two* unusual buildings (Lotte World Tower: short floors; Tianjin CTF Finance Centre: tall floors). → [Derived variables](../concepts/derived-variables.md)
3. **Strategies** → [Visualization strategies](../concepts/visualization-strategies.md): set goals · go for quantity · look at your plots (imagine seeing them for the first time) · iterate.
   - Example of "look at your plots": a strip of country vs height points hides that China has the most tall buildings; a bar count (`fct_infreq() %>% fct_rev()`) shows it.

## Data

[Tallest buildings](../datasets/tallest-buildings.md) (main), [Olympic 100 m final](../datasets/olympics-100m.md).

## Related

[Discrete-continuous source](discrete-continuous.md) (precedes this chapter in the book order) · [Ordering categories](../concepts/ordering-categories.md) · [Choosing a plot](../guides/choosing-a-plot.md)

## Sources

`general-strategy.Rmd` — all sections. Cites Cleveland & McGill (1985) three times in `references.bib`.
