# Vis Wisdom

This repository contains the source for the book [Vis Wisdom](https://bookdown.org/content/2138/).

We welcome suggestions for improvements.

* Small matters, such as typos, can be submitted through pull requests.
* Larger matters can be submitted through issues.

## LLM wiki

This repository also contains an LLM-maintained knowledge base about the book's ideas (visualization "wisdom" plus ggplot2 mechanics), following the "LLM Wiki" pattern (the LLM incrementally builds and maintains a structured, interlinked markdown wiki between you and your raw sources).

* Start at [`wiki/overview.md`](wiki/overview.md) or browse [`wiki/index.md`](wiki/index.md).
* [`CLAUDE.md`](CLAUDE.md) is the schema: how the wiki is structured and the ingest / query / lint workflows an LLM agent follows.
* The book's chapters, `references.bib` and `data/` are the immutable raw sources; new sources go in [`raw/`](raw/).
* `python3 tools/wiki.py lint` checks links, frontmatter, index coverage and orphans.
