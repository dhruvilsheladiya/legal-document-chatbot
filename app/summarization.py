from app.rag_pipeline import create_vector_store, retrieve_relevant_text

def generate_summary(text: str) -> str:
    """Generates a summary using only RAG-based retrieval (No OpenAI)."""
    try:
        vector_store = create_vector_store(text)
        relevant_text = retrieve_relevant_text("Summarize the document", vector_store)

        # Simple rule-based summarization: Extract key sentences
        sentences = relevant_text.split(". ")
        summary = ". ".join(sentences[:3])  # Take first 3 sentences
        return summary if summary else "No summary generated."
    
    except Exception as e:
        return f"Error in summarization: {str(e)}"
