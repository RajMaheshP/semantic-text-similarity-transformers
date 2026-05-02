from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(embedding1, embedding2):
    """
    Compute cosine similarity between two embeddings
    """
    score = cosine_similarity([embedding1], [embedding2])
    return score[0][0]