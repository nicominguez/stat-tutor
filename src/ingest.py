"""
1: Convert raw course PDFs/HTML into plain Markdown files.

Usage:
    python src/ingest.py --in data/raw --out data/markdown
"""
import argparse
from pathlib import Path

import pdfplumber
import trafilatura


def pdf_to_markdown(path: Path) -> str:
    lines = []
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            lines.append(f"<!-- page {i} -->\n{text.strip()}\n")
    return "\n".join(lines)


def html_to_markdown(path: Path) -> str:
    raw_html = path.read_text(encoding="utf-8", errors="ignore")
    md = trafilatura.extract(raw_html, output_format="markdown")
    return md or ""


def convert_file(path: Path) -> str | None:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return pdf_to_markdown(path)
    elif suffix in (".html", ".htm"):
        return html_to_markdown(path)
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="in_dir", default="data/raw")
    parser.add_argument("--out", dest="out_dir", default="data/markdown")
    args = parser.parse_args()

    in_dir = Path(args.in_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    converted, skipped = 0, 0
    for path in sorted(in_dir.iterdir()):
        if not path.is_file():
            continue
        md = convert_file(path)
        if md is None:
            print(f"skip (unsupported type): {path.name}")
            skipped += 1
            continue
        out_path = out_dir / (path.stem + ".md")
        out_path.write_text(md, encoding="utf-8")
        print(f"wrote {out_path}  ({len(md)} chars)")
        converted += 1

    print(f"\nDone. {converted} converted, {skipped} skipped.")


if __name__ == "__main__":
    main()
