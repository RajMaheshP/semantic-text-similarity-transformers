import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

st.title("Semantic Text Similarity using Transformers")

sentence1 = st.text_input("Enter Sentence 1")
sentence2 = st.text_input("Enter Sentence 2")

if st.button("Compute Similarity"):

    embeddings = model.encode([sentence1, sentence2])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    st.write("Similarity Score:", similarity)