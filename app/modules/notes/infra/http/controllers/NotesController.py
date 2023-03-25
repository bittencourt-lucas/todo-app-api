from sqlalchemy.orm import Session
from google.cloud.firestore_v1 import Client
from app.shared.infra.schemas.Note import Note as NoteSchema
from ...sqlalchemy.repositories.SQLAlchemyRepository import SQLAlchemyRepository
from ...firestore.repositories.FirestoreRepository import FirestoreRepository
from ....services.CreateNoteService import CreateNoteService
from ....services.ListNotesService import ListNotesService
from ....services.GetNoteService import GetNoteService
from ....services.UpdateNoteService import UpdateNoteService
from ....services.DeleteNoteService import DeleteNoteService

class NotesController:
  def __init__(self, *args):
    if len(args) != 1:
      raise(Exception('Invalid input for NotesController. The input must be one ORM or DB client.'))
    if isinstance(args[0], Session):
      self.ormRepository = SQLAlchemyRepository(args[0])
    elif isinstance(args[0], Client):
      self.ormRepository = FirestoreRepository(args[0])
    else:
      raise(Exception('The input is not a valid ORM or DB client type.'))

  async def create(self, request: str) -> NoteSchema:
    title = request
    create_note_service = CreateNoteService(self.ormRepository)
    note = await create_note_service.execute(title)
    return note

  async def list(self) -> list:
    list_notes_service = ListNotesService(self.ormRepository)
    notes = await list_notes_service.execute()
    return notes

  async def index(self, request: int) -> NoteSchema:
    id = request
    get_note_service = GetNoteService(self.ormRepository)
    note = await get_note_service.execute(id)
    return note

  async def update(self, request: [int, NoteSchema]) -> NoteSchema:
    id, note = request
    update_note_service = UpdateNoteService(self.ormRepository)
    note = await update_note_service.execute(id, note)
    return note

  async def delete(self, request: int) -> None:
    id = request
    delete_note_service = DeleteNoteService(self.ormRepository)
    await delete_note_service.execute(id)
