from sqlalchemy.orm import Session
from ...sqlalchemy.schemas.Note import Note as NoteSchema
from ...sqlalchemy.repositories.SQLAlchemyRepository import SQLAlchemyRepository
from ....services.CreateNoteService import CreateNoteService

class NotesController:
  def __init__(self, session: Session):
    self.session = session

  async def create(self, request: str) -> NoteSchema:
    title = request
    ormRepository = SQLAlchemyRepository(self.session)
    create_note_service = CreateNoteService(ormRepository)
    note = await create_note_service.execute(title)
    return note
