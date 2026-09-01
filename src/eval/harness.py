"""
M5: Run the eval set through retrieval + generation. Retrieval metrics (recall@k, MRR)
are computed automatically. Answer-quality rubric fields are left blank for manual scoring.

Usage:
    python src/eval/harness.py --qa eval/qa_set.jsonl --k 5
"""
import argparse
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate import answer
from eval.scorers import ManualScorer #TODO: , LLMJudgeScorer


def recall_and_mrr(retrieved_sources: list[str], gold_source: str) -> tuple[int | None, float | None]:
    if not gold_source:
        return None, None  # trap questions have no gold source to check against
    recall = 1 if gold_source in retrieved_sources else 0
    mrr = 0.0
    for rank, src in enumerate(retrieved_sources, start=1):
        if src == gold_source:
            mrr = 1.0 / rank
            break
    return recall, mrr


def load_qa_set(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def run_eval(qa_items: list[dict], k: int, scorer: AnswerScorer) -> list[dict]:
    rows = []
    for item in qa_items:
        gold_source = item.get("source_file", "")
        response, chunks = answer(item["question"], k=k)
        retrieved_sources = [c["source"] for c in chunks]
        recall, mrr = recall_and_mrr(retrieved_sources, gold_source)

        row = {
            "question_id": item["id"],
            "question": item["question"],
            "gold_answer": item.get("gold_answer", ""),
            "gold_source": gold_source,
            "tags": item.get("tags", []),
            "retrieved_sources": retrieved_sources,
            "recall_at_k": recall,
            "mrr": round(mrr, 3) if mrr is not None else None,
            "model_answer": response,
        }
        row.update(scorer.score(row))
        rows.append(row)
        print(f"[{item['id']}] recall@{k}={recall}  mrr={mrr}")
    return rows


def write_results(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")


def print_retrieval_summary(rows: list[dict], k: int) -> None:
    scored = [r for r in rows if r["recall_at_k"] is not None]
    if scored:
        avg_recall = sum(r["recall_at_k"] for r in scored) / len(scored)
        avg_mrr = sum(r["mrr"] for r in scored) / len(scored)
        print(f"\nRetrieval baseline (excl. trap questions): recall@{k}={avg_recall:.2f}  MRR={avg_mrr:.2f}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--qa", default="eval/qa_set.jsonl")
    parser.add_argument("--out", default=None)
    parser.add_argument("--k", type=int, default=5)
    args = parser.parse_args()

    out_path = Path(args.out or f"eval/results/run_{date.today().isoformat()}.jsonl")

    qa_items = load_qa_set(args.qa)
    scorer = ManualScorer()   # swap for LLMJudgeScorer(get_provider()) later — see scorers.py TODO
    rows = run_eval(qa_items, k=args.k, scorer=scorer)
    write_results(rows, out_path)

    print_retrieval_summary(rows, k=args.k)
    print(f"Wrote {len(rows)} rows to {out_path}")
    print("Rubric fields are blank — score by hand next (see score_results.py).")


if __name__ == "__main__":
    main()