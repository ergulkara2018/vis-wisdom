---
title: "Source: Book build configuration and data scripts"
type: source
tags: [build, bookdown, data, infrastructure]
sources: [_bookdown.yml, _common.R, _output.yml, DESCRIPTION, .travis.yml, data/gapminder/README.md]
updated: 2026-09-30
---

The non-prose files that define how the book is built and where its example data comes from. Useful as provenance for the [dataset pages](../datasets/gapminder.md).

## Build

- **Chapter order** (`_bookdown.yml` `rmd_files`): index → ggplot2-basics → discrete-continuous → general-strategy → distributions → continuous-continuous → time-series → references. `new_session: true`, so each chapter runs in a fresh R session; `_common.R` runs before each chapter.
- **`_common.R`:** sets `set.seed(2466)`, printing options, knitr chunk defaults (golden-ratio `fig.asp = 0.618`, `cache = TRUE`, centered, `fig.show = "hold"`), and defines **`stamp(tag = "Bad", tag_color = "#B33A3A", ...)`** — a ggplot2 layer list that puts a red tag in the top-right of a plot (idea credited to Wilke's book). It is how the book flags poor example plots. See the [bad-to-good catalog](../analyses/bad-to-good-catalog.md).
- **Output:** `bookdown::gitbook`, split by Rmd, edit links to `dcl-docs/vis-wisdom`.
- **CI:** `.travis.yml` renders with `bookdown::render_book("index.Rmd")` and deploys `_book` to Netlify. `DESCRIPTION` lists imports (bookdown, ggrepel, hexbin, knitr, rmarkdown, tidyverse).

## Data

Each `data/<name>/data.R` is a reproducible script (authors Sara Altman & Bill Behrman) that fetches the raw data and writes an `.rds` file. Provenance per data set is on the dataset pages: [tallest buildings](../datasets/tallest-buildings.md), [Olympic 100 m](../datasets/olympics-100m.md), [US languages](../datasets/us-languages.md), [Congress 2019](../datasets/congress-2019.md), [Gapminder](../datasets/gapminder.md), [word frequencies](../datasets/word-frequencies.md), [wheat prices](../datasets/wheat-prices.md), [famines](../datasets/famines.md).

## Related

[Welcome source](welcome.md) · [References source](references-bib.md)

## Sources

`_bookdown.yml`, `_common.R`, `_output.yml`, `DESCRIPTION`, `.travis.yml`, `data/*/data.R`, `data/gapminder/README.md`.
