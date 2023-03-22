from ..repositories.INotesRepository import INotesRepository
from ..infra.sqlalchemy.schemas.Note import Note as NoteSchema

class GetNoteService:
  def __init__(self, notesRepository: INotesRepository):
    self.notesRepository: INotesRepository = notesRepository

  async def execute(self, id: int) -> NoteSchema:
    note: NoteSchema = await self.notesRepository.index(id=id)
    return note
