import os
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator


def create_app(enable_test_endpoints: bool = False) -> FastAPI:
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

    if enable_test_endpoints:
        @app.get("/test-error")
        def test_error():
            raise HTTPException(
                status_code=500,
                detail="Test error for Prometheus alert",
            )

    Instrumentator().instrument(app).expose(app)
    return app


app = create_app(
    enable_test_endpoints=os.getenv("ENABLE_TEST_ENDPOINTS", "").lower() == "true"
)
