from fastapi import APIRouter

router = APIRouter()

@router.get('/ritual')
def generate_ritual():
    return {'message': 'Ritual generated'}