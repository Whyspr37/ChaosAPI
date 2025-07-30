from fastapi import FastAPI
from utils.note_handler import upload_note
from utils.search import semantic_search

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ChaosAPI is running."}