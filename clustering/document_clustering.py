from sklearn.cluster import KMeans

def cluster_documents(embeddings, documents, num_clusters=3):

    kmeans = KMeans(n_clusters=num_clusters)
    labels = kmeans.fit_predict(embeddings)

    clustered_docs = {}

    for i, label in enumerate(labels):
        if label not in clustered_docs:
            clustered_docs[label] = []

        clustered_docs[label].append(documents[i])

    return clustered_docs