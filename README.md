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
```
- **Response:**
```json
{
  "original_text": "Your text to summarize",
  "summary": "The summarized text"
}
```
### 2. Get All Summaries
- **URL:** `/summaries/`
- **Method:** `GET`
- **Response:**
```json
[
  {"id": 1, "original_text": "Text 1", "summary": "Summary 1"},
  {"id": 2, "original_text": "Text 2", "summary": "Summary 2"}
]
```
## Future Improvements
- Add a frontend UI to input text and display summaries.
- Add Docker support for easy deployment.
- Include authentication for secure API access.


