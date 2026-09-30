---
title: Ordering categories
type: concept
tags: [factors, bar-plots, comparison]
sources: [discrete-continuous.Rmd, general-strategy.Rmd, distributions.Rmd]
updated: 2026-09-30
---

**Rule (book):** reordering a character variable before plotting is almost always a good idea; you'll rarely want alphabetical order. Usually order by the amount on the other axis. Exception: match an intrinsic order (e.g. the ordered factor `clarity` in `diamonds`).

## Why

Unordered bars force back-and-forth eye motion: comparing Vietnamese with French in the alphabetical plot is hard; sorted, French clearly wins and the shortest bar (Laotian) is obvious. Sorted categories also make differences between adjacent categories easy to estimate. It supports the goal "compare numbers to each other" ([Discrete-continuous guide](../guides/discrete-continuous-relationships.md)).

## How (ggplot2)

- ggplot2 draws character variables alphabetically from bottom to top regardless of row order; convert to a factor to control order.
- `fct_reorder(category, amount)` — order by another variable; use `-amount` (e.g. `fct_reorder(name, -time)`) to reverse.
- `fct_infreq()` — order by count (for `geom_bar()`); add `fct_rev()` for low-to-high (needed with `coord_flip()`).
- Also used for boxplots: `fct_reorder(division, age)` orders by median.

Details: [Forcats](../ggplot2/forcats.md).

## Related

[Zero baseline](zero-baseline-for-bars.md) · [Encoding and decoding](encoding-and-decoding.md)

## Sources

`discrete-continuous.Rmd` — "Effective bar plots", "`geom_bar()`"; `general-strategy.Rmd` — alphabetical-bars example; `distributions.Rmd` — boxplots. Summary: [Discrete-continuous](../sources/discrete-continuous.md).
