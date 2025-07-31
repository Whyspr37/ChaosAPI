from fastapi import APIRouter, Form
from utils.highlighter import add_manual_highlight, suggest_highlights, view_all_highlights
from utils.summary import archive_one_word_summary
from utils.rituals import generate_reflective_ritual

router = APIRouter()

@router.post("/highlight/manual")
def manual_highlight(note_id: str = Form(...), text: str = Form(...)):
    success = add_manual_highlight(note_id, text)
    return {"status": "added" if success else "error", "note_id": note_id, "text": text}

@router.post("/highlight/ai")
def ai_highlight(note_id: str = Form(...)):
    highlights = suggest_highlights(note_id)
    return {"status": "success", "highlights": highlights}

@router.get("/highlight/view_all")
def view_highlights():
    return {"highlights": view_all_highlights()}

@router.get("/summary/oneword")
def oneword_summary():
    return {"summary": archive_one_word_summary()}

@router.post("/ritual/generate")
def ritual_generate(tags: list[str] = Form(...)):
    return {"ritual": generate_reflective_ritual(tags)}