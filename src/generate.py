"""
M4: End-to-end — retrieve context, stuff it into a prompt, generate an answer.

Usage:
    python src/generate.py --query "What is a p-value?"
"""
import argparse
import sys
sys.path.insert(0, "src")

from provider import get_provider
from retrieve import retrieve

SYSTEM_PROMPT = """You are a statistics course tutor. Answer the student's question using ONLY the
provided course material below. If the material doesn't contain the answer, say so explicitly —
do not guess or use outside knowledge."""


def build_prompt(query: str, chunks: list[dict]) -> str:
    context = "\n\n---\n\n".join(
        f"[Source: {c['source']}]\n{c['text']}" for c in chunks
    )
    return f"""Course material:
{context}

Student question: {query}"""


def answer(query: str, k: int = 5) -> tuple[str, list[dict]]:
    chunks = retrieve(query, k=k)
    prompt = build_prompt(query, chunks)
    provider = get_provider()
    response = provider.complete(system=SYSTEM_PROMPT, user=prompt)
    return response, chunks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    parser.add_argument("--k", type=int, default=5)
    args = parser.parse_args()

    response, chunks = answer(args.query, args.k)

    print("=== Retrieved sources ===")
    for c in chunks:
        print(f"  [{c['score']:.3f}] {c['source']}")

    print("\n=== Answer ===")
    print(response)


if __name__ == "__main__":
    main()