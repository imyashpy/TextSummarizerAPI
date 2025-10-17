from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

# Database config
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "text_summarizer"
}

# Create FastAPI app
app = FastAPI(title="Simple Text Summarizer API")

# Request model
class TextRequest(BaseModel):
    text: str

# Simple Python-based summarizer
def simple_summarizer(text: str) -> str:
    # Split into sentences and take first 2
    sentences = text.split('.')
    summary = '. '.join(sentences[:2]).strip()
    return summary + '.' if summary else text

# Endpoint: Summarize text
@app.post("/summarize/")
def summarize_text(request: TextRequest):
    text = request.text
    summary = simple_summarizer(text)

    try:
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO summaries (original_text, summarized_text) VALUES (%s, %s)",
            (text, summary)
        )
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"original_text": text, "summarized_text": summary}

# Endpoint: Get all summaries
@app.get("/summaries/")
def get_summaries():
    try:
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()
        cursor.execute("SELECT id, original_text, summarized_text FROM summaries")
        rows = cursor.fetchall()
        cursor.close()
        db.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return [
        {"id": row[0], "original_text": row[1], "summarized_text": row[2]}
        for row in rows
    ]
