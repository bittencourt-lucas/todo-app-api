import os
from fastapi import APIRouter
from app.shared.infra.sqlalchemy.orm import get_session, engine
from app.shared.infra.firestore.client import client
from app.shared.infra.schemas.Note import Note as NoteSchema, NoteCreate, NoteUpdate
from ..controllers.NotesController import NotesController
from ...sqlalchemy.models import Note as NoteModel

if os.environ['ENV'] == 'development':
  NoteModel.Base.metadata.create_all(bind=engine)
  notes_controller = NotesController(get_session())
elif os.environ['ENV'] == 'production':
  notes_controller = NotesController(client)

notes_router = APIRouter(prefix='/notes')

@notes_router.post('/', response_model=NoteSchema)
async def create_note(note: NoteCreate):
  request = note.title
  return await notes_controller.create(request)

@notes_router.get('/', response_model=list[NoteSchema])
async def list_notes():
  return await notes_controller.list()

@notes_router.get('/{id}', response_model=NoteSchema)
async def index(id: int):
  request = id
  return await notes_controller.index(request)

@notes_router.patch('/{id}', response_model=NoteSchema)
async def update(id: int, note: NoteUpdate):
  request = id, note
  return await notes_controller.update(request)

@notes_router.delete('/{id}', response_model=None)
async def delete(id: int):
  request = id
  return await notes_controller.delete(request)
