# raw/ — immutable sources

Drop new source documents here (clipped web articles as markdown, paper PDFs, notes, data files). The LLM reads from this folder but **never edits** files in it.

The book's own chapters are also raw sources, but they live in the repo root because the bookdown build needs them there; see `CLAUDE.md` for the full list.

- Put downloaded images in `raw/assets/` (Obsidian: set *Attachment folder path* to `raw/assets/`).
- Suggested naming: `YYYY-MM-DD-short-title.md` (date = date you added it).
- To process a source, tell the LLM: *"ingest raw/<file>"*. The workflow is in `CLAUDE.md` → *Ingest*.

Sources worth adding (mentioned in the book, none ingested yet): Claus Wilke's *Fundamentals of Data Visualization*, Cleveland & McGill (1985), Cleveland's *The Elements of Graphing Data*, Tufte's *The Visual Display of Quantitative Information*, Talbot et al. (2012). See `wiki/open-questions.md`.
