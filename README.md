# Text Summarizer API

A FastAPI backend that summarizes text using a Hugging Face transformer model and stores results in a MySQL database.

## Features
- Summarize any text input.
- Save original and summarized text in MySQL asynchronously.
- Retrieve all past summaries via a simple API endpoint.
- Works on GPU (if available) or CPU.

## Tech Stack
- **Backend:** FastAPI
- **Database:** MySQL
- **NLP Model:** Transformers (`sshleifer/distilbart-cnn-12-6`)
- **Async DB library:** aiomysql

## API Endpoints

### 1. Summarize Text
- **URL:** `/summarize/`
- **Method:** `POST`
- **Request body (JSON):**
```json
{
  "text": "Your text to summarize"
}
