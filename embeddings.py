from sentence_transformers import SentenceTransformer
import numpy as np

class Embedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def generate_embeddings(self, documents):
        """Generate embeddings for a list of documents."""
        embeddings = self.model.encode(documents, convert_to_numpy=True)
        return embeddings

if __name__ == "__main__":
    from ingestion import load_documents
    docs = load_documents()
    embedder = Embedder()
    embeddings = embedder.generate_embeddings(docs)
    print("Embeddings shape:", embeddings.shape)
