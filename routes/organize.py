from fastapi import APIRouter, Form
from utils.organizer import (
    add_to_storyline, view_storyline,
    assign_archetype, merge_tags,
    auto_tag_note
)

router = APIRouter()

@router.post("/organize/storyline")
def storyline_add(note_id: str = Form(...), arc: str = Form(...)):
    return {"status": add_to_storyline(note_id, arc)}

@router.get("/organize/storyline")
def storyline_view():
    return {"storylines": view_storyline()}

@router.post("/organize/archetype")
def archetype_assign(note_id: str = Form(...), role: str = Form(...)):
    return {"status": assign_archetype(note_id, role)}

@router.post("/organize/tag_merge")
def tag_merge(source: str = Form(...), target: str = Form(...)):
    return {"merged_to": merge_tags(source, target)}

@router.post("/organize/auto_tag")
def auto_tag(note_id: str = Form(...)):
    return {"tags": auto_tag_note(note_id)}