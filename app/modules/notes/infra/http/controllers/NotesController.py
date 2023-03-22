from sqlalchemy.orm import Session
from ...sqlalchemy.schemas.Note import Note as NoteSchema
from ...sqlalchemy.repositories.SQLAlchemyRepository import SQLAlchemyRepository
from ....services.CreateNoteService import CreateNoteService
from ....services.ListNotesService import ListNotesService
from ....services.GetNoteService import GetNoteService

class NotesController:
  def __init__(self, session: Session):
    self.session = session
    self.ormRepository = SQLAlchemyRepository(self.session)

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
