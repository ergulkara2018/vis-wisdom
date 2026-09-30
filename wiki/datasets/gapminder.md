---
title: Gapminder (life expectancy, GDP per capita, population)
type: dataset
tags: [dataset, gapminder, countries, time-series]
sources: [data/gapminder/README.md, continuous-continuous.Rmd, time-series.Rmd]
updated: 2026-09-30
---

The book's workhorse data, from [Gapminder.org](https://www.gapminder.org/) (CC BY 4.0). Files under `data/gapminder/data/`:

| File | Content |
|---|---|
| `combined_1950-2015_5yr.rds` → `gapminder` | population, GDP per capita, life expectancy for **183 countries every 5 years, 1950–2015**; columns used: `iso_a3`, `name`, `region`, `year`, `life_expectancy`, `gdp_per_capita`, `population` |
| `life_expectancy.rds` | country life expectancy, 1800–2100 (used in Time series, joined to regions) |
| `gdp_per_capita.rds` | GDP per capita, constant PPP dollars, 1800–2040 |
| `population.rds` | population, 1800–2100 |
| `countries.rds` | ISO alpha-3 code, name, regions (`region_gm4`, `region_gm8`), UN status, World Bank income |

## Used for

- Life expectancy vs GDP: log scale, hex bins, smooths, paired 2010–2015, three-variable bubble plot (2015) — [Continuous-continuous guide](../guides/continuous-continuous-relationships.md), [Paired data](../concepts/paired-data.md), [Log scales](../concepts/log-scales.md).
- Life expectancy over time, South Africa and neighbors, Africa by sub-region — [Time-series guide](../guides/time-series.md). Also the source of region/GDP for [Famines](famines.md).
- The bubble plots follow the Gapminder visualizations and Hans Rosling's well-known demonstration (linked in the chapter).

Note: the Time series chapter uses `countries` without loading it — see [lint 2026-09-30](../analyses/lint-2026-09-30.md).

## Sources

`data/gapminder/README.md`, `data/gapminder/scripts/`; `continuous-continuous.Rmd`; `time-series.Rmd`. The `.rds` files were not opened.
