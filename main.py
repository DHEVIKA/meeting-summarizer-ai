from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI
app = FastAPI(title="Meeting Summarizer AI")

# Use a public summarization model
# This is CPU-friendly and publicly accessible
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"  # PUBLIC model (~400MB)
)

# Root route
@app.get("/")
def root():
    return {"message": "Meeting Summarizer API is running!"}

# Pydantic model for POST input
class Meeting(BaseModel):
    transcript: str

# Summarization endpoint
@app.post("/summarize")
def summarize(meeting: Meeting):
    summary = summarizer(
        meeting.transcript,
        max_length=100,
        min_length=30,
        do_sample=False
    )
    return {"summary": summary[0]['summary_text']}
