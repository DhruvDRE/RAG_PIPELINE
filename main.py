from ingestion import load_documents
from embeddings import Embedder
from vector_store import VectorStore
from retriever import Retriever
from generator import Generator

def main():
    # Step 1: Load documents
    print("Loading documents...")
    documents = load_documents()

    # Step 2: Generate embeddings
    print("Generating embeddings...")
    embedder = Embedder()
    embeddings = embedder.generate_embeddings(documents)

    # Step 3: Store embeddings
    print("Building vector store...")
    vector_store = VectorStore(dimension=embeddings.shape[1])
    vector_store.add_embeddings(embeddings)

    # Step 4: Set up retriever
    retriever = Retriever(vector_store, embedder, documents)

    # Step 5: Set up generator
    generator = Generator()

    # Step 6: Query the pipeline
    query = "What is RAG?"
    print(f"\nQuery: {query}")
    retrieved_docs = retriever.retrieve(query, k=1)
    print("Retrieved document:", retrieved_docs[0])
    
    answer = generator.generate_answer(query, retrieved_docs[0])
    print("Generated answer:", answer)

if __name__ == "__main__":
    main()
