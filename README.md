> **Author:** John Mitchell (@whmatrix)
> **Status:** SUPERSEDED (by batch-02)
> **Audience:** Researchers / Learners
> **Environment:** CPU sufficient (pre-built indices included)
> **Fast Path:** See [batch-02 mini-index](https://github.com/whmatrix/semantic-indexing-batch-02/tree/main/mini-index)

> This repository represents early foundational work. For the current production implementation, see [semantic-indexing-batch-02](https://github.com/whmatrix/semantic-indexing-batch-02).

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

## What's Actually In This Repository

### Included
- `portfolio_index_results/` — Pre-built FAISS indices for all 6 datasets
  - Each contains: `chunks.jsonl`, `metadata.jsonl`, `summary.json`, `vectors.index`, `index_info.json`
- Ready to load and query immediately (see "How to Use These Indexes" above)

### Not Included
- Source datasets (publicly available; see dataset documentation)
- Indexing scripts (see [semantic-indexing-batch-02](https://github.com/whmatrix/semantic-indexing-batch-02) for the production pipeline)

### Quickest Proof

This batch is superseded. For a runnable demo, see the [mini-index in batch-02](https://github.com/whmatrix/semantic-indexing-batch-02/tree/main/mini-index):

```bash
git clone https://github.com/whmatrix/semantic-indexing-batch-02
cd semantic-indexing-batch-02/mini-index
pip install sentence-transformers faiss-cpu
python demo_query.py
```

---

## Badges

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![FAISS](https://img.shields.io/badge/FAISS-IndexFlatIP-green.svg)
![Embeddings](https://img.shields.io/badge/Model-e5--large--v2-orange.svg)

---

## Limitations & Non-Claims

This batch provides a foundational semantic index demonstrating the indexing pipeline. It is superseded by [semantic-indexing-batch-02](https://github.com/whmatrix/semantic-indexing-batch-02) (8.35M+ vectors, larger scale). No retrieval quality metrics or benchmarking are provided; this is proof-of-concept infrastructure. Index outputs are not tuned for any specific application domain.

---

## Routing

This repo has been **superseded** by the production portfolio:

- **Current Production**: [semantic-indexing-batch-02](https://github.com/whmatrix/semantic-indexing-batch-02) (8.3M+ vectors)
- **Canonical Protocol**: [Universal Protocol v4.23](https://github.com/whmatrix/universal-protocol-v4.23)

## Protocol Alignment

This indexing run conforms to the
[Universal Protocol v4.23](https://github.com/whmatrix/universal-protocol-v4.23).

All dataset ingestion, chunking, embedding, FAISS construction,
and validation artifacts follow the schemas and constraints defined there.
