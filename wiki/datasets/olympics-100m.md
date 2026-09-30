---
title: 2016 Olympics men's 100 m final
type: dataset
tags: [dataset, wikipedia, sprint]
sources: [data/olympics-2016/data.R, discrete-continuous.Rmd, general-strategy.Rmd]
updated: 2026-09-30
---

`sprint_times` — the results table for the men's 100 metres final at the 2016 Summer Olympics, scraped from Wikipedia (script version 2018-12-31). The script keeps `lane`, `reaction`, `time` (numeric), adds `rank`, and drops `notes`; the book's plots use `name` and `time`.

- **Used for:** the canonical bars-vs-dots comparison. Bars (from 0) say "everyone ran ~10 s"; dots reveal a couple of runners behind, a pack in the middle, Bolt far ahead. Also reused in General strategy to contrast encodings (length vs position).
- **Concepts:** [Compared to what?](../concepts/compared-to-what.md) · [Zero baseline](../concepts/zero-baseline-for-bars.md) · [Encoding and decoding](../concepts/encoding-and-decoding.md)

## Sources

`data/olympics-2016/data.R`; `discrete-continuous.Rmd` — "Bars vs. dots"; `general-strategy.Rmd`. The `.rds` was not opened.
