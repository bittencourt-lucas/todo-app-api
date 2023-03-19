from fastapi import APIRouter
from app.modules.notes.infra.http.routes.NotesRouter import notes_router

router = APIRouter(prefix='/api')

router.include_router(notes_router)
