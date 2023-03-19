from ..repositories.INotesRepository import INotesRepository
from ..infra.sqlalchemy.schemas.NoteSchema import Note

class CreateNoteService:
  def __init__(self, notesRepository: INotesRepository):
    self.notesRepository: INotesRepository = notesRepository

  async def execute(self, title: str, content: str) -> Note:
    note: Note = await self.notesRepository.create(data=(title, content))
    return note
