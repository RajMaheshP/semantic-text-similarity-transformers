import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Page config
st.set_page_config(page_title="Semantic Similarity", layout="centered")

# Title
st.title("Semantic Text Similarity using Transformers")
st.markdown("### Compare semantic meaning between sentences using AI-powered embeddings")

# ---------------- EXAMPLE BUTTONS ----------------
st.markdown("### Try Examples")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🟢 High"):
        st.session_state.sentence1 = "The meeting has been postponed"
        st.session_state.sentence2 = "The meeting is delayed"

with col2:
    if st.button("🟡 Medium"):
        st.session_state.sentence1 = "I love eating pizza"
        st.session_state.sentence2 = "pizza is food"

with col3:
    if st.button("🔴 Low"):
        st.session_state.sentence1 = "Data science involves analyzing data"
        st.session_state.sentence2 = "I enjoy playing football"

# ---------------- INPUT FIELDS ----------------
sentence1 = st.text_input("Enter Sentence 1", key="sentence1")
sentence2 = st.text_input("Enter Sentence 2", key="sentence2")

# ---------------- COMPUTE ----------------
if st.button("Compute Similarity"):

    if sentence1.strip() == "" or sentence2.strip() == "":
        st.warning("Please enter both sentences")
    else:
        embeddings = model.encode([sentence1, sentence2])

        similarity = cosine_similarity(
            [embeddings[0]],
            [embeddings[1]]
        )[0][0]

        # ---------------- COLOR LOGIC ----------------
        if similarity >= 0.7:
            color = "#00FFAA"   # Green
            label = "Highly Similar"
        elif similarity >= 0.4:
            color = "#FFD700"   # Yellow
            label = "Moderately Similar"
        else:
            color = "#FF4B4B"   # Red
            label = "Low Similarity"

        # ---------------- RESULT ----------------
        st.markdown(
            f"""
            <div style="text-align: center; margin-top: 20px;">
                <h3 style="color: white;">Similarity Score</h3>
                <h1 style="color: {color}; font-size: 42px; margin-bottom: 5px;">
                    {similarity:.4f}
                </h1>
                <h4 style="color: {color}; margin-top: 0px;">{label}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

        # ---------------- PROGRESS BAR ----------------
        st.markdown("### Similarity Visualization")

        st.progress(float(similarity))

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("Built using Sentence Transformers | Streamlit | PyTorch")