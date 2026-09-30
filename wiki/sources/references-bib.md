---
title: "Source: References (references.bib, references.Rmd)"
type: source
tags: [bibliography, citations]
sources: [references.bib, references.Rmd]
updated: 2026-09-30
---

The book's bibliography: nine BibTeX entries. `references.Rmd` only emits a "References" heading in HTML output; the list itself is generated from `references.bib`.

## Entries and where they are cited

| Key | Work | Cited in |
|---|---|---|
| `cleveland-1985` | Cleveland & McGill, *Graphical Perception and Graphical Methods for Analyzing Scientific Data* (1985) | General strategy (×3), Continuous-continuous |
| `cleveland-1988` | Cleveland, McGill & McGill, *The Shape Parameter of a Two-Variable Graph*, JASA (1988) | Time series |
| `cleveland-1993` | Cleveland, *A Model for Studying Display Methods of Statistical Graphics*, JCGS (1993) | *not cited in any chapter* |
| `cleveland-1994` | Cleveland, *The Elements of Graphing Data*, 2nd ed. (1994) | *not cited in any chapter* (mentioned by link in Welcome) |
| `talbot-2012` | Talbot, Gerth & Hanrahan, *An Empirical Model of Slope Ratio Comparisons* (2012) | Time series |
| `tufte-2001` | Tufte, *The Visual Display of Quantitative Information*, 2nd ed. (2001) | Discrete-continuous (p. 74) |
| `wickham-2010` | Wickham, *A Layered Grammar of Graphics*, JCGS (2010) | ggplot2 basics |
| `wickham-2016` | Wickham, *ggplot2: Elegant Graphics for Data Analysis* (2016) | *not cited in any chapter* |
| `wilke-2019` | Wilke, *Fundamentals of Data Visualization* (2019) | Continuous-continuous (×2) |

Person pages: [Cleveland](../people/william-cleveland.md) · [Talbot et al.](../people/talbot-gerth-hanrahan.md) · [Tufte](../people/edward-tufte.md) · [Wickham](../people/hadley-wickham.md) · [Wilke](../people/claus-wilke.md).

## Notes

- Three entries are unused by the chapters, and the `cleveland-1985` journal field reads "American Association for the Advancement of Science" — see [lint 2026-09-30](../analyses/lint-2026-09-30.md).
- None of the cited works is in `raw/` yet; the wiki relies on the book's description of them. See [Open questions](../open-questions.md).

## Sources

`references.bib`, `references.Rmd`; citation usage found by searching the chapters for `@key`.
