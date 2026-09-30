---
title: Wheat prices (real, 1850–2017)
type: dataset
tags: [dataset, commodities, time-series]
sources: [data/wheat-prices/data.R, time-series.Rmd]
updated: 2026-09-30
---

`wheat_prices` — yearly real wheat prices from the dataset accompanying *"From Boom to Bust: A Typology of Real Commodity Prices in the Long Run"* (NBER Working Paper 18874; spreadsheet "Real commodity prices, 1850–2017"; script version 2019-02-06). Columns: `year`, `product` ("wheat"), `price`. (The script renames the spreadsheet's year column, headed `(1900=100)`, which suggests an index with 1900 = 100 — not stated in the book; units are not given in the chapter.)

- **Used for:** data with *two trend types* — a cycle plus a long-term decline. Aspect ratio decides which shows; loess reveals only the long-term trend → [Aspect ratio and banking](../concepts/aspect-ratio-and-banking.md), [Smoothing](../concepts/smoothing.md), [Time-series guide](../guides/time-series.md).

## Sources

`data/wheat-prices/data.R`; `time-series.Rmd` — "Multiple trend-types". The `.rds` was not opened.
