import os

from models.model_loader import load_embedding_model
from embeddings.embedding_generator import generate_embeddings
from search.semantic_search import SemanticSearch
from clustering.document_clustering import cluster_documents

# -------- FIXED PATH --------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "data", "sample_documents.txt")

# Load documents
with open(data_path, "r") as f:
    documents = [line.strip() for line in f.readlines()]

# Load model
model = load_embedding_model()

# Generate embeddings
embeddings = generate_embeddings(model, documents)

# Semantic search
search_engine = SemanticSearch(embeddings)

query = "AI applications"
query_embedding = model.encode(query)

results = search_engine.search(query_embedding, documents)

print("\nSemantic Search Results:\n")

for r in results:
    print(r)

# Clustering
clusters = cluster_documents(embeddings, documents)

print("\nDocument Clusters:\n")

for cluster, docs in clusters.items():
    print(f"\nCluster {cluster}")
    for d in docs:
        print("-", d)