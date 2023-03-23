from sqlalchemy.orm import Session
from ..schemas.Note import NoteCreate as NoteSchema
from ..models.Note import Note as NoteModel
from ....repositories.INotesRepository import INotesRepository

class SQLAlchemyRepository(INotesRepository):
  def __init__(self, session: Session):
    self.session = session

  async def create(self, title: str) -> NoteSchema:
    order = len(await self.list())+1
    note = NoteModel(title=title, order=order)
    new_note = self.session.add(note)
    new_note.commit()
    new_note.refresh(note)
    return note

  async def index(self, id: int) -> NoteSchema:
    note = self.session.query(NoteModel).filter(NoteModel.id == id).first()
    return note

  async def list(self) -> list[NoteSchema]:
    notes = self.session.query(NoteModel).all()
    return notes

  async def update(self, id: int, note: NoteSchema) -> NoteSchema:
    stored_note = self.session.query(NoteModel).filter(NoteModel.id == id)
    stored_note.update(note=note)
    stored_note.commit()
    stored_note.refresh(note)
    return note

  async def delete(self, id: int) -> NoteSchema:
    pass