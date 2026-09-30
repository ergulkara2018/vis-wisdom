---
title: Derived variables beat multi-encoding
type: concept
tags: [strategy, encoding, transformation]
sources: [general-strategy.Rmd, continuous-continuous.Rmd]
updated: 2026-09-30
---

**Insight (book):** "Creating new variables can often lead to better insights than plotting several variables at once." If a plot needs several continuous variables, ask whether a more direct measure of the relationship you care about exists.

## Examples

- **Tallest buildings:** `height_ft` (position) + `floors` (size) shows only that Tianjin CTF Finance Centre is an outlier. Plotting `height_ft / floors` with position alone shows *both* Tianjin CTF (very tall floors) and Lotte World Tower (very short floors) as unusual — and uses the best-ranked encoding ([Perceptual ranking](perceptual-ranking.md)).
- **Paired life expectancy:** a scatter of 2010 vs 2015 makes it hard to read each country's exact change; computing `diff = year_2015 - year_2010` turns it into a discrete-continuous plot of the change. Plotting 2010 and 2015 on one axis with connecting segments shows both levels and change ([Paired data](paired-data.md)).
- **Size-encoded bubble plots:** the book warns they make the relationship between the axis variables and the size variable hard to judge; if that relationship matters, create variables that express it explicitly.

## Trade-off

A derived variable answers one question sharply but hides the raw levels (the `diff` plot doesn't show actual life expectancies) — pick by goal ([Visualization strategies](visualization-strategies.md)).

## Related

[Encoding and decoding](encoding-and-decoding.md) · [Continuous-continuous guide](../guides/continuous-continuous-relationships.md)

## Sources

`general-strategy.Rmd` — "Encodings"; `continuous-continuous.Rmd` — "Paired data", "Three continuous variables". Summaries: [General strategy](../sources/general-strategy.md), [Continuous-continuous](../sources/continuous-continuous.md).
