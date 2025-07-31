from fastapi import APIRouter, Query
from utils.search_engine import semantic_search, vibe_search
from utils.search import (
    memory_timeline,
    reoccurrence_tracker,
    contradiction_finder,
    unreliable_narrator_detector
)

router = APIRouter()

@router.get("/search/semantic")
def semantic_search_endpoint(query: str = Query(...)):
    results = semantic_search(query)
    return {"results": results}

@router.get("/search/vibe")
def vibe_search_endpoint(vibe: str = Query(...)):
    results = vibe_search(vibe)
    return {"results": results}

@router.get("/search/timeline")
def timeline_endpoint():
    return {"timeline": memory_timeline()}

@router.get("/search/reoccurrence")
def reoccurrence_endpoint(tag: str = Query(...)):
    return {"reoccurrence": reoccurrence_tracker(tag)}

@router.get("/search/contradictions")
def contradictions_endpoint():
    return {"contradictions": contradiction_finder()}

@router.get("/search/unreliable")
def unreliable_endpoint():
    return {"flags": unreliable_narrator_detector()}