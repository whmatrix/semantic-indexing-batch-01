import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Configuration
MODEL_NAME = "intfloat/e5-large-v2"
DATASET = "imdb"  # Change this to test other datasets
INDEX_PATH = f"portfolio_index_results/{DATASET}/vectors.index"
CHUNKS_PATH = f"portfolio_index_results/{DATASET}/chunks.jsonl"

print(f"\nLoading model ({MODEL_NAME})...")
model = SentenceTransformer(MODEL_NAME, device="cuda")

print(f"Loading FAISS index from {INDEX_PATH} ...")
index = faiss.read_index(INDEX_PATH)

# Load chunks
chunks = []
with open(CHUNKS_PATH, "r") as f:
    for line in f:
        chunks.append(json.loads(line))

print(f"Loaded {len(chunks)} chunks.")


def embed_query(text):
    text = "query: " + text
    emb = model.encode([text], convert_to_numpy=True, normalize_embeddings=True)
    return emb.astype("float32")


def search(query, k=5):
    print(f"\nQuery: {query}")
    qv = embed_query(query)
    scores, indices = index.search(qv, k)

    print("\nTop results:")
    for rank, idx in enumerate(indices[0]):
        chunk = chunks[idx]["text"]
        print(f"\n#{rank+1} — Score: {scores[0][rank]:.3f}")
        print(chunk[:500], "...")


if __name__ == "__main__":
    search("movies about heartbreak and betrayal")
    search("reviews describing poorly written scripts")
    search("films with strong female leads")
