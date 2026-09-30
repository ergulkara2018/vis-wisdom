---
title: Smoothing
type: concept
tags: [trends, geom_smooth, loess, scatterplots]
sources: [continuous-continuous.Rmd, time-series.Rmd]
updated: 2026-09-30
---

`geom_smooth()` adds a smooth trend line with a shaded confidence band (wider band = more uncertainty; widest at the extremes of GDP per capita in the book's example).

## Method choice

- Default: `gam` (generalized additive model) for more than 1000 points, `loess` (locally estimated scatterplot smoothing) for fewer, because loess can be computationally infeasible for big data.
- The book's advice: unless you have a very large amount of data, **`method = "loess"`** is usually better (smoother line).

## When to use

- Use a smooth when you care about a trend that isn't obvious without one.
- Show **only** smooth lines when you care more about trends than individual values, want several trends on one plot, or have more data than one plot can show. Points + per-region smooths was "even worse" (can't distinguish lines over points); smooths alone revealed different regional trends.
- Drop the confidence band (`se = FALSE`) only if it is small and constant along the whole line.
- Smoothing picks the trend it can see: on wheat prices, loess shows only the long-term decline, not the cycle ([Time-series guide](../guides/time-series.md)). For "distributions over time" a smooth over alpha-faded individual lines summarizes many countries (but hid the southern-Africa dip).

## Related

[Overplotting](overplotting.md) · [Direct labeling and legends](direct-labeling-and-legends.md) (ordering smooth-line legends) · [Geoms](../ggplot2/geoms.md)

## Sources

`continuous-continuous.Rmd` — "Smoothing"; `time-series.Rmd` — "Distributions over time", "Multiple trend-types". Summary: [Continuous-continuous](../sources/continuous-continuous.md).
