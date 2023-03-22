from ..INotesRepository import INotesRepository
from ...infra.sqlalchemy.schemas.Note import Note as NoteSchema
from ...infra.sqlalchemy.models.Note import Note as NoteModel

class FakeNotesRepository(INotesRepository):
  notes: list[NoteSchema] = []
  id: int = 0

  async def create(self, title: str) -> NoteSchema:
    self.id += 1

    note = NoteModel(id=self.id, title=title, order=self.id, completed=False)
    self.notes.append(note)
    
    return note

  async def index(self, id: int) -> NoteSchema:
    return self.notes[id]
