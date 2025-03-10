import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)  # L2 distance index

    def add_embeddings(self, embeddings):
        """Add embeddings to the FAISS index."""
        self.index.add(embeddings)

    def save(self, filepath="faiss_index.bin"):
        """Save the FAISS index to disk."""
        faiss.write_index(self.index, filepath)

    @staticmethod
    def load(filepath="faiss_index.bin"):
        """Load a FAISS index from disk."""
        index = faiss.read_index(filepath)
        vector_store = VectorStore(0)  # Dimension is inferred
        vector_store.index = index
        return vector_store

if __name__ == "__main__":
    from embeddings import Embedder
    from ingestion import load_documents

    docs = load_documents()
    embedder = Embedder()
    embeddings = embedder.generate_embeddings(docs)
    
    vector_store = VectorStore(dimension=embeddings.shape[1])
    vector_store.add_embeddings(embeddings)
    vector_store.save()
    print("Vector store created and saved.")
