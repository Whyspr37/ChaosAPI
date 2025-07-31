from fastapi import APIRouter, Form
from utils.trauma import (
    generate_shadow_work,
    build_haunt_index
)

router = APIRouter()

@router.post("/trauma/shadow_work")
def shadow_work(theme: str = Form(...)):
    result = generate_shadow_work(theme)
    return {"shadow_analysis": result}

@router.get("/trauma/haunt_index")
def haunt_index():
    return {"index": build_haunt_index()}