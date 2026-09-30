---
title: "Guide: choosing a plot (decision table)"
type: guide
tags: [guide, synthesis, decision-table]
sources: []
updated: 2026-09-30
---

A cross-chapter synthesis of the book's advice: *what do you want to show* → *what to try* → *what to avoid*. Built from the wiki's concept and guide pages; each row links to the detail.

| Goal / data | First try | Adjust | Avoid |
|---|---|---|---|
| Amounts per category | flipped, **sorted** `geom_col()` or dots ([guide](discrete-continuous-relationships.md)) | dots if differences between values matter more than zero-relative size ([bars vs dots](../concepts/zero-baseline-for-bars.md)) | alphabetical order; overlapping labels; bars with non-zero baseline |
| Counts per category | `geom_bar()` with `fct_infreq() %>% fct_rev()` | — | plotting a measured value when you only want counts |
| Amounts per **two** categories | dodged bars (2 levels) or facets ([faceting](../concepts/faceting-strategy.md)) | more-valued variable on axis; vertical facets | stacked bars ([why](../concepts/stacking-problem.md)) |
| One distribution | histogram with chosen binwidth + median line ([guide](distributions.md)) | freqpoly / density as alternatives | default binwidth; density with little data |
| 2–3 distributions | overlaid freqpolys (`..density..` if sizes differ) | vertical facets | stacked histograms; column facets |
| Many distributions | boxplots / violins, sorted by median | angled labels instead of `coord_flip` | colored freqpolys |
| Two continuous variables | scatterplot ([guide](continuous-continuous-relationships.md)) | log scale; hex/alpha; loess smooth | unfixed overplotting |
| Same measure twice | scatter + `y = x` line, `coord_fixed()`; or difference dots; or segments ([paired](../concepts/paired-data.md)) | label outliers | reading exact changes off a scatter |
| Three continuous variables | x, y position; color (discrete) ; size | bigger size range; `shape = 21`; draw big first | trusting size to show relationships |
| Trend over time | line (+ points if sparse) ([guide](time-series.md)) | aspect ratio; reference line; direct labels | unlabeled `geom_path` |
| Fluctuations over discrete times | columns or segments | color by category | lines that hide gaps |
| Individual events over time | points/bubbles/segments with labels | log y | forcing a trend line |
| Anything | set goals, make many, look with fresh eyes, iterate ([strategies](../concepts/visualization-strategies.md)) | — | committing to the first plot |

Two meta-rules that cut across rows: encode the most important variable with the best-ranked channel ([perceptual ranking](../concepts/perceptual-ranking.md)), and consider a [derived variable](../concepts/derived-variables.md) before adding another encoding.

This is a wiki synthesis of the book's recommendations; it does not add outside advice. Gaps (maps, uncertainty, discrete color palettes, etc.) are listed in [Open questions](../open-questions.md).

## Sources

Synthesis of the concept and guide pages linked above.
