from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="clarity-notes API")


class NoteInput(BaseModel):
    text: str


class StructuredNote(BaseModel):
    symptoms: list[str]
    duration: str | None
    severity: str | None
    red_flags: list[str]
    summary: str
    detected_language: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/structure", response_model=StructuredNote)
def structure_note(note: NoteInput):
    # TODO: call Claude API to detect language and structure the free-text
    # complaint into symptoms / duration / severity / red flags + summary.
    raise NotImplementedError
