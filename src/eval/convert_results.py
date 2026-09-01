"""
Convert eval results between JSONL (what harness.py writes/reads) and CSV
(what's actually usable for manual rubric scoring in a spreadsheet).

Usage:
    python src/eval/convert_results.py to-csv --file eval/results/run_2026-08-28.jsonl
    # ...score by hand in the spreadsheet...
    python src/eval/convert_results.py to-jsonl --file eval/results/run_2026-08-28.csv
"""
import argparse
from pathlib import Path

import pandas as pd


def to_csv(jsonl_path: Path) -> Path:
    csv_path = jsonl_path.with_suffix(".csv")
    pd.read_json(jsonl_path, lines=True).to_csv(csv_path, index=False)
    return csv_path


def to_jsonl(csv_path: Path) -> Path:
    jsonl_path = csv_path.with_suffix(".jsonl")
    pd.read_csv(csv_path).to_json(jsonl_path, orient="records", lines=True)
    return jsonl_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("direction", choices=["to-csv", "to-jsonl"])
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    fn = to_csv if args.direction == "to-csv" else to_jsonl
    out = fn(Path(args.file))
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()