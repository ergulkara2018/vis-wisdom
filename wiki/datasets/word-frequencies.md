---
title: War and Peace word frequencies
type: dataset
tags: [dataset, text, power-law]
sources: [data/word-frequencies/data.R, continuous-continuous.Rmd]
updated: 2026-09-30
---

`war_and_peace` — every word in Tolstoy's *War and Peace* (Project Gutenberg ebook 2600), tokenized with `tidytext`, counted, and ranked (script version 2018-02-01). Columns: `word`, `freq`, `rank`.

- **Used for:** the power-law example for [log scales](../concepts/log-scales.md): frequency is inversely proportional to rank; curved on linear axes, a straight line on log–log axes.

## Sources

`data/word-frequencies/data.R`; `continuous-continuous.Rmd` — "Log scales". The `.rds` was not opened.
