# Semantic Indexing Batch 01

This repository contains the final indexing outputs for 6 open datasets,
processed with a GPU-based pipeline using the `intfloat/e5-large-v2` model
and FAISS `IndexFlatIP`.

All datasets were:

- cleaned and normalized
- chunked into 512–800 token segments
- embedded in FP16 with batch_size=1300
- indexed into FAISS for semantic search

## Datasets

The `portfolio_index_results/` directory contains one folder per dataset:

- `20_newsgroups/`
- `simplewiki/`
- `imdb/`
- `stackoverflow/`
- `ag_news/`
- `disaster_tweets/`

Each dataset folder has:

- `chunks.jsonl` – text chunks
- `metadata.jsonl` – per-document or per-chunk metadata
- `summary.json` – high-level stats and notes
- `vectors.index` – FAISS index
- `index_info.json` – counts, dimensions, and verification info

Total: **661,525 vectors** across 6 datasets.

This repo is mainly a portfolio artifact showing that I can take real-world
text datasets from raw form to a clean, verified, RAG-ready index with
consistent structure.
