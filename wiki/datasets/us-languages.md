---
title: US languages spoken at home (ACS 2013)
type: dataset
tags: [dataset, census, utah, categories]
sources: [data/us-languages/non-english.R, discrete-continuous.Rmd]
updated: 2026-09-30
---

American Community Survey (2013) estimates of non-English languages spoken at home, fetched from the Census API (script version 2018-12-31). Three files: US, states, and `utah_languages` (top 20 languages **other than English and Spanish** in Utah) — the one the book uses. Columns: `language`, `speakers` (integer).

- **Used for:** the chapter's main example — bars with overlapping labels → `coord_flip()` → sorted with `fct_reorder()` → dots.
- **Note:** `speakers` is an integer yet ggplot2 treats it as continuous (the book's aside on integer vs discrete).

→ [Discrete-continuous guide](../guides/discrete-continuous-relationships.md) · [Ordering categories](../concepts/ordering-categories.md) · [Bad-to-good catalog](../analyses/bad-to-good-catalog.md)

## Sources

`data/us-languages/non-english.R`; `discrete-continuous.Rmd`. The `.rds` was not opened.
