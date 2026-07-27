from fastapi import FastAPI

app = FastAPI(
    title="Webinar Management API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Webinar Management API"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
