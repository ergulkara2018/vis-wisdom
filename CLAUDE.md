# CLAUDE.md — schema for the Vis Wisdom LLM wiki

This repository is two things at once:

1. The source of the bookdown book **Vis Wisdom** (R Markdown chapters, `data/`, build config).
2. An **LLM-maintained wiki** (`wiki/`) that compiles what the book — and any sources added later — teaches about effective data visualization with ggplot2.

You (the LLM) are the wiki's maintainer. The human curates sources and asks questions; you do the summarizing, cross-referencing, filing and bookkeeping. The pattern is the "LLM Wiki" idea: *the wiki is a persistent, compounding artifact* — knowledge is compiled once and kept current, not re-derived on every question.

## The three layers

| Layer | Where | Who writes it | Rules |
|---|---|---|---|
| **Raw sources** | Book chapters `index.Rmd`, `ggplot2-basics.Rmd`, `general-strategy.Rmd`, `discrete-continuous.Rmd`, `distributions.Rmd`, `continuous-continuous.Rmd`, `time-series.Rmd`, `references.Rmd`; `references.bib`; `_common.R`; `_bookdown.yml`; `data/**`; and everything under `raw/` | Humans | **Immutable for wiki work.** Read, never edit. The book files stay in place because the bookdown build needs them. New external sources (articles, papers, notes, clipped pages) go in `raw/`. |
| **The wiki** | `wiki/**` | You | You own this layer entirely. Humans read it. |
| **The schema** | This file | You + human, co-evolved | Update it when a workflow or convention changes. |

**Book edits are a separate job.** If the human explicitly asks to change the book (fix a typo, repair code), that is ordinary repo work, not wiki work. After such an edit, re-check the affected wiki pages (see *Keeping in sync*).

## Directory layout

```
CLAUDE.md                 this schema
raw/                      new immutable sources (+ raw/README.md)
raw/assets/               downloaded images for raw sources
tools/wiki.py             lint / search / log helper (stdlib-only Python 3)
wiki/
  index.md                content catalog — read this first when answering
  log.md                  append-only chronological record
  overview.md             the evolving top-level synthesis
  open-questions.md       gaps, contradictions, sources worth finding
  sources/                one summary page per raw source
  concepts/               ideas and principles ("visualization wisdom")
  guides/                 plot-type hubs + decision guides, built from concepts
  ggplot2/                ggplot2 mechanics (functions, arguments, recipes)
  people/                 researchers and authors whose work the wiki relies on
  datasets/               data sets used in examples
  analyses/               filed query answers, catalogs, lint reports
```

Add a new directory only when a new page *type* appears; document it here and in `index.md`.

## Page conventions

- **Filenames:** lowercase kebab-case, `.md`. A page's filename is its permanent id.
- **Frontmatter (required on every page except `log.md` and `index.md`):**
  ```yaml
  ---
  title: Human-readable title
  type: source | concept | guide | ggplot2 | person | dataset | analysis | meta
  tags: [short, lowercase, tags]
  sources: [general-strategy.Rmd, references.bib]   # raw files this page draws on; [] for pure syntheses
  updated: 2026-09-30                                # date of last substantive edit
  ---
  ```
- **Shape of a page:** a one-or-two-sentence summary first, then sections, then `## Related` (links) and `## Sources` (raw file + chapter/section, and the link to the source summary page).
- **Links:** standard relative markdown links, e.g. `[Overplotting](../concepts/overplotting.md)`. They render on GitHub and in Obsidian. No wikilinks.
- **Every page must be linked from `index.md`** and should have at least one inbound link from another page (no orphans).
- **Provenance:** state what the sources say; attribute claims to their origin (the book, or a researcher the book cites). Anything *you* add from outside the sources — general knowledge, inference, a judgment — must be visibly marked, e.g. *"Not from the sources: …"* or *"Note (wiki):"*, and ideally also logged in `open-questions.md` until verified. Never invent citations, figures, or ggplot2 behavior.
- **Contradictions and staleness:** when a new source disagrees with an existing page, do not silently overwrite. Record both claims, say which source says what, and add an entry to `open-questions.md`.
- **Tone:** plain, concise, specific. Prefer a table or a short list when it is clearer than prose. Keep code snippets to the minimum that shows the idea.
- **The book's voice:** the book uses "we" and "you"; wiki pages should describe it in the third person ("the book recommends…").

## Operations

### Ingest (adding a source)

1. Put the file in `raw/` (book chapters already live in the repo root). Read it fully.
2. Discuss key takeaways with the human if they want to stay in the loop; otherwise proceed.
3. Write `wiki/sources/<slug>.md`: what the source is, its main claims, structure, examples/data used, concepts it touches, and any problems noticed.
4. Create or update the affected pages — concepts, guides, ggplot2 pages, people, datasets. A single source typically touches 5–15 pages. Merge new claims into existing pages instead of duplicating them.
5. Add every new page to `wiki/index.md`; revise `wiki/overview.md` if the synthesis shifted.
6. Flag contradictions / gaps in `wiki/open-questions.md`.
7. Append a log entry (see below).
8. Run `python3 tools/wiki.py lint` and fix what it reports.

### Query (answering questions)

1. Read `wiki/index.md`, then the relevant pages (follow links). Use `python3 tools/wiki.py search "<terms>"` if the index is not enough.
2. Answer with citations to wiki pages (and through them to raw sources). Say clearly when the wiki does not cover something.
3. **File good answers back.** If the answer is a comparison, catalog, decision table, or new connection worth keeping, save it as `wiki/analyses/<slug>.md` (or fold it into an existing guide), add it to the index, and log it as `query`. Do not leave durable insight only in chat.

### Lint (health check)

Run `python3 tools/wiki.py lint` (mechanical checks: broken links, orphans, pages missing from the index, frontmatter, stale `sources:` paths). Then do the judgment checks by hand:

- contradictions between pages; claims superseded by newer sources;
- concepts mentioned on several pages but lacking their own page;
- missing cross-references; thin or stale pages;
- wiki pages whose raw source changed since `updated:` (compare with `git log -- <raw file>`);
- data gaps a new source or a web search could fill.

Write the findings to `wiki/analyses/lint-<YYYY-MM-DD>.md`, fix the cheap issues immediately, put the rest in `open-questions.md`, and log it as `lint`.

## index.md and log.md

**`wiki/index.md`** — catalog, organized by directory/category. One line per page: `- [Title](path) — one-line summary`. Update it on every ingest and whenever a page is added, renamed or removed.

**`wiki/log.md`** — append-only, newest at the bottom. Every entry starts with a parseable header:

```
## [YYYY-MM-DD] <op> | <title>
```

`<op>` is one of `setup`, `ingest`, `query`, `lint`, `refactor`, `schema`. Under the header, a few bullets: pages created/updated, notable findings. Never rewrite old entries. Recent history: `python3 tools/wiki.py log 5` (or `grep "^## \[" wiki/log.md | tail -5`).

## Keeping in sync

- The wiki's source pages were written from the book as of the commit named in their log entry. If a raw file changes, re-ingest it: diff, update the source page, propagate to concepts/guides, log it as `ingest` (re-ingest).
- Code in the book uses the tidyverse/ggplot2 APIs of roughly 2019 (e.g. `..density..`, `spread()`, `top_n()`). The wiki records *what the book says and does*; modern equivalents are labelled as not-from-the-sources notes until verified.

## Repo hygiene

- `wiki/`, `raw/`, `tools/` and this file are excluded from the R package/build via `.Rbuildignore`; `_bookdown.yml` lists chapters explicitly, so wiki markdown is never rendered into the book.
- Commit wiki changes with clear messages (`wiki: ingest <source>`, `wiki: lint`, …). The wiki is just a git repo of markdown files — history is the audit trail.
