from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI(title="CloudOps Lab")

@app.get("/")
def home():
    return {"message": "CloudOps Lab is running!"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
