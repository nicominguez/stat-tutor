"""
M4: Brute-force cosine similarity retrieval over the saved embeddings.

Usage (standalone test):
    python src/retrieve.py --query "What is a p-value?" --k 5
"""
import argparse
import json
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"  # must match what embed.py used


def load_index(embeddings_dir: Path):
    vectors = np.load(embeddings_dir / "vectors.npy")
    metadata = []
    with (embeddings_dir / "metadata.jsonl").open(encoding="utf-8") as f:
        for line in f:
            metadata.append(json.loads(line))
    return vectors, metadata


def cosine_top_k(query_vec: np.ndarray, vectors: np.ndarray, k: int):
    # Normalize so a plain dot product equals cosine similarity
    query_norm = query_vec / np.linalg.norm(query_vec)
    matrix_norm = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)
    scores = matrix_norm @ query_norm  # shape (num_chunks,)
    top_idx = np.argsort(-scores)[:k]  # highest score first
    return [(int(i), float(scores[i])) for i in top_idx]


def retrieve(query: str, embeddings_dir: str = "data/embeddings", k: int = 5, model=None):
    embeddings_dir = Path(embeddings_dir)
    vectors, metadata = load_index(embeddings_dir)

    if model is None:
        model = SentenceTransformer(MODEL_NAME)
    query_vec = model.encode([query], convert_to_numpy=True)[0]

    results = []
    for idx, score in cosine_top_k(query_vec, vectors, k):
        results.append({**metadata[idx], "score": score})
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    parser.add_argument("--embeddings", default="data/embeddings")
    parser.add_argument("--k", type=int, default=5)
    args = parser.parse_args()

    results = retrieve(args.query, args.embeddings, args.k)
    for r in results:
        preview = r["text"][:120].replace("\n", " ")
        print(f"[{r['score']:.3f}] {r['source']} :: {preview}...")


if __name__ == "__main__":
    main()