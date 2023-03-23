from sqlalchemy.orm import Session
from ...sqlalchemy.schemas.Note import Note as NoteSchema
from ...sqlalchemy.repositories.SQLAlchemyRepository import SQLAlchemyRepository
from ....services.CreateNoteService import CreateNoteService
from ....services.ListNotesService import ListNotesService
from ....services.GetNoteService import GetNoteService
from ....services.UpdateNoteService import UpdateNoteService
from ....services.DeleteNoteService import DeleteNoteService

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

  async def update(self, request: [int, NoteSchema]) -> NoteSchema:
    id, note = request
    update_note_service = UpdateNoteService(self.ormRepository)
    note = await update_note_service.execute(id, note)
    return note

  async def delete(self, request: int) -> None:
    id = request
    delete_note_service = DeleteNoteService(self.ormRepository)
    await delete_note_service.execute(id)
