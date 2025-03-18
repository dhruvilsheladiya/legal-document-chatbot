from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load embeddings
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_vector_store(text):
    """Splits text, converts into embeddings, and stores in FAISS."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    documents = text_splitter.create_documents([text])

    faiss_index = FAISS.from_documents(documents, embedding_model)
    return faiss_index

def retrieve_relevant_text(query, vector_store):
    """Retrieves the most relevant text chunks from FAISS."""
    try:
        results = vector_store.similarity_search(query, k=3)
        return " ".join([doc.page_content for doc in results])
    except Exception as e:
        return f"Error retrieving relevant text: {str(e)}"
