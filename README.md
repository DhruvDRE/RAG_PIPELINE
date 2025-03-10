# RAG_PIPELINE
This is a basic RAG pipeline. You can enhance it by: Adding support for PDFs or other file types in ingestion.py. Using a more powerful model in generator.py (e.g., facebook/rag-token-base). Optimizing FAISS with an IVF index in vector_store.py.

This RAG pipeline includes:

Data Ingestion: Load and preprocess documents.

Embedding Generation: Convert documents into vector embeddings.

Vector Store: Store embeddings in a vector database (FAISS).

Retriever: Retrieve relevant documents based on a query.

Generator: Generate answers using a language model.

Main Script: Tie everything together.


rag-pipeline/

│

├── README.md              # Project description and setup instructions

├── requirements.txt       # Dependencies

├── data/                  # Folder for sample documents

│      └── sample.txt         # Example document

├── ingestion.py           # Step 1: Load and preprocess documents

├── embeddings.py          # Step 2: Generate embeddings

├── vector_store.py        # Step 3: Store embeddings in FAISS

├── retriever.py           # Step 4: Retrieve relevant documents

├── generator.py           # Step 5: Generate answers

└── main.py                # Step 6: Main script to run the pipeline


# RAG Pipeline

A simple Retrieval-Augmented Generation (RAG) pipeline built with Python, FAISS, and Hugging Face transformers.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rag-pipeline.git
   cd rag-pipeline
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your documents to the data/ folder.
4. Run the pipeline:
   ```bash
   python main.py
   ```
# Dependencies

See requirements.txt for a full list.

# Usage

Place text files in the data/ folder.

Run main.py to process documents and query the pipeline.


---

### Create File : `requirements.txt`

**Purpose**: Lists the Python dependencies.

```text
transformers==4.35.0
sentence-transformers==2.2.2
faiss-cpu==1.7.4
torch==2.0.1
numpy==1.26.0
```


# How to Set Up on GitHub

Create a New Repository:

Go to GitHub.com, log in, and click "New Repository."
Name it rag-pipeline, add a description, and initialize it with a README (optional).
Clone the Repository Locally:

```bash
git clone https://github.com/your-username/rag-pipeline.git
cd rag-pipeline
```
Create the Files:

Copy the code above into the respective files using a text editor (e.g., VS Code).

Create the data/ folder and add sample.txt.

Commit and Push:
```bash
git add .
git commit -m "Initial commit: RAG pipeline implementation"
git push origin main
```
Test Locally:
Install dependencies: 
```bash
pip install -r requirements.txt
```
Run the pipeline: 
```bash
python main.py
```
