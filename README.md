![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)
![NLP](https://img.shields.io/badge/NLP-Transformers-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![GitHub stars](https://img.shields.io/github/stars/RajMaheshP/semantic-text-similarity-transformers?style=social)

# Text Embedding & Semantic Understanding Using Transformers

🎓 Internship Project (WoRisGo, Bengaluru)

---

## 📌 Overview

This project demonstrates how transformer-based models can be used to generate sentence embeddings and perform:

- Semantic Similarity  
- Semantic Search  
- Document Clustering  

The system leverages **Sentence-BERT (SBERT)** to generate high-quality contextual embeddings for textual data, enabling machines to understand semantic meaning beyond simple keyword matching.

---

## 🚀 Features

- Sentence Embedding Generation  
- Semantic Similarity Computation (Cosine Similarity)  
- Semantic Search Engine  
- Document Clustering  
- Interactive Web Interface using Streamlit  

---

## 🛠️ Technologies Used

- Python  
- PyTorch  
- Sentence Transformers  
- FAISS  
- Scikit-learn  
- Streamlit  

---

## 📂 Project Structure

```
semantic-text-similarity-transformers/
│
├── app/                  # Streamlit web application
├── clustering/           # Document clustering logic
├── data/                 # Sample input documents
├── models/               # Model loading & embeddings
├── search/               # Semantic search implementation
├── utils/                # Utility functions
│
├── main.py               # CLI-based execution
├── requirements.txt      # Dependencies
├── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/RajMaheshP/semantic-text-similarity-transformers
cd semantic-text-similarity-transformers
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### 🔹 Command Line Mode

```
python main.py
```

### 🔹 Web Application (Streamlit)

```
streamlit run app/streamlit_app.py
```

---

## 📊 Example Use Case

**Input:**
- Sentence 1: The meeting has been postponed  
- Sentence 2: The meeting is delayed  

**Output:**
- High similarity score (~0.84+)

---

## 🤖 Model Used

- all-MiniLM-L6-v2 (Sentence Transformers)

---

## 📁 Dataset

Sample text documents are provided in the `data/` directory.

---

## 💡 Applications

- Semantic Search Engines  
- Text Similarity Detection  
- Document Clustering  
- Recommendation Systems  
- NLP-based Intelligent Assistants  

---

## 🏢 Internship Details

This project was developed as part of an internship at:

**WoRisGo, Bengaluru**

Focused on:
- Natural Language Processing (NLP)  
- Transformer-based models  
- Semantic understanding systems  

---

## 📬 Contact

Feel free to connect for collaboration or feedback.