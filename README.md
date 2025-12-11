[✔️ Live Project](https://github.com/whmatrix/semantic-indexing-batch-01)

**661,525 vectors · 6 datasets · e5-large-v2 · FAISS IndexFlatIP**

---

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

## Tech Stack

- **Python**
- **CUDA / PyTorch (FP16 inference)**
- **FAISS (IndexFlatIP)**
- **e5-large-v2 encoder**
- **JSONL pipelines (chunks, metadata, summaries)**

## Project Overview

This project demonstrates a complete semantic indexing pipeline optimized for large-scale text datasets. Each dataset moves through a consistent sequence of steps:

1. **Data Cleaning** – Normalize text, strip markup, handle encoding, remove noise.
2. **Chunking** – Split documents into 512–800 token segments with metadata preservation.
3. **Embedding** – Generate vector representations using the `intfloat/e5-large-v2` model in FP16 mode, GPU-accelerated.
4. **Indexing** – Build FAISS `IndexFlatIP` indexes for fast semantic search and retrieval.
5. **Verification** – Validate vector counts, dimensions, and metadata alignment.

### Deliverables

Each dataset includes:

- `chunks.jsonl` – segmented text chunks  
- `metadata.jsonl` – metadata for each chunk  
- `summary.json` – dataset-level stats and notes  
- `vectors.index` – FAISS vector index  
- `index_info.json` – counts, dimensions, and integrity checks  

This project is designed as a portfolio artifact demonstrating reliability, reproducibility, and clean engineering practices for preparing large datasets, generating embeddings, and producing RAG-ready indexes.
