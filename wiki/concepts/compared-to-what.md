---
title: '"Compared to what?"'
type: concept
tags: [tufte, comparison, bars-vs-dots]
sources: [discrete-continuous.Rmd, references.bib]
updated: 2026-09-30
---

[Edward Tufte](../people/edward-tufte.md)'s directive, quoted in the book: *"To be truthful and revealing, data graphics must bear on the question at the heart of quantitative thinking: 'Compared to what?'"* (Tufte 2001, p. 74). The book treats it as a question to ask while designing any plot.

## The worked example

The men's 100 m final times (all ≈ 10 s):

- **Bar plot** (`geom_col`): bars start at 0, so the implied comparison is *time vs 0*. The takeaway is "everyone ran about 10 seconds" — useless without knowing whether 10 s is fast.
- **Dot plot** (`geom_point`): the axis zooms to the data range, so the implied comparison is *runner vs runner*. Now the race appears: a couple of runners behind, a pack in the middle, Bolt far ahead. That narrative was hidden in the bars.

The choice between bars and dots is "largely a choice between comparing values to 0 or comparing values to each other." See [Zero baseline for bars](zero-baseline-for-bars.md).

## Other appearances

- Comparing South Africa to its neighbors to test whether the post-apartheid dip was special ([Time-series guide](../guides/time-series.md)).
- Reference lines (overall median, `y = x`) that give each panel or point something to be compared to ([Layering and reference lines](layering-and-reference-lines.md), [Paired data](paired-data.md)).

## Sources

`discrete-continuous.Rmd` — "Bars vs. dots". Summary: [Discrete-continuous](../sources/discrete-continuous.md). Tufte's book is not in `raw/` (see [Open questions](../open-questions.md)).
