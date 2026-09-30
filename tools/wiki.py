#!/usr/bin/env python3
"""Helper CLI for the Vis Wisdom LLM wiki (stdlib only).

Usage:
    python3 tools/wiki.py lint            mechanical health checks (exit 1 on errors)
    python3 tools/wiki.py search TERMS    ranked keyword search over wiki pages
    python3 tools/wiki.py log [N]         last N log entries (default 5)
    python3 tools/wiki.py stats           page counts by type
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"

TYPE_BY_DIR = {
    "sources": "source",
    "concepts": "concept",
    "guides": "guide",
    "ggplot2": "ggplot2",
    "people": "person",
    "datasets": "dataset",
    "analyses": "analysis",
}
ALLOWED_TYPES = set(TYPE_BY_DIR.values()) | {"meta"}
REQUIRED_KEYS = ("title", "type", "tags", "sources", "updated")
NO_FRONTMATTER = {"index.md", "log.md"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
LOG_HEADER_RE = re.compile(
    r"^## \[\d{4}-\d{2}-\d{2}\] (setup|ingest|query|lint|refactor|schema) \| .+"
)


def pages():
    return sorted(WIKI.rglob("*.md"))


def rel(p):
    return p.relative_to(WIKI).as_posix()


def parse_frontmatter(text):
    """Return (dict, body). Supports `key: value` and inline `[a, b]` lists."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    block, body = text[4:end], text[end + 4:]
    data = {}
    for line in block.splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, _, val = line.partition(":")
        val = val.split("  #")[0].strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key.strip()] = [v.strip() for v in inner.split(",")] if inner else []
        else:
            data[key.strip()] = val
    return data, body


def links_in(text, page):
    """Yield (target_path_or_None, raw_link) for each relative link."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)  # ignore fenced code
    text = re.sub(r"`[^`\n]*`", "", text)  # ignore inline code
    for m in LINK_RE.finditer(text):
        raw = m.group(1)
        if re.match(r"^[a-z]+:", raw) or raw.startswith("#"):
            continue
        target = (page.parent / raw.split("#")[0]).resolve()
        yield target, raw


def cmd_lint():
    errors, warnings = [], []
    all_pages = pages()
    inbound = defaultdict(set)
    index_path = (WIKI / "index.md").resolve()
    index_links = set()

    for p in all_pages:
        text = p.read_text(encoding="utf-8")
        name = rel(p)

        # frontmatter
        if p.name not in NO_FRONTMATTER or p.parent != WIKI:
            fm, _ = parse_frontmatter(text)
            if fm is None:
                errors.append(f"{name}: missing frontmatter")
            else:
                for k in REQUIRED_KEYS:
                    if k not in fm:
                        errors.append(f"{name}: frontmatter missing '{k}'")
                t = fm.get("type")
                if t and t not in ALLOWED_TYPES:
                    errors.append(f"{name}: unknown type '{t}'")
                d = p.parent.name
                if p.parent != WIKI and d in TYPE_BY_DIR and t and t != TYPE_BY_DIR[d]:
                    errors.append(f"{name}: type '{t}' does not match directory '{d}'")
                upd = fm.get("updated", "")
                if upd and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", upd):
                    errors.append(f"{name}: bad 'updated' date '{upd}'")
                for s in fm.get("sources", []) or []:
                    if not (ROOT / s).exists():
                        errors.append(f"{name}: sources entry '{s}' does not exist")

        # links
        for target, raw in links_in(text, p):
            if not target.exists():
                errors.append(f"{name}: broken link '{raw}'")
                continue
            if WIKI in target.parents:
                if p.resolve() == index_path:
                    index_links.add(target)
                elif target != p.resolve():
                    inbound[target].add(p.resolve())

    # index coverage + orphans
    for p in all_pages:
        if p.name in NO_FRONTMATTER and p.parent == WIKI:
            continue
        if p.resolve() not in index_links:
            errors.append(f"{rel(p)}: not listed in index.md")
        if not inbound.get(p.resolve()):
            warnings.append(f"{rel(p)}: orphan (no inbound links from other pages)")

    # log format
    log = WIKI / "log.md"
    if log.exists():
        for i, line in enumerate(log.read_text(encoding="utf-8").splitlines(), 1):
            if line.startswith("## ") and not LOG_HEADER_RE.match(line):
                errors.append(f"log.md:{i}: malformed entry header: {line!r}")

    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\n{len(all_pages)} pages checked: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


def cmd_search(terms):
    if not terms:
        print("usage: wiki.py search TERMS", file=sys.stderr)
        return 2
    words = [w.lower() for t in terms for w in t.split()]
    results = []
    for p in pages():
        text = p.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        fm = fm or {}
        title = fm.get("title", p.stem).lower()
        tags = " ".join(fm.get("tags", [])) if isinstance(fm.get("tags"), list) else ""
        low = body.lower()
        score = 0
        for w in words:
            score += 10 * title.count(w) + 5 * tags.count(w) + low.count(w)
        if score:
            snippet = ""
            for line in body.splitlines():
                if any(w in line.lower() for w in words) and not line.startswith("#"):
                    snippet = line.strip()[:140]
                    break
            results.append((score, rel(p), fm.get("title", p.stem), snippet))
    for score, path, title, snippet in sorted(results, reverse=True)[:15]:
        print(f"{score:4d}  wiki/{path}  —  {title}")
        if snippet:
            print(f"      {snippet}")
    if not results:
        print("no matches")
    return 0


def cmd_log(n):
    log = WIKI / "log.md"
    entries = [l for l in log.read_text(encoding="utf-8").splitlines() if l.startswith("## [")]
    print("\n".join(entries[-n:]))
    return 0


def cmd_stats():
    counts = defaultdict(int)
    for p in pages():
        fm, _ = parse_frontmatter(p.read_text(encoding="utf-8"))
        counts[(fm or {}).get("type", "(no type)")] += 1
    for k, v in sorted(counts.items()):
        print(f"{k:10s} {v}")
    print(f"{'total':10s} {sum(counts.values())}")
    return 0


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd, rest = argv[1], argv[2:]
    if cmd == "lint":
        return cmd_lint()
    if cmd == "search":
        return cmd_search(rest)
    if cmd == "log":
        return cmd_log(int(rest[0]) if rest else 5)
    if cmd == "stats":
        return cmd_stats()
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
