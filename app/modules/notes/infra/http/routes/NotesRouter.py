from fastapi import APIRouter, Depends
from app.shared.infra.sqlalchemy.orm import get_session
from app.shared.infra.sqlalchemy.orm import engine
from ..controllers.NotesController import NotesController
from ...sqlalchemy.models import Note as NoteModel
from ...sqlalchemy.schemas.Note import Note as NoteSchema

NoteModel.Base.metadata.create_all(bind=engine)

notes_controller = NotesController(Depends(get_session()))

notes_router = APIRouter(prefix='/notes')

@notes_router.post('/', response_model=NoteSchema)
async def create_note(title: str, content: str):
  request = (title, content)
  return notes_controller.create(request)
