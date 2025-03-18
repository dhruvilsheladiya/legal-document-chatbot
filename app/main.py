from fastapi import FastAPI, UploadFile, File, HTTPException
from app.preprocess import extract_text_from_pdf, perform_ner
from app.summarization import generate_summary
import os

app = FastAPI()

UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """Handles PDF file uploads and returns a summary & extracted entities."""
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        text = extract_text_from_pdf(file_path)
        if not text:
            raise HTTPException(status_code=400, detail="No text extracted from PDF.")

        summary = generate_summary(text)
        entities = perform_ner(text)

        return {
            "summary": summary,
            "entities": entities
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
