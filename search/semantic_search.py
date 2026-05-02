import faiss
import numpy as np

class SemanticSearch:

    def __init__(self, embeddings):
        self.embeddings = embeddings
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

    def search(self, query_embedding, documents, top_k=5):

        query_embedding = np.array([query_embedding])

        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            results.append(documents[idx])

        return results