from fastapi import APIRouter, Form
from utils.creative import (
    generate_polaroid_snapshot,
    pull_quote_tarot,
    scaffold_zine_layout
)

router = APIRouter()

@router.post("/creative/polaroid")
def polaroid(note_id: str = Form(...)):
    snapshot = generate_polaroid_snapshot(note_id)
    return {"snapshot": snapshot}

@router.get("/creative/tarot")
def tarot():
    return {"cards": pull_quote_tarot()}

@router.get("/creative/zine_scaffold")
def zine_scaffold():
    return {"layout": scaffold_zine_layout()}