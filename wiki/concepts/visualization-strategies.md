---
title: Four strategies for every visualization
type: concept
tags: [strategy, process, goals]
sources: [general-strategy.Rmd, discrete-continuous.Rmd]
updated: 2026-09-30
---

Perception knowledge is "only one tool in your toolbox". The book gives four practical strategies that apply to *all* visualizations (later chapters add strategies for specific plot types).

1. **Set goals.** Goals force you to think about a plot's purpose and let you *evaluate* it. EDA goals are questions; presentation goals are specific information to convey. Goals also narrow scope — data sets have more interesting features than one plot can show. Example: the two [discrete-continuous goals](../guides/discrete-continuous-relationships.md) (connect categories to numbers; compare numbers) used to judge every Utah-languages plot.
2. **Go for quantity.** Make many plots per goal; ggplot2/RStudio make this cheap. In EDA each plot is a slightly different window into the data; in presentation it frees you from committing too early and lets you compare approaches. To grow your stockpile of ideas: make visualizations, *consume* many, and scan the geoms section of the cheat sheet.
3. **Look at your plots.** Notice your reactions: what's easy to see, what jumps out, what's obscured? Practice noticing weaknesses even when you can't fix them yet. Imagine seeing the plot for the first time — decoding may succeed for you (after staring all day) and fail for newcomers. Example: a country-vs-height strip doesn't reveal "China has the most tall buildings"; a bar count of buildings per country does.
4. **Iterate.** The first attempt is almost never the best; fix problems, emphasize the relationships you want. It takes time — step away and return.

## Related

[EDA vs presentation](eda-vs-presentation-plots.md) · [Encoding and decoding](encoding-and-decoding.md) · [Bad-to-good catalog](../analyses/bad-to-good-catalog.md) (iteration in action) · [Derived variables](derived-variables.md)

## Sources

`general-strategy.Rmd` — "Strategies"; `discrete-continuous.Rmd` — "One discrete category". Summary: [General strategy](../sources/general-strategy.md).
