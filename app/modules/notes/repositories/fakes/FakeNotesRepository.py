from .. import INotesRepository
from ...infra.sqlalchemy.schemas.NoteSchema import Note

class FakeNotesRepository(INotesRepository):
  notes: list[Note] = []
  id: int = 0

  def create(self, data) -> Note:
    id += 1
    title, content = data

    note = Note(id, title, content)
    notes.append(data)
    
    return note

  def index(self, id) -> Note:
    return self.notes[id]
