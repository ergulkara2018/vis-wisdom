---
title: Major famines
type: dataset
tags: [dataset, famines, time-series, events]
sources: [data/famines/data.R, time-series.Rmd]
updated: 2026-09-30
---

`famines` — major famines scraped from Our World in Data (<https://ourworldindata.org/famines>; script version 2019-02-05), joined with Gapminder country, region and GDP data. Columns: `start`, `end`, `name` (country), `deaths_estimate` (excess-mortality midpoint), `iso_a3`, `region`, `gdp_per_capita` (famines without a GDP value are dropped).

- **Findings in the book:** deaths and the GDP per capita at which famines occur have not changed much over time.
- **Used for:** *individual values over time* — bubble plot (start date × GDP, size = deaths, fill = region, labels) and `geom_segment()` spans for famine duration with log-scaled deaths → [Time-series guide](../guides/time-series.md), [Perceptual ranking](../concepts/perceptual-ranking.md).

Depends on [Gapminder](gapminder.md) (`gdp_per_capita.rds`, `countries.rds`).

## Sources

`data/famines/data.R`; `time-series.Rmd` — "Individual values". The `.rds` was not opened.
