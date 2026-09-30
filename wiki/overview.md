---
title: Overview — the wiki's current synthesis
type: meta
tags: [overview, synthesis]
sources: []
updated: 2026-09-30
---

*Status: built from one body of sources — the Vis Wisdom book (7 chapters + front matter + bibliography + data scripts). Nothing external has been ingested yet. Revise this page whenever a new source shifts the picture.*

## The thesis in one paragraph

A visualization is a code. You **encode** data into visual elements and the viewer must **decode** them; the plot succeeds only if decoding works ([Encoding and decoding](concepts/encoding-and-decoding.md)). Humans decode some encodings far more accurately than others, so the most important variables should get the top of the [Cleveland–McGill ranking](concepts/perceptual-ranking.md) — position, then length — and lower-ranked channels (area, color) only when forced. Everything else in the book is a consequence of that idea plus a few working habits: know whether you're making an [EDA or a presentation plot](concepts/eda-vs-presentation-plots.md), and [set goals, make many plots, look with fresh eyes, iterate](concepts/visualization-strategies.md).

## Five recurring moves

1. **Give every comparison a shared baseline** — sorted bars, dodged not stacked, vertical facets, bars from zero (or dots when differences matter) ([Stacking problem](concepts/stacking-problem.md), [Zero baseline](concepts/zero-baseline-for-bars.md), [Faceting strategy](concepts/faceting-strategy.md)).
2. **Ask "compared to what?"** — reference lines, neighbors, `y = x` ([Compared to what?](concepts/compared-to-what.md), [Layering and reference lines](concepts/layering-and-reference-lines.md)).
3. **Tame density and scale** — log scales, hex/alpha, binwidth, smooths ([Log scales](concepts/log-scales.md), [Overplotting](concepts/overplotting.md), [Smoothing](concepts/smoothing.md)).
4. **Make decoding direct** — order, direct labels, legend next to data ([Ordering categories](concepts/ordering-categories.md), [Direct labeling](concepts/direct-labeling-and-legends.md)).
5. **Compute the quantity you care about** instead of stacking encodings ([Derived variables](concepts/derived-variables.md), [Paired data](concepts/paired-data.md)).

## Where to go

- *I have a data shape; what do I plot?* → [Choosing a plot](guides/choosing-a-plot.md), then the guides: [discrete-continuous](guides/discrete-continuous-relationships.md), [distributions](guides/distributions.md), [continuous-continuous](guides/continuous-continuous-relationships.md), [time series](guides/time-series.md).
- *How do I do it in ggplot2?* → [Plot template](ggplot2/plot-template.md) and the [ggplot2 pages](index.md#ggplot2-mechanics).
- *What does the book show going wrong?* → [Bad-to-good catalog](analyses/bad-to-good-catalog.md).
- *What is uncertain?* → [Open questions](open-questions.md) and [Lint 2026-09-30](analyses/lint-2026-09-30.md).

## Caveats

- The book's empirical claims about perception come from 1985–2012 studies summarized in the text; the originals are not yet in `raw/` and one key result (banking to 45) is reported as not replicated ([Aspect ratio](concepts/aspect-ratio-and-banking.md)).
- The book covers a deliberately small set of situations — no maps, networks, uncertainty displays, or discrete color palettes ([Open questions](open-questions.md)).
- The book's code is 2019-era tidyverse; see the [lint notes](analyses/lint-2026-09-30.md).
