from datetime import datetime, timezone
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

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

Instrumentator().instrument(app).expose(app)