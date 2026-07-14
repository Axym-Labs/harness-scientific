---
name: arxiv
description: Download arXiv paper PDFs or LaTeX sources and search metadata through the official API with the bundled CLI. Use when Codex needs an arXiv paper, source bundle, figures, metadata, author or topic search, or stable programmatic arXiv access.
---

# arXiv

CLI tool for downloading papers and metadata from arXiv using the official API (`export.arxiv.org`). Respects rate limits, uses proper programmatic access channels, and supports PDF, LaTeX source bundles, and metadata retrieval.

## Attribution

This skill and its bundled `arxiv-dl.py` script were created by Tim Scarfe.
The local adaptation changes only packaging, invocation guidance, and metadata
for the curated Harness scientific suite.

> **This is the canonical method for fetching arXiv papers.** Do NOT use Readwise as a proxy for arXiv — use this tool directly. The old Readwise workaround is deprecated.

## Bundled Script

```bash
scripts/arxiv-dl.py --help
```

Treat `scripts/arxiv-dl.py` as an ordinary bundled skill script. It requires no
separate or global installation. The executable uses `uv` and PEP 723 metadata
to resolve and cache its `arxiv` and `requests` dependencies. The examples
below assume the skill directory is the working directory.

## Commands

### Get a Paper

```bash
# Download PDF (default)
scripts/arxiv-dl.py get 2301.07041v1

# Download PDF from a full URL
scripts/arxiv-dl.py get https://arxiv.org/abs/2301.07041v1

# Download LaTeX source bundle
scripts/arxiv-dl.py get 2301.07041v1 -f source

# Download source and extract the tarball
scripts/arxiv-dl.py get 2301.07041v1 -f source --extract

# Download both PDF and source
scripts/arxiv-dl.py get 2301.07041v1 -f both --extract

# Metadata only (no download)
scripts/arxiv-dl.py get 2301.07041v1 -f info

# JSON output (for programmatic use)
scripts/arxiv-dl.py get 2301.07041v1 -f info --json

# Custom output directory and filename
scripts/arxiv-dl.py get 2301.07041v1 -o /tmp/papers --filename attention-paper

# Shorthand: omit "get" subcommand
scripts/arxiv-dl.py 2301.07041v1
```

### Search

```bash
# Basic search
scripts/arxiv-dl.py search transformer attention

# With arXiv query syntax
scripts/arxiv-dl.py search "au:hinton AND cat:cs.LG"
scripts/arxiv-dl.py search "ti:scaling laws"
scripts/arxiv-dl.py search "cat:cs.AI AND ti:reasoning"

# Limit results and sort
scripts/arxiv-dl.py search "au:lecun" -n 5 --sort-by date

# JSON output
scripts/arxiv-dl.py search "cat:cs.CL" -n 20 --json
```

## Input Formats

The `get` command accepts any of these as the paper argument:

| Format | Example |
|--------|---------|
| Bare ID (new) | `2301.07041v1` or `2301.07041` |
| Bare ID (old) | `quant-ph/0201082v1` |
| Abstract URL | `https://arxiv.org/abs/2301.07041v1` |
| PDF URL | `https://arxiv.org/pdf/2301.07041v1` |
| HTML URL | `https://arxiv.org/html/2301.07041v1` |

## Download Formats

| Flag | What it downloads | Default filename |
|------|-------------------|-----------------|
| `-f pdf` (default) | PDF file | `{id}.{sanitized_title}.pdf` |
| `-f source` | LaTeX source tarball (.tar.gz) | `{id}.{sanitized_title}.tar.gz` |
| `-f both` | Both PDF and source | Both patterns |
| `-f info` | Nothing — metadata only | — |

Use `--extract` with `source` or `both` to automatically unpack the tarball into a directory containing individual `.tex`, `.bib`, figure files, etc.

## JSON Output

Add `--json` to any command for machine-readable output. The JSON schema for a paper:

```json
{
  "id": "2301.07041v1",
  "title": "Paper Title",
  "authors": ["Author One", "Author Two"],
  "abstract": "...",
  "published": "2023-01-17T00:00:00+00:00",
  "updated": "2023-01-17T00:00:00+00:00",
  "primary_category": "cs.LG",
  "categories": ["cs.LG", "cs.AI"],
  "comment": "15 pages, 3 figures",
  "journal_ref": null,
  "doi": null,
  "pdf_url": "https://arxiv.org/pdf/2301.07041v1",
  "source_url": "https://arxiv.org/src/2301.07041v1",
  "abs_url": "https://arxiv.org/abs/2301.07041v1",
  "html_url": "https://arxiv.org/html/2301.07041v1"
}
```

## arXiv Query Syntax

For the `search` command, use arXiv's query language:

| Prefix | Field | Example |
|--------|-------|---------|
| `ti:` | Title | `ti:"attention is all you need"` |
| `au:` | Author | `au:hinton` |
| `abs:` | Abstract | `abs:reasoning` |
| `cat:` | Category | `cat:cs.LG` |
| `all:` | All fields | `all:transformer` |

**Operators:** `AND`, `OR`, `ANDNOT`. **Grouping:** parentheses. **Phrases:** double quotes.

**Common CS categories:** `cs.AI`, `cs.LG`, `cs.CL`, `cs.CV`, `cs.NE`, `cs.RO`, `cs.SE`

## Rate Limits & Infrastructure

- Uses `export.arxiv.org` (dedicated programmatic endpoint, not the main site)
- 3-second delay between API requests (arXiv ToS requirement)
- 3 automatic retries on failure
- Downloads also go via `export.arxiv.org` to avoid firewall blocks

## When to Use This Tool

| Scenario | Action |
|----------|--------|
| Need to read/analyse an arXiv paper | `scripts/arxiv-dl.py get <id> -f info --json` for metadata, then download the PDF for full content |
| Gather an author's papers | `scripts/arxiv-dl.py search "au:author-name"` then download key papers |
| Need figures/LaTeX from a paper | `scripts/arxiv-dl.py get <id> -f source --extract` |
| Quick lookup of paper metadata | `scripts/arxiv-dl.py get <id> -f info` |
| Bulk paper search for a topic | `scripts/arxiv-dl.py search "cat:cs.AI AND ti:topic" -n 20 --json` |
