---
title: Congress 2019 ages
type: dataset
tags: [dataset, congress, distributions]
sources: [data/congress/data.R, distributions.Rmd]
updated: 2026-09-30
---

`congress_2019` — members of the US Congress serving in 2019, built from `theunitedstates.io` legislator JSON (script version 2018-01-26). Columns: `name`, `state`, `division` (US Census division), `chamber` (House/Senate), `party` (top two parties, others lumped as "Other"), `age`, `gender`.

- `age` = age (in years, 2 decimals) at the start of the member's term.
- The script's comment notes 534 rows at the time (one vacancy) and excludes non-voting members from territories (no division).
- **Findings in the book:** mean and median ≈ 58–59; House marginally younger than Senate; youngest members under 32; oldest is 85; Democrats more spread out and slightly older than Republicans; divisions have similar medians but different shapes.
- **Used for:** histograms, frequency polygons, densities, boxplots and violins — [Distributions guide](../guides/distributions.md), [Bin width](../concepts/bin-width.md), [Mean vs median](../concepts/mean-vs-median.md), [Summary vs detail](../concepts/summary-vs-detail.md).

## Sources

`data/congress/data.R`; `distributions.Rmd`. The `.rds` was not opened.
