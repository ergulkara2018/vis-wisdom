---
title: Perceptual ranking of encodings (Cleveland–McGill)
type: concept
tags: [perception, encoding, cleveland, continuous]
sources: [general-strategy.Rmd, continuous-continuous.Rmd, references.bib]
updated: 2026-09-30
---

Cleveland & McGill (1985) ran an experiment on how accurately humans decode different encodings of **continuous** data. The book reports this ranking, best to worst:

1. Position along a common scale
2. Position along identical but nonaligned scales (same axis, different facets)
3. Length
4. Angle
5. Slope
6. Area
7. Volume
8. Density
9. Color saturation
10. Color hue

**Scope:** continuous variables only ("continuous" in the ggplot2 sense). Hue is a poor way to show a continuous variable but can work well for discrete ones.

## How the book uses it

1. Loosely rank the variables by importance.
2. Give the most important variables the highest-ranked encodings; move down the list only when forced.
3. Reject options that don't make semantic sense — e.g. for `floors` next to `height_ft` on the tallest buildings: faceting doesn't make sense; *length* would wrongly imply floors are in height units; angle is unsuitable; so *area* (`size`) is used.
4. Accept the cost: readers can't read exact floors from area, but can see the outlier.

Three-variable application (Gapminder 2015): life expectancy and GDP → the two position axes; region (discrete) → color; population → size (area). See [Continuous-continuous guide](../guides/continuous-continuous-relationships.md).

## Evidence in the book's own examples

Height by color: Lotte World Tower and One World Trade Center look identical; height by size has the same problem; position and length make both estimation and comparison easy ([Encoding and decoding](encoding-and-decoding.md)).

## Limits and alternatives

- Before stacking encodings, ask whether a [derived variable](derived-variables.md) (e.g. `height_ft / floors`) answers the question with position alone.
- Size encodings make the *relationship* between axis variables and the sized variable hard to judge ([Claus Wilke](../people/claus-wilke.md), as cited in the book).
- Note (wiki, not from the sources): the ranking is reported as written in the book; the original 1985 paper is not in `raw/` and has not been checked — see [Open questions](../open-questions.md).

## Related

[Scales](../ggplot2/scales.md) (size, color) · [Color scales](color-scales.md)

## Sources

`general-strategy.Rmd` — "Encodings"; `continuous-continuous.Rmd` — "Three continuous variables". Summaries: [General strategy](../sources/general-strategy.md), [Continuous-continuous](../sources/continuous-continuous.md).
