# stat-tutor

A RAG pipeline built by hand, end-to-end, to learn how the pieces work. Acts as a tutor for a statistics course, answering student questions using the course's own material (PDFs/HTML converted to Markdown), with retrieval, generation, and evaluation all implemented from scratch.

Runs against a **local Ollama model** or **Azure OpenAI**, switched via one config value — no code changes.

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in Azure keys as needed
ollama pull llama3.2:3b   # or whatever's in configs/default.yaml
```

## Provider

`src/provider.py` is the single seam between local and hosted inference. Everything else in the pipeline calls `get_provider()` and never knows which backend it's talking to.

```yaml
# configs/default.yaml
provider: local   # or: azure

local:
  model: llama3.2:3b   # must match `ollama list`

azure:
  deployment: null      # set once Azure is configured
```

Secrets (Azure API key) live in `.env` (never committed); non-secret config (which provider, which model) lives in `configs/default.yaml` (committed).

## Pipeline

Each stage is a standalone script, one input artifact, one output artifact — run independently or chained.

| Stage | Script | In → Out | What it does |
|---|---|---|---|
| **Ingest** | `src/ingest.py` | `data/raw/*.pdf,.html` → `data/markdown/*.md` | Converts source docs to Markdown. PDFs go through Marker (handles LaTeX math and figures); HTML through trafilatura. |
| **Chunk** | `src/chunk.py` | `data/markdown/*.md` → `data/chunks/chunks.jsonl` | Splits Markdown into fixed-size, overlapping, token-counted chunks. |
| **Embed** | `src/embed.py` | `chunks.jsonl` → `data/embeddings/vectors.npy` + `metadata.jsonl` | Embeds each chunk locally (`sentence-transformers/all-MiniLM-L6-v2`). No network calls after the model is cached. |
| **Retrieve** | `src/retrieve.py` | query → top-k chunks | Brute-force cosine similarity in NumPy over the saved vectors — no vector DB, written by hand to see the math. |
| **Generate** | `src/generate.py` | query → answer | Retrieves context, builds a prompt instructing the model to answer only from provided material (and say so if it can't), calls the active provider. |

Quickstart:
```bash
python src/ingest.py --in data/raw --out data/markdown
python src/chunk.py --in data/markdown --out data/chunks/chunks.jsonl
python src/embed.py --in data/chunks/chunks.jsonl --out data/embeddings
python src/generate.py --query "What is a p-value?"
```

## Evaluation

`eval/qa_set.jsonl` holds 15–20 hand-written question/gold-answer/source-file rows pulled from the actual syllabus (including a few "trap" questions with no answer in the material, to test abstention).

`src/eval/harness.py` runs every question through retrieve → generate and scores two things separately:

- **Automatic — retrieval quality:** `recall@k` (was the right source retrieved at all) and `MRR` (how highly ranked), computed directly against `qa_set.jsonl`'s gold source file.
- **Manual — answer quality:** relevance, groundedness, correctness, uncertainty handling, citation — scored 0–2 by hand via a CSV round-trip (`src/eval/convert_results.py`), since these require judgment an automated check can't yet make reliably.

```bash
python src/eval/harness.py --qa eval/qa_set.jsonl
python src/eval/convert_results.py to-csv --file eval/results/run_YYYY-MM-DD.jsonl
# score the CSV by hand, then:
python src/eval/convert_results.py to-jsonl --file eval/results/run_YYYY-MM-DD.csv
```

## TODO

- **Tools:** wire in web search and R code execution (`src/tools/`) as callable functions, routed by keyword for now — not yet an agentic decision (the model doesn't choose whether to call them).
- **Pre-query check:** rewrite vague/ambiguous student questions into a sharper retrieval query before retrieval runs.
- **Post-answer check:** a critic pass that checks the draft answer against retrieved chunks for faithfulness, and revises or flags low-confidence answers.
- **LLM-judge scorer:** automate the manual rubric half of evaluation, validated against a human-scored sample.
