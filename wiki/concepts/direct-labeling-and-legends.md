---
title: Direct labeling and legends
type: concept
tags: [legends, labels, decoding, color]
sources: [continuous-continuous.Rmd, time-series.Rmd]
updated: 2026-09-30
---

Decoding a color-coded plot means connecting each mark to a legend entry — a back-and-forth the book works to minimize, in increasing order of effectiveness:

1. **Order the legend to match the lines.** Legend order should match the order of the lines (attributed to Wilke 2019): `scale_color_discrete(breaks = c("Europe", "Americas", "Asia", "Africa"))`.
2. **Move the legend near the data.** `theme(legend.justification = "top")` puts it at the top, closer to the lines.
3. **Label directly and delete the legend.** Text at the line ends (`geom_text()` on the last year's rows, `nudge_x`, extra x-range via `coord_cartesian(xlim = ...)`) plus `guides(color = "none")`. The book says directly labeling lines is even easier than a well-ordered legend.
4. **Label only what matters.** `ggrepel::geom_text_repel()` labels selected outliers (Haiti, Syria, Libya in the paired life-expectancy plot; famine names) without overlap.

Also: too many colors defeat the legend — nine-colored frequency polygons by census division were unusable, so the book switched to boxplots ([Summary vs detail](summary-vs-detail.md)). And a path plot (`geom_path()`) needs year labels at inflection points to be decoded ([Time-series guide](../guides/time-series.md)).

## Related

[Annotations and labels](../ggplot2/annotations-and-labels.md) · [Encoding and decoding](encoding-and-decoding.md) · [Claus Wilke](../people/claus-wilke.md)

## Sources

`continuous-continuous.Rmd` — "Smoothing", "Paired data"; `time-series.Rmd` — "Trends". Note: the prose in `time-series.Rmd` says `geom_text_repel()` but the shown code uses `geom_text()` (see [lint 2026-09-30](../analyses/lint-2026-09-30.md)).
