---
title: Continuous color scales
type: concept
tags: [color, scales, viridis, sequential, diverging]
sources: [continuous-continuous.Rmd, general-strategy.Rmd]
updated: 2026-09-30
---

Two kinds of continuous color scale in the book:

| Kind | Functions | Use when |
|---|---|---|
| **Sequential** | `scale_color_gradient()` / `scale_fill_gradient()` (default: low = dark blue → high = light blue); set `low`, `high`; **viridis**: `scale_*_viridis_c()` | one direction of magnitude |
| **Diverging** | `scale_color_gradient2()` / `scale_fill_gradient2()`; `low`, `mid`, `high`; `midpoint` (default 0) | you want to encode *both sign and magnitude* (e.g. temperature above/below freezing) |

- Viridis was designed to be **colorblind-friendly** and is "generally better than the default blue scale"; `_c` = continuous, `_d` = discrete. A common pairing: `geom_hex()` + `scale_fill_viridis_c()` — the strong contrast makes counts easier to decode ([Overplotting](overplotting.md)).
- `scale_*_gradient()` maps the data minimum to `low` and maximum to `high`.

## Caution

Color is at the bottom of the [perceptual ranking](perceptual-ranking.md) (saturation 9th, hue 10th) for continuous variables: height encoded by color made two buildings look identical. Use color scales when position is taken (e.g. counts in hex bins) or a rough impression suffices; color *hue* is better suited to discrete variables (region).

## Related

[Scales](../ggplot2/scales.md)

## Sources

`continuous-continuous.Rmd` — "Continuous color scales"; `general-strategy.Rmd` — color example. Summary: [Continuous-continuous](../sources/continuous-continuous.md).
