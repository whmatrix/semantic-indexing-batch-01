[✔️ Live Project](https://github.com/whmatrix/semantic-indexing-batch-01)

**661,525 vectors · 6 datasets · e5-large-v2 · FAISS IndexFlatIP**

---

# Semantic Indexing Batch 01

This repository contains the final indexing outputs for 6 open datasets, processed with a GPU-based pipeline using the `intfloat/e5-large-v2` model and FAISS `IndexFlatIP`.

All datasets were cleaned and normalized, chunked into 512–800 token segments, embedded in FP16 with batch_size=1300, and indexed into FAISS for semantic search.

## Datasets

The `portfolio_index_results/` directory contains one folder per dataset:

- `20_newsgroups/`
- `simplewiki/`
- `imdb/`
- `stackoverflow/`
- `ag_news/`
- `disaster_tweets/`

Each dataset folder includes:  
`chunks.jsonl`, `metadata.jsonl`, `summary.json`, `vectors.index`, `index_info.json`

Total: **661,525 vectors** across 6 datasets.

## Tech Stack

- **Python**
- **CUDA / PyTorch (FP16 inference)**
- **FAISS (IndexFlatIP)**
- **e5-large-v2 encoder**
- **JSONL pipelines**

## Project Overview

A complete semantic indexing pipeline for large-scale text datasets. Each dataset moves through:  
cleaning → chunking → embedding → indexing → verification.

## Deliverables

- `chunks.jsonl`  
- `metadata.jsonl`  
- `summary.json`  
- `vectors.index`  
- `index_info.json`

## Pipeline Diagram

```
Raw Text
   ↓
Cleaning & Normalization
   ↓
Chunking (512–800 tokens)
   ↓
Embedding (e5-large-v2 · FP16 · GPU)
   ↓
Vector Index (FAISS IndexFlatIP)
   ↓
Verification & Stats
   ↓
RAG-Ready Dataset
```

## Repository Structure

```
portfolio_index_results/
 ├── 20_newsgroups/
 ├── ag_news/
 ├── disaster_tweets/
 ├── imdb/
 ├── simplewiki/
 └── stackoverflow/
```

## How to Use These Indexes

```python
import faiss
index = faiss.read_index("vectors.index")
```

## Badges

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![FAISS](https://img.shields.io/badge/FAISS-IndexFlatIP-green.svg)
![Embeddings](https://img.shields.io/badge/Model-e5--large--v2-orange.svg)
