# backend/main.py

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import PyPDF2, io, json, os
from docx import Document
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()  # Add this line at the top (after imports)

# Load keywords
def load_keywords(path="keywords.json"):
    with open(path) as f:
        return json.load(f)["keywords"]

KEYWORDS = load_keywords()

# MongoDB setup (replace MONGO_URI in env or inline)
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client.resume_grader
scores_collection = db.scores

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/score")
async def score_document(file: UploadFile = File(...)):
    if file.content_type not in [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "text/plain"
    ]:
        raise HTTPException(status_code=400, detail="Unsupported file type.")

    raw = await file.read()
    text = ""

    # PDF
    if file.content_type == "application/pdf":
        try:
            reader = PyPDF2.PdfReader(io.BytesIO(raw))
            for page in reader.pages:
                text += page.extract_text() or ""
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Failed to read PDF: {e}")

    # Plain text
    elif file.content_type == "text/plain":
        try:
            text = raw.decode("utf-8")
        except Exception:
            raise HTTPException(status_code=400, detail="Failed to decode text file.")

    # DOCX
    else:
        try:
            doc = Document(io.BytesIO(raw))
            for p in doc.paragraphs:
                text += p.text + "\n"
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Failed to read DOCX: {e}")

    # Scoring
    found = [kw for kw in KEYWORDS if kw.lower() in text.lower()]
    score = int(len(found) / len(KEYWORDS) * 100) if KEYWORDS else 0

    # Persist result
    scores_collection.insert_one({
        "filename": file.filename,
        "score": score,
        "timestamp": datetime.utcnow()
    })

    return {"score": score, "found_keywords": found}


@app.get("/api/high-scores")
async def get_high_scores():
    docs = scores_collection.find({"score": {"$gt": 60}}).sort("timestamp", -1)
    high_scores = [
        {"filename": d["filename"], "score": d["score"]}
        for d in docs
    ]
    return JSONResponse(content=high_scores)
