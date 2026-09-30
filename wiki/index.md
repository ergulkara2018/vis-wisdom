# Vis Wisdom wiki — index

Catalog of every page. Start with the [overview](overview.md); see `../CLAUDE.md` for how this wiki is maintained. Last updated 2026-09-30. Page counts: `python3 tools/wiki.py stats`.

## Top level

- [Overview](overview.md) — the current synthesis: the book's thesis, five recurring moves, where to go
- [Open questions](open-questions.md) — gaps, unverified claims, sources to ingest next
- [Log](log.md) — chronological record of ingests, queries and lint passes

## Guides (by situation)

- [Choosing a plot](guides/choosing-a-plot.md) — cross-chapter decision table: goal → what to try → what to avoid
- [Discrete-continuous relationships](guides/discrete-continuous-relationships.md) — amounts per category: flip, sort, bars vs dots, two categories
- [Distributions](guides/distributions.md) — histograms, freqpolys, densities, boxplots, violins; one vs many groups
- [Continuous-continuous relationships](guides/continuous-continuous-relationships.md) — scatterplots, overplotting, smoothing, paired data, three variables
- [Time series](guides/time-series.md) — trends, cycles, fluctuations, individual events; testing hypotheses by comparison

## Concepts (visualization wisdom)

- [EDA plots vs presentation plots](concepts/eda-vs-presentation-plots.md) — two purposes, two workflows
- [Encoding and decoding](concepts/encoding-and-decoding.md) — a plot succeeds only if decoding works
- [Perceptual ranking (Cleveland–McGill)](concepts/perceptual-ranking.md) — ten encodings from position to hue
- [Four strategies for every visualization](concepts/visualization-strategies.md) — set goals, quantity, look, iterate
- ["Compared to what?"](concepts/compared-to-what.md) — Tufte's question; bars vs dots on the 100 m final
- [Bars need a zero baseline; dots don't](concepts/zero-baseline-for-bars.md) — length vs position
- [Ordering categories](concepts/ordering-categories.md) — sort by the plotted amount
- [Overplotting](concepts/overplotting.md) — hex bins, alpha, shape 21, geom_count
- [The problem with stacked bars and histograms](concepts/stacking-problem.md) — floating baselines; dodge, facet, overlay
- [Faceting strategy](concepts/faceting-strategy.md) — compare within panels; more-valued variable on axis; align
- [Aspect ratio and banking to 45°](concepts/aspect-ratio-and-banking.md) — slope perception; a heuristic, not a rule
- [Direct labeling and legends](concepts/direct-labeling-and-legends.md) — reduce back-and-forth decoding
- [Log scales](concepts/log-scales.md) — orders of magnitude and power laws
- [Layering and reference lines](concepts/layering-and-reference-lines.md) — draw references under the data
- [Summary vs detail in distribution plots](concepts/summary-vs-detail.md) — histogram → density → violin → boxplot
- [Derived variables beat multi-encoding](concepts/derived-variables.md) — compute the quantity you care about
- [Grammar of graphics](concepts/grammar-of-graphics.md) — the eight plot elements
- [Mean vs median](concepts/mean-vs-median.md) — prefer medians
- [Continuous color scales](concepts/color-scales.md) — sequential, diverging, viridis
- [Paired data](concepts/paired-data.md) — scatter + y = x, difference, segments
- [Smoothing](concepts/smoothing.md) — loess vs gam, when to show only smooths
- [Bin width](concepts/bin-width.md) — choose it deliberately

## ggplot2 mechanics

- [Plot code template and style](ggplot2/plot-template.md) — pipe-first, recommended element order
- [Geoms used in the book](ggplot2/geoms.md) — every geom, with the book's advice
- [Scales used in the book](ggplot2/scales.md) — log, color, size, date/time
- [Coordinate systems](ggplot2/coordinate-systems.md) — cartesian, fixed, flip; zooming
- [Facets](ggplot2/facets.md) — `vars()` syntax
- [Theme](ggplot2/theme.md) — element functions; angled labels; legend position
- [Factors with forcats](ggplot2/forcats.md) — `fct_reorder`, `fct_infreq`, `fct_rev`
- [Annotations and labels](ggplot2/annotations-and-labels.md) — `labs`, `annotate`, `ggrepel`, `guides`

## Sources

- [Welcome (index.Rmd)](sources/welcome.md) — scope, audience, how to read the book
- [ggplot2 basics](sources/ggplot2-basics.md) — R4DS on-ramp, pipes, facets, grammar
- [General strategy](sources/general-strategy.md) — goals, encoding/decoding, perception, strategies
- [Discrete-continuous relationships](sources/discrete-continuous.md) — coords, bar plots, bars vs dots, two categories
- [Distributions](sources/distributions.md) — layering, theme, one and many distributions
- [Continuous-continuous relationships](sources/continuous-continuous.md) — scales, overplotting, smoothing, paired data, bubbles
- [Time series](sources/time-series.md) — date scales, banking, trends, fluctuations, events
- [References (references.bib)](sources/references-bib.md) — nine entries and where each is cited
- [Book build and data scripts](sources/book-build-and-data.md) — chapter order, `stamp()`, data provenance

## People

- [William S. Cleveland (and McGill)](people/william-cleveland.md) — graphical perception, bank to 45
- [Edward R. Tufte](people/edward-tufte.md) — "Compared to what?"
- [Claus O. Wilke](people/claus-wilke.md) — legend order, size encodings, `stamp()`
- [Hadley Wickham](people/hadley-wickham.md) — ggplot2, grammar of graphics, R4DS
- [Talbot, Gerth, Hanrahan](people/talbot-gerth-hanrahan.md) — non-replication of banking to 45

## Datasets

- [Tallest buildings](datasets/tallest-buildings.md) — encodings, `height/floors`
- [2016 Olympics men's 100 m final](datasets/olympics-100m.md) — bars vs dots
- [US languages spoken at home](datasets/us-languages.md) — Utah bar-plot example
- [Congress 2019 ages](datasets/congress-2019.md) — distributions
- [Gapminder](datasets/gapminder.md) — life expectancy, GDP, population
- [War and Peace word frequencies](datasets/word-frequencies.md) — power law
- [Wheat prices](datasets/wheat-prices.md) — cycle + long-term trend
- [Famines](datasets/famines.md) — individual events over time
- [Built-in and package data sets](datasets/builtin-r-datasets.md) — `mpg`, `diamonds`, `flights`

## Analyses (filed answers and reports)

- [Catalog of the book's bad plots and their fixes](analyses/bad-to-good-catalog.md) — ~30 problem → fix pairs
- [Lint report 2026-09-30](analyses/lint-2026-09-30.md) — source-file problems and wiki gaps
