"""
M5: Aggregate a scored results file into summary stats.

Usage:
    python src/score_results.py --file eval/results/run_2026-08-28.jsonl
"""
import argparse
import json

RUBRIC_FIELDS = ["relevance", "groundedness", "correctness", "uncertainty_handling", "citation"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    with open(args.file, encoding="utf-8") as f:
        rows = [json.loads(line) for line in f]

    n = len(rows)
    scored = [r for r in rows if r["recall_at_k"] is not None]
    if scored:
        print(f"Retrieval: recall@k={sum(r['recall_at_k'] for r in scored)/len(scored):.2f}  "
              f"MRR={sum(r['mrr'] for r in scored)/len(scored):.2f}  (n={len(scored)}/{n})")

    for field in RUBRIC_FIELDS:
        vals = [r[field] for r in rows if r.get(field) is not None]
        if not vals:
            print(f"{field}: not scored yet")
        else:
            print(f"{field}: avg={sum(vals)/len(vals):.2f}  (n={len(vals)}/{n})")


if __name__ == "__main__":
    main()