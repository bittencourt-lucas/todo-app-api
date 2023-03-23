from ..INotesRepository import INotesRepository
from ...infra.sqlalchemy.schemas.Note import Note as NoteSchema
from ...infra.sqlalchemy.models.Note import Note as NoteModel

class FakeNotesRepository(INotesRepository):
  notes: list[NoteSchema] = []
  id: int = 0

  async def create(self, title: str) -> NoteSchema:
    self.id += 1
    order = len(await self.list())+1
    note = NoteModel(id=self.id, title=title, order=order, completed=False)
    self.notes.append(note)
    
    return note

  async def index(self, id: int) -> NoteSchema:
    index = next((i for i, note in enumerate(self.notes) if note.id == id), -1)
    return self.notes[index]

  async def list(self) -> list[NoteSchema]:
    return self.notes

  async def update(self, id: int, note: NoteSchema) -> NoteSchema:
    stored_note = await self.index(id)
    self.notes[stored_note.id-1] = note

    return self.notes[stored_note.id-1]

  async def delete(self, id: int) -> None:
    self.notes.pop(id)

  def clear(self) -> None:
    self.notes.clear()
    self.id = 0
