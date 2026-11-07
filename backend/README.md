# backend

FastAPI service for clarity-notes.

## Setup

```
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Set `ANTHROPIC_API_KEY` in your environment before running.

## Run

```
uvicorn app.main:app --reload
```

## Endpoints

- `GET /health` — health check
- `POST /structure` — takes `{"text": "..."}`, returns structured note (not yet implemented)
