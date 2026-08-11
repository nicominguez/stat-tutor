"""
2: Split markdown files into fixed-size, overlapping chunks.

Usage:
    python src/chunk.py --in data/markdown --out data/chunks/chunk.jsonl --size 500 --overlap 50
"""
import argparse
import json
from pathlib import Path

import tiktoken

ENC = tiktoken.get_encoding("cl100k_base")

def chunk_text(text: str, size: int, overlap: int):
    """
    Yields (chunk_text, token_start, token_end).
    """
    tokens = ENC.encode(text)
    start = 0
    while start < len(tokens):
        end = min(start + size, len(tokens))
        yield ENC.decode(tokens[start:end]), start, end
        if end == len(tokens):
            break
        start = end - overlap

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="in_dir", default="data/markdown")
    parser.add_argument("--out", dest="out_dir", default="data/chunks/chunks.jsonl")
    parser.add_argument("--size", type=int, default=500)
    parser.add_argument("--overlap", type=int, default=50)
    args = parser.parse_args()
    
    in_dir = Path(args.in_dir)
    out_path = Path(args.out_dir)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    count = 0
    with out_path.open("w", encoding="utf-8") as out_f:
        for md_path in sorted(in_dir.glob("*.md")):
            text = md_path.read_text(encoding="utf-8")
            for chunk_str, tok_start, tok_end in chunk_text(text, args.size, args.overlap):
                record = {
                    "id": f"{md_path.stem}_{tok_start:06d}",
                    "source": md_path.name,
                    "text": chunk_str,
                    "token_start": tok_start,
                    "token_end": tok_end,
                }
                out_f.write(json.dumps(record) + "\n")
                count += 1

    print(f"Wrote {count} chunks to {out_path}")


if __name__ == "__main__":
    main()