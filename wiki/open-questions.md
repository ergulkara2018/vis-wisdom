---
title: Open questions, gaps and sources to find
type: meta
tags: [open-questions, todo, gaps]
sources: []
updated: 2026-09-30
---

Living list. Resolve an item by ingesting a source or verifying a claim, then move it to the *Resolved* section with the date and log reference.

## Sources worth ingesting (none in `raw/` yet)

1. **Claus Wilke, *Fundamentals of Data Visualization*** (free online) — the book cites it for legend order, size encodings and `stamp()`; likely the richest next source, and covers topics this wiki lacks (color for discrete data, uncertainty, figure design). → [Claus Wilke](people/claus-wilke.md)
2. **Cleveland & McGill (1985)** — verify the ten-item ranking, what "continuous" vs other data types means in the paper, and the exact journal. → [Perceptual ranking](concepts/perceptual-ranking.md)
3. **Cleveland, McGill & McGill (1988)** and **Talbot, Gerth & Hanrahan (2012)** — clarify exactly what "bank to 45" claims and what the replication found (and who the "first" replicating group is). → [Aspect ratio](concepts/aspect-ratio-and-banking.md)
4. **Tufte (2001)** — check the quoted "Compared to what?" passage (p. 74) in context. → [Compared to what?](concepts/compared-to-what.md)
5. **Cleveland, *The Elements of Graphing Data* (1994)** — recommended in the book's welcome, bibliography-only. → [William Cleveland](people/william-cleveland.md)
6. **Current ggplot2 / forcats documentation** — to verify the wiki's modernization notes and the "ggplot2 requires zero for bars" wording. → [Lint](analyses/lint-2026-09-30.md)

## Claims to verify

- [ ] "ggplot2 requires that the numerical axis of a bar plot starts at 0" — wording vs actual behavior. ([Zero baseline](concepts/zero-baseline-for-bars.md))
- [ ] Modern equivalents of deprecated calls used in the book (`..density..`, `spread()`, `top_n()`, `size` for lines, `draw_quantiles`) — labeled *not from the sources*.
- [ ] `cleveland-1985` journal field in `references.bib`.
- [ ] Whether `countries` in `time-series.Rmd` is meant to be `data/gapminder/data/countries.rds`.

## Topics the book does not cover (candidate new pages if sources arrive)

- Color for **discrete** variables / palette choice and colorblind safety beyond viridis (the book only says hue suits discrete variables).
- **Uncertainty** displays beyond `geom_smooth` confidence bands.
- **Maps / spatial** data, **networks**, **proportions/parts-of-whole** (pie vs bar), **ranking/slope charts**.
- **Text and typography**, figure sizing for print vs web, accessibility.
- How the **Cleveland–McGill ranking extends to discrete variables** (the book says it does not apply).

## Questions the wiki could answer next (file answers in `analyses/`)

- A side-by-side of "bar vs dot vs lollipop" for different goals (the book compares bars/dots; `geom_segment` appears for time series and paired data).
- Which of the book's recommendations depend on *data size* (density plots, violins, hex bins, loess vs gam)? A cross-cutting page could collect them.

## Resolved

*(none yet)*
