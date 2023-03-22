from sqlalchemy.orm import Session
from ..schemas.Note import NoteCreate as NoteSchema
from ..models.Note import Note as NoteModel
from ....repositories.INotesRepository import INotesRepository

class SQLAlchemyRepository(INotesRepository):
  def __init__(self, session: Session):
    self.session = session

  async def create(self, title: str) -> NoteSchema:
    note = NoteModel(title=title)
    self.session.add(note)
    self.session.commit()
    self.session.refresh(note)
    return note

  async def index(self, id: str):
    note = self.session.query(NotesModel).filter(NoteModel.id == id).first()
    return note
