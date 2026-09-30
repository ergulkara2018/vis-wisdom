---
title: The problem with stacked bars and histograms
type: concept
tags: [bar-plots, histograms, position-adjustments, comparison]
sources: [discrete-continuous.Rmd, distributions.Rmd]
updated: 2026-09-30
---

**Rule (book):** stacked bar plots are rarely a good idea, and stacked histograms aren't either. Only the bottom segment starts at 0; every other segment starts at a different point along the axis, so comparing it needs "visual arithmetic". More fill categories make it worse.

## Alternatives, in the order the book offers them

| Plot | Verdict |
|---|---|
| Stacked bars, `fill = year` | hard to compare the 1999 bars (floating baselines) |
| `position = "dodge"` | fixes it for **2** fill values (all bars of a color start at 0); fails with many (10 `trans` levels: hard to remember colors, hard to pull out same-color bars) |
| Facets | better for >2 values ([Faceting strategy](faceting-strategy.md)) |
| Stacked histogram by party | bad — can't read Democrat counts per bin |
| Side-by-side (column) facets of histograms | bad — hard to compare; **vertical** facets (`rows = vars(party)`) are much better |
| Overlaid `geom_freqpoly()` by color | best for 2–3 distributions; use `y = ..density..` if group sizes differ |
| Filled `geom_density(alpha = .5)` | OK with enough data and distinguishable distributions |

The common thread: give each group its own baseline so comparisons are between aligned positions or lengths from a common zero ([Perceptual ranking](perceptual-ranking.md)).

## Related

[Distributions guide](../guides/distributions.md) · [Discrete-continuous guide](../guides/discrete-continuous-relationships.md) · [Bad-to-good catalog](../analyses/bad-to-good-catalog.md)

## Sources

`discrete-continuous.Rmd` — "Color and facets"; `distributions.Rmd` — "Multiple distributions". Summaries: [Discrete-continuous](../sources/discrete-continuous.md), [Distributions](../sources/distributions.md).
