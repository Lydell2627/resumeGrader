from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import PyPDF2
import io
import json
from docx import Document

# Load keywords from keywords.json
def load_keywords():
    try:
        with open("keywords.json", "r") as f:
            return json.load(f)["keywords"]
    except Exception as e:
        print(f"Error loading keywords.json: {e}")
        return []

KEYWORDS = load_keywords()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/score")
async def score_document(file: UploadFile = File(...)):
    if not KEYWORDS:
        raise HTTPException(status_code=500, detail="Keyword list not loaded.")

    if file.content_type not in [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "text/plain"
    ]:
        raise HTTPException(status_code=400, detail="Unsupported file type.")

    raw = await file.read()
    text = ""

    try:
        if file.content_type == "application/pdf":
            reader = PyPDF2.PdfReader(io.BytesIO(raw))
            for page in reader.pages:
                text += page.extract_text() or ""

        elif file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(io.BytesIO(raw))
            for para in doc.paragraphs:
                text += para.text + "\n"

        elif file.content_type == "text/plain":
            text = raw.decode("utf-8")  # assumes UTF-8 encoding

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing file: {str(e)}")

    found = [kw for kw in KEYWORDS if kw.lower() in text.lower()]
    score = int(len(found) / len(KEYWORDS) * 100) if KEYWORDS else 0

    return {"score": score, "found_keywords": found}
