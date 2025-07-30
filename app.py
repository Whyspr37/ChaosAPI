
from fastapi import FastAPI
from routes import upload, search, whisper, highlight

app = FastAPI(title="ChaosAPI")

app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(search.router, prefix="/search", tags=["Search"])
app.include_router(whisper.router, prefix="/whisper", tags=["Whisper"])
app.include_router(highlight.router, prefix="/highlight", tags=["Highlight"])

@app.get("/")
async def root():
    return {"message": "Welcome to ChaosAPI!"}
