from sqlalchemy.orm import Session
from ..schemas.Note import Note as NoteSchema
from ..models.Note import Note as NoteModel
from ....repositories.INotesRepository import INotesRepository

class SQLAlchemyRepository(INotesRepository):
  def __init__(self, session: Session):
    self.session = session

  async def create(self, title: str) -> NoteSchema:
    order = len(await self.list())+1
    note = NoteModel(title=title, order=order)
    self.session.add(note)
    self.session.commit()
    self.session.refresh(note)
    return note

  async def index(self, id: int) -> NoteSchema | None:
    note = self.session.query(NoteModel).filter(NoteModel.id == id).first()
    return note if note else None

  async def list(self) -> list[NoteSchema]:
    notes = self.session.query(NoteModel).all()
    return notes

  async def update(self, id: int, note: NoteSchema) -> NoteSchema:
    self.session.query(NoteModel).where(NoteModel.id == id).update(dict(note))
    self.session.commit()
    updated_note = self.session.query(NoteModel).filter(NoteModel.id == id).first()
    return updated_note

  async def delete(self, id: int) -> None:
    self.session.query(NoteModel).where(NoteModel.id == id).delete()
    self.session.commit()
