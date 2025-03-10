from transformers import pipeline

class Generator:
    def __init__(self, model_name="distilbert-base-uncased-distilled-squad"):
        self.generator = pipeline("question-answering", model=model_name)

    def generate_answer(self, question, context):
        """Generate an answer given a question and context."""
        result = self.generator(question=question, context=context)
        return result["answer"]

if __name__ == "__main__":
    generator = Generator()
    context = "Retrieval-Augmented Generation (RAG) combines retrieval and generation."
    question = "What is RAG?"
    answer = generator.generate_answer(question, context)
    print("Answer:", answer)
