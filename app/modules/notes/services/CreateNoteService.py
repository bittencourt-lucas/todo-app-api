from ..repositories.INotesRepository import INotesRepository
from ..infra.sqlalchemy.schemas.Note import Note as NoteSchema

class CreateNoteService:
  def __init__(self, notesRepository: INotesRepository):
    self.notesRepository: INotesRepository = notesRepository

  async def execute(self, title: str) -> NoteSchema:
    note: NoteSchema = await self.notesRepository.create(title=title)
    return note
