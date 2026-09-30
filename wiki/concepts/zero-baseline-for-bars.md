---
title: Bars need a zero baseline; dots don't
type: concept
tags: [bars-vs-dots, truthful-graphics, length-vs-position]
sources: [discrete-continuous.Rmd]
updated: 2026-09-30
---

**Rule (book):** a bar plot's numeric axis must start at 0, because viewers judge and compare bar *lengths*, and lengths only encode the values accurately when measured from 0. A dot plot encodes values by *position*, so its axis may start anywhere.

## Demonstration

Values a=2, b=4, c=8 (each twice the previous). With a baseline at 0 the bar lengths keep the 1:2 relationships. Start the axis at 1 and a's bar has length 1 while b's has length 3 — the relationship is lost.

## Choosing between bars and dots

| Want to emphasize | Use |
|---|---|
| Values relative to zero / total magnitude | bars (`geom_col`) |
| Values relative to each other, differences in a tight range | dots (`geom_point`), axis fitted to the data |

Example: Utah languages — bars and dots both work (x-axis of the dot plot starts near 1250); 100 m final — dots reveal the race ([Compared to what?](compared-to-what.md)).

This connects to the [perceptual ranking](perceptual-ranking.md): position along a common scale (dots) outranks length (bars).

## Caveat recorded by the wiki

The book says "ggplot2 *requires* that the numerical axis of a bar plot starts at 0". The principle is the book's; the enforcement claim has not been checked against ggplot2 documentation — see [lint 2026-09-30](../analyses/lint-2026-09-30.md).

## Related

[Ordering categories](ordering-categories.md) · [Discrete-continuous guide](../guides/discrete-continuous-relationships.md)

## Sources

`discrete-continuous.Rmd` — "Bars vs. dots". Summary: [Discrete-continuous](../sources/discrete-continuous.md).
