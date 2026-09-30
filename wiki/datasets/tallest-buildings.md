---
title: Tallest buildings
type: dataset
tags: [dataset, wikipedia, general-strategy]
sources: [data/tallest-buildings/data.R, general-strategy.Rmd]
updated: 2026-09-30
---

`buildings` — the world's tallest buildings, scraped from Wikipedia's *List of tallest buildings* (script version 2018-01-08, authors Sara Altman & Bill Behrman). `buildings_10` is the top 10 by `height_ft` (`top_n(10, height_ft)`).

- **Variables used in the book:** `building`, `height_ft`, `floors`, `country`.
- **Used for:** the encoding/perception examples — position vs length vs color vs size for height; `floors` as area; `height_ft / floors` ratio exposing Tianjin CTF Finance Centre and Lotte World Tower; a country strip plot vs a count bar plot showing China has the most tall buildings.
- **Findings stated:** Burj Khalifa is tallest by several hundred feet.

→ [Perceptual ranking](../concepts/perceptual-ranking.md) · [Derived variables](../concepts/derived-variables.md) · [Visualization strategies](../concepts/visualization-strategies.md) · [General strategy source](../sources/general-strategy.md)

## Sources

`data/tallest-buildings/data.R` (provenance); chapter usage in `general-strategy.Rmd`. The `.rds` was not opened (no R in the maintenance environment).
