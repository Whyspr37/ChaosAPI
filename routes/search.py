
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def semantic_search(query: str):
    return {"query": query, "results": ["example result 1", "example result 2"]}
