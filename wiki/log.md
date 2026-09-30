# Wiki log

Append-only. Newest at the bottom. Entry header format: `## [YYYY-MM-DD] <op> | <title>`. Recent: `python3 tools/wiki.py log 5`.

## [2026-09-30] setup | Create the LLM wiki scaffolding

- Added `CLAUDE.md` (schema: layers, conventions, ingest/query/lint workflows), `raw/` (for future immutable sources), `tools/wiki.py` (lint/search/log/stats), and `wiki/` with `index.md`, `log.md`, `overview.md`, `open-questions.md`.
- Decision: the book's chapters, `references.bib`, `_common.R` and `data/` stay in place as the immutable raw layer (the bookdown build needs them there). Wiki markdown is excluded from the R build via `.Rbuildignore`.

## [2026-09-30] ingest | Vis Wisdom book (chapters, bibliography, build, data scripts)

- Sources ingested: `index.Rmd`, `ggplot2-basics.Rmd`, `general-strategy.Rmd`, `discrete-continuous.Rmd`, `distributions.Rmd`, `continuous-continuous.Rmd`, `time-series.Rmd`, `references.bib`/`references.Rmd`, `_common.R`/`_bookdown.yml`/data scripts.
- Created: 9 source pages, 22 concept pages, 5 guides (4 plot-type hubs + decision table), 8 ggplot2 pages, 5 people pages, 9 dataset pages, 1 analysis (bad-to-good catalog).
- Notable: the book's core is the encode/decode + Cleveland–McGill ranking; four strategies; ~30 "bad plot → fix" pairs cataloged.
- Flagged: undefined objects and text/code mismatches in `time-series.Rmd`; uncited bibliography entries; an unverified "ggplot2 requires zero for bars" claim; 2019-era API usage. See the lint entry below.

## [2026-09-30] lint | First lint pass

- Wrote [lint-2026-09-30](analyses/lint-2026-09-30.md): 10 source-file findings, wiki-level tensions and gaps.
- Cleaned wording in a few pages; added open questions (sources to ingest, claims to verify).
- Ran `python3 tools/wiki.py lint`.
