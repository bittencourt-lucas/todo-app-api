from ..INotesRepository import INotesRepository
from ...infra.sqlalchemy.schemas.Note import Note

class FakeNotesRepository(INotesRepository):
  notes: list[Note] = []
  id: int = 0

  async def create(self, data: tuple([str, str])) -> Note:
    self.id += 1
    title, content = data

    note = Note(id=self.id, title=title, content=content)
    self.notes.append(data)
    
    return note

  async def index(self, id: int) -> Note:
    return self.notes[id]
