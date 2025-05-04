# 🧠 Deployed Face Recognition Model using Flask

## 📝 Project Overview

This project is a **Flask-based web API** that receives a face image through an HTTP request, processes it using a face recognition model, and returns a **face embedding (vector)**. These embeddings can be stored in a **vector database** (like **Pinecone**, **FAISS**, or **Weaviate**) for future face comparisons (e.g., recognition, clustering, or search).

---

## 🏗️ Architecture

```mermaid
graph TD;
    Client[User/Client]
    Upload[Upload Face Image]
    FlaskAPI[Flask API]
    Model[Face Recognition Model]
    Embedding[Face Embedding]
    VectorDB[Vector Database]

    Client --> Upload --> FlaskAPI
    FlaskAPI --> Model
    Model --> Embedding
    Embedding --> Client
    Embedding --> VectorDB
