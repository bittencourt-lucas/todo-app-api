from .. import INotesRepository
from ...infra.sqlalchemy.schemas.NoteSchema import Note

class FakeNotesRepository:
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
