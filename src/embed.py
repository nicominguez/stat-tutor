"""
Embed chunks with a local model, store as a NumPy array + aligned metadeta.

Usage:
    python src/embed.py --in data/chunks.chunks.jsonl --out data/embeddings
"""
import argparse
import json
import time
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"


def load_chunks(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="in_dir", default="data/chunks/chunks.jsonl")
    parser.add_argument("--out", dest="out_dir", default="data/embeddings")
    args = parser.parse_args()

    in_dir = Path(args.in_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    chunks = load_chunks(in_dir)
    texts = [c["text"] for c in chunks]

    print(f"Loading {MODEL_NAME}...")
    model = SentenceTransformer(MODEL_NAME)

    print(f"Embedding {len(texts)} chunks...")
    t0 = time.time()
    vectors = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    elapsed = time.time() - t0

    # vectors: shape (num_chunks, embedding_dim), float32
    np.save(out_dir / "vectors.npy", vectors.astype("float32"))

    # metadata is stored separately, index-aligned with vectors.npy row i <-> metadata[i]
    metadata = [{"id": c["id"], "source": c["source"], "text": c["text"]} for c in chunks]
    with (out_dir / "metadata.jsonl").open("w", encoding="utf-8") as f:
        for m in metadata:
            f.write(json.dumps(m) + "\n")

    with (out_dir / "info.json").open("w", encoding="utf-8") as f:
        json.dump({
            "model": MODEL_NAME,
            "num_chunks": len(texts),
            "dim": int(vectors.shape[1]),
            "elapsed_sec": round(elapsed, 2),
        }, f, indent=2)

    print(f"Saved {vectors.shape[0]} vectors, dim={vectors.shape[1]}, took {elapsed:.1f}s")
    print(f"-> {out_dir/'vectors.npy'}")
    print(f"-> {out_dir/'metadata.jsonl'}")


if __name__ == "__main__":
    main()