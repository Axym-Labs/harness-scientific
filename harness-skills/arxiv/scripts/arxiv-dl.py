#!/usr/bin/env -S uv run --script
# Created by Tim Scarfe; packaged locally in the curated scientific skill suite.
# /// script
# requires-python = ">=3.11"
# dependencies = ["arxiv>=2.1", "requests"]
# ///
"""arxiv-dl — Download papers and metadata from arXiv.

Uses the official arXiv API via export.arxiv.org with proper rate limiting.
"""

import argparse
import json
import os
import re
import sys
import tarfile
import textwrap
from datetime import timezone
from pathlib import Path

import arxiv


def parse_arxiv_id(raw: str) -> str:
    """Extract a bare arXiv ID from a URL or bare ID string."""
    raw = raw.strip()
    # Full URL patterns
    for pattern in [
        r"arxiv\.org/abs/(.+?)(?:\?|#|$)",
        r"arxiv\.org/pdf/(.+?)(?:\.pdf)?(?:\?|#|$)",
        r"arxiv\.org/html/(.+?)(?:\?|#|$)",
        r"arxiv\.org/src/(.+?)(?:\?|#|$)",
    ]:
        m = re.search(pattern, raw)
        if m:
            return m.group(1)
    # Already a bare ID (new format: 2301.07041v1, old format: quant-ph/0201082v1)
    if re.match(r"^(\d{4}\.\d{4,5}(v\d+)?|[a-z-]+/\d{7}(v\d+)?)$", raw):
        return raw
    return raw  # pass through and let the API error


def result_to_dict(r: arxiv.Result) -> dict:
    """Convert an arxiv.Result to a serialisable dict."""
    return {
        "id": r.get_short_id(),
        "title": r.title,
        "authors": [a.name for a in r.authors],
        "abstract": r.summary,
        "published": r.published.astimezone(timezone.utc).isoformat(),
        "updated": r.updated.astimezone(timezone.utc).isoformat(),
        "primary_category": r.primary_category,
        "categories": r.categories,
        "comment": r.comment,
        "journal_ref": r.journal_ref,
        "doi": r.doi,
        "pdf_url": r.pdf_url,
        "source_url": _source_url(r),
        "abs_url": r.entry_id,
        "html_url": f"https://arxiv.org/html/{r.get_short_id()}",
    }


def _source_url(r: arxiv.Result) -> str | None:
    """Derive source URL from pdf_url."""
    if r.pdf_url:
        return r.pdf_url.replace("/pdf/", "/src/")
    return None


def print_info(r: arxiv.Result, as_json: bool = False) -> None:
    """Print paper metadata."""
    d = result_to_dict(r)
    if as_json:
        print(json.dumps(d, indent=2))
    else:
        authors = ", ".join(d["authors"][:5])
        if len(d["authors"]) > 5:
            authors += f" (+{len(d['authors']) - 5} more)"
        cats = ", ".join(d["categories"])
        print(f"  ID:         {d['id']}")
        print(f"  Title:      {d['title']}")
        print(f"  Authors:    {authors}")
        print(f"  Published:  {d['published'][:10]}")
        print(f"  Categories: {cats}")
        if d["comment"]:
            print(f"  Comment:    {d['comment']}")
        if d["journal_ref"]:
            print(f"  Journal:    {d['journal_ref']}")
        if d["doi"]:
            print(f"  DOI:        {d['doi']}")
        print(f"  PDF:        {d['pdf_url']}")
        print(f"  HTML:       {d['html_url']}")
        print(f"  Abstract:   {textwrap.shorten(d['abstract'], width=200)}")


def download_pdf(r: arxiv.Result, outdir: str, filename: str | None) -> str:
    """Download PDF. Returns path."""
    fname = filename if filename else ""
    path = r.download_pdf(dirpath=outdir, filename=fname)
    return path


def download_source(r: arxiv.Result, outdir: str, filename: str | None, extract: bool = False) -> str:
    """Download source tarball. Returns path."""
    fname = filename if filename else ""
    path = r.download_source(dirpath=outdir, filename=fname)
    if extract:
        extract_dir = Path(path).with_suffix("").with_suffix("")  # strip .tar.gz
        extract_dir.mkdir(parents=True, exist_ok=True)
        try:
            with tarfile.open(path, "r:gz") as tf:
                tf.extractall(path=extract_dir, filter="data")
            print(f"  Extracted:  {extract_dir}/")
        except tarfile.TarError:
            print(f"  Note: Source is not a tar.gz (may be a single .tex file)")
            # Move the file as-is
            single = extract_dir / "main.tex"
            extract_dir.mkdir(parents=True, exist_ok=True)
            Path(path).rename(single)
            print(f"  Saved as:   {single}")
    return path


def cmd_get(args: argparse.Namespace) -> int:
    """Fetch a paper by ID/URL."""
    arxiv_id = parse_arxiv_id(args.paper)
    client = arxiv.Client(delay_seconds=3, num_retries=3)
    search = arxiv.Search(id_list=[arxiv_id])

    try:
        result = next(client.results(search))
    except StopIteration:
        print(f"Error: Paper not found: {arxiv_id}", file=sys.stderr)
        return 1

    outdir = args.output or "."
    os.makedirs(outdir, exist_ok=True)

    fmt = args.format
    fname = args.filename

    if fmt == "info":
        print_info(result, as_json=args.json)
        return 0

    # Always show info first
    if not args.json:
        print_info(result)
        print()

    paths = {}
    if fmt in ("pdf", "both"):
        pdf_name = f"{fname}.pdf" if fname else None
        path = download_pdf(result, outdir, pdf_name)
        paths["pdf"] = path
        if not args.json:
            print(f"  Downloaded: {path}")

    if fmt in ("source", "both"):
        src_name = f"{fname}.tar.gz" if fname else None
        path = download_source(result, outdir, src_name, extract=args.extract)
        paths["source"] = path
        if not args.json:
            print(f"  Downloaded: {path}")

    if args.json:
        out = result_to_dict(result)
        out["downloaded"] = paths
        print(json.dumps(out, indent=2))

    return 0


def cmd_search(args: argparse.Namespace) -> int:
    """Search arXiv by query."""
    client = arxiv.Client(delay_seconds=3, num_retries=3)

    sort_map = {
        "relevance": arxiv.SortCriterion.Relevance,
        "date": arxiv.SortCriterion.SubmittedDate,
        "updated": arxiv.SortCriterion.LastUpdatedDate,
    }
    sort_by = sort_map.get(args.sort_by, arxiv.SortCriterion.Relevance)

    search = arxiv.Search(
        query=args.query,
        max_results=args.max_results,
        sort_by=sort_by,
        sort_order=arxiv.SortOrder.Descending,
    )

    results = list(client.results(search))
    if not results:
        print("No results found.", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps([result_to_dict(r) for r in results], indent=2))
    else:
        for i, r in enumerate(results, 1):
            authors = ", ".join(a.name for a in r.authors[:3])
            if len(r.authors) > 3:
                authors += " et al."
            print(f"  {i:>2}. [{r.get_short_id()}] {r.title}")
            print(f"      {authors} ({r.published.strftime('%Y-%m-%d')}) [{r.primary_category}]")
            if i < len(results):
                print()

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="arxiv-dl",
        description="Download papers and metadata from arXiv via the official API.",
    )
    sub = parser.add_subparsers(dest="command")

    # --- get ---
    p_get = sub.add_parser("get", help="Fetch a paper by arXiv ID or URL")
    p_get.add_argument("paper", help="arXiv ID (e.g. 2301.07041v1) or full URL")
    p_get.add_argument("-o", "--output", default=".", help="Output directory (default: current dir)")
    p_get.add_argument("-f", "--format", choices=["pdf", "source", "both", "info"], default="pdf",
                       help="What to download: pdf (default), source (LaTeX bundle), both, or info (metadata only)")
    p_get.add_argument("--filename", help="Custom filename stem (without extension)")
    p_get.add_argument("--extract", action="store_true", help="Extract source tarball after download")
    p_get.add_argument("--json", action="store_true", help="Machine-readable JSON output")

    # --- search ---
    p_search = sub.add_parser("search", help="Search arXiv by query")
    p_search.add_argument("query", nargs="+", help="Search query (arXiv query syntax)")
    p_search.add_argument("-n", "--max-results", type=int, default=10, help="Max results (default: 10)")
    p_search.add_argument("--sort-by", choices=["relevance", "date", "updated"], default="relevance",
                          help="Sort criterion (default: relevance)")
    p_search.add_argument("--json", action="store_true", help="Machine-readable JSON output")

    # If first non-flag arg isn't a subcommand, assume "get"
    if len(sys.argv) > 1 and sys.argv[1] not in ("get", "search", "-h", "--help"):
        sys.argv.insert(1, "get")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 0

    if args.command == "search":
        args.query = " ".join(args.query)

    handler = {"get": cmd_get, "search": cmd_search}
    return handler[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
