
from fastapi import APIRouter

router = APIRouter()

@router.post("/suggest")
async def suggest_highlight(text: str):
    return {"highlight": text.split(".")[0] if "." in text else text}
