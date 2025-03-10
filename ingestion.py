import os

def load_documents(data_dir="data"):
    """Load text files from the data directory."""
    documents = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(data_dir, filename), "r", encoding="utf-8") as f:
                documents.append(f.read().strip())
    return documents

if __name__ == "__main__":
    docs = load_documents()
    print("Loaded documents:", docs)
