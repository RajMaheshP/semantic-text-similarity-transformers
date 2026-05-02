import numpy as np

def generate_embeddings(model, sentences):
    """
    Generate embeddings for sentences
    """
    embeddings = model.encode(sentences)
    return np.array(embeddings)