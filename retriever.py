from embeddings import Embedder

class Retriever:
    def __init__(self, vector_store, embedder, documents):
        self.vector_store = vector_store
        self.embedder = embedder
        self.documents = documents

    def retrieve(self, query, k=1):
        """Retrieve the top-k relevant documents for a query."""
        query_embedding = self.embedder.generate_embeddings([query])
        distances, indices = self.vector_store.index.search(query_embedding, k)
        retrieved_docs = [self.documents[idx] for idx in indices[0]]
        return retrieved_docs

if __name__ == "__main__":
    from ingestion import load_documents
    from embeddings import Embedder
    from vector_store import VectorStore

    docs = load_documents()
    embedder = Embedder()
    embeddings = embedder.generate_embeddings(docs)
    
    vector_store = VectorStore(dimension=embeddings.shape[1])
    vector_store.add_embeddings(embeddings)
    
    retriever = Retriever(vector_store, embedder, docs)
    results = retriever.retrieve("What is RAG?", k=1)
    print("Retrieved:", results)
