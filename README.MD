# 📜 Legal Document Chatbot

## Overview
The **Legal Document Chatbot** is an AI-powered system that processes legal documents (NDAs, contracts, policies) and generates clause-specific summaries. It utilizes an **open-source LLM with RAG capabilities** inside a Docker container and includes **GuardRail validation** for user inputs. The chatbot also features a **frontend dashboard** built with Streamlit for document uploads and summaries.

## Features
✅ Extracts text from legal documents (PDFs)  
✅ Retrieves relevant clauses using **RAG (Retrieval-Augmented Generation)**  
✅ Summarizes legal clauses with an **open-source LLM**  
✅ Extracts key legal entities using **NER (Named Entity Recognition)**  
✅ Provides an interactive **frontend (Streamlit)** for document uploads  
✅ **Dockerized** for easy deployment  

---

## 🚀 Setup Instructions

--------# Venv folder im not uploaded in my repo. and .env file not uploaded!.  

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo/legal_chatbot.git
cd legal_chatbot
```

### **2️⃣ Install Dependencies**
Ensure you have Python 3.9+ installed. Then, run:
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the FastAPI Backend**
```bash
uvicorn app.main:app --reload
```
The backend will be available at: **http://127.0.0.1:8000**

### **4️⃣ Run the Streamlit Frontend**
```bash
streamlit run app/frontend.py
```
The frontend will be accessible at: **http://localhost:8501**

---

## 📂 Project Structure
```
legal_chatbot/
│── data/                        # Folder for storing PDFs and text files
│── models/                      # Pre-trained models and embeddings
│── app/                         # Application source code
│   │── main.py                   # FastAPI application
│   │── rag_pipeline.py            # RAG-based document retrieval
│   │── preprocess.py              # Legal text preprocessing
│   │── summarization.py           # LLM-based summarization
│   │── ner.py                     # Named Entity Recognition
│   │── frontend/              
│            │── app.py           # Streamlit app
             │── Dockerfile       # Docker setup
│── requirements.txt              # Python dependencies
│── Dockerfile                    # Docker setup
│── README.md                     # Instructions to run the chatbot
```

---

## 🐳 Docker Deployment

### **1️⃣ Build the Docker Image**
```bash
docker build -t legal_chatbot .
```

### **2️⃣ Run the Docker Container**
```bash
docker run -p 8000:8000 legal_chatbot
```
The backend will now be running inside a container at **http://127.0.0.1:8000**

### **3️⃣ Run Streamlit Frontend (Outside Docker)**
```bash
streamlit run app/frontend/app.py
```

---

## 📡 API Endpoints
### **1️⃣ Upload and Process a Document**
#### **POST /upload/**
- **Description**: Upload a legal document (PDF) and get a summary with extracted entities.
- **Request**:
  ```bash
  curl -X POST "http://127.0.0.1:8000/upload/" \
       -F "file=@example.pdf"
  ```
- **Response**:
  ```json
  {
      "summary": "This NDA prevents disclosure of confidential information.",
      "entities": {
          "Parties": "Company A, Employee B",
          "Effective Date": "2025-03-18",
          "Term": "2 years"
      }
  }
  ```

### **2️⃣ Get Available Endpoints**
#### **GET /docs**
- **Description**: Access the **Swagger API Documentation**.
- **URL**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

# Created By:- 
# Dhruvil Sheladiya.

