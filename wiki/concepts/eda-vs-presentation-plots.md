---
title: EDA plots vs presentation plots
type: concept
tags: [goals, strategy, eda]
sources: [general-strategy.Rmd]
updated: 2026-09-30
---

The book distinguishes two purposes for a plot, and most of its advice depends on which one you are making.

| | EDA plot | Presentation plot |
|---|---|---|
| Audience | you | others, who may know nothing about the data |
| Purpose | answer questions; you don't know what it will show before you run it | transfer an idea from your mind to theirs as effectively as possible |
| Speed | quick; don't perfect details | *slow*; clear, focused plots take lots of iteration |
| Polish | minimal | labels, titles, legend position matter more |
| Goals look like | questions ("What's the tallest building?") | specific information to convey |
| Path annotation (time series) | arrows are fine | direct labels are better |

Visualization is just one tool of exploratory data analysis: ask questions, try to answer them, reformulate or ask new ones.

## Why it matters

- Encoding choices differ in value: in EDA, different encodings are different *viewpoints* (some show nothing, some lead to discoveries); in presentation, choose encodings so *decoding* is easy. See [Encoding and decoding](encoding-and-decoding.md).
- The same plot can be fine for EDA and poor for presentation — e.g. the unlabeled `geom_path()` of GDP vs life expectancy needs arrows (EDA) or year labels (presentation). See [Time-series guide](../guides/time-series.md).

## Related

[Visualization strategies](visualization-strategies.md) · [Encoding and decoding](encoding-and-decoding.md)

## Sources

`general-strategy.Rmd` — "Two types of plots"; `time-series.Rmd` — "Two response variables". Summary: [General strategy](../sources/general-strategy.md).
