from fastapi import APIRouter
from app.shared.infra.sqlalchemy.orm import get_session, engine
from ..controllers.NotesController import NotesController
from ...sqlalchemy.schemas.Note import Note as NoteSchema, NoteCreate
from ...sqlalchemy.models import Note as NoteModel

NoteModel.Base.metadata.create_all(bind=engine)

notes_controller = NotesController(get_session())

notes_router = APIRouter(prefix='/notes')

@notes_router.post('/', response_model=NoteSchema)
async def create_note(note: NoteCreate):
  request = note.title
  return await notes_controller.create(request)

@notes_router.get('/', response_model=list[NoteSchema])
async def list_notes():
  return await notes_controller.list()
