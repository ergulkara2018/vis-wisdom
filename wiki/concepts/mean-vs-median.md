---
title: Mean vs median
type: concept
tags: [statistics, robustness, reference-lines]
sources: [distributions.Rmd]
updated: 2026-09-30
---

"Average" is ambiguous. The mean is the sum divided by the count and is sensitive to outliers; the median is the midpoint and is robust.

Book's demonstration: `x <- c(1, 2, 10, 15)` has mean 7 and median 6 (close). Append `1e6` and the mean explodes while the median only increases by a small amount.

**Convention in the book:** use **medians** for averages and reference lines. Congress 2019: mean and median ages are both between 58 and 59, so the hypothesis "average age ≈ 60" was close; the House is marginally younger than the Senate by median.

Summary statistics (`summary()`, `group_by() %>% summarize(median_age = median(age))`) are useful for asking questions, but visualizing the distribution gives a richer picture ([Summary vs detail](summary-vs-detail.md)). Median reference lines: [Layering and reference lines](layering-and-reference-lines.md). Boxplots show the median by construction.

## Related

[Distributions guide](../guides/distributions.md) · [Congress 2019](../datasets/congress-2019.md)

## Sources

`distributions.Rmd` — "One distribution". Summary: [Distributions](../sources/distributions.md).
