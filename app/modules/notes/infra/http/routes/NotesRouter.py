from fastapi import APIRouter

notes_router = APIRouter(prefix='/notes')

@notes_router.get('/')
async def get_note():
  pass
