from sqlalchemy.orm import Session
from ...sqlalchemy.schemas.Note import Note as NoteSchema
from ...sqlalchemy.repositories.SQLAlchemyRepository import SQLAlchemyRepository
from ....services.CreateNoteService import CreateNoteService

class NotesController:
  def __init__(self, session: Session):
    self.session = session

  async def create(self, request: tuple(str, str)) -> NoteSchema:
    title, content = request
    db_session = SQLAlchemyRepository(session)
    create_note_service = CreateNoteService(db_session)
    note = create_note_service.execute(title, content)
    return note
