from ..repositories.INotesRepository import INotesRepository
from ..infra.sqlalchemy.schemas.Note import Note as NoteSchema

class DeleteNoteService:
  def __init__(self, notesRepository: INotesRepository):
    self.notesRepository: INotesRepository = notesRepository

  async def execute(self, id: int) -> NoteSchema:
    note: NoteSchema = await self.notesRepository.delete(id=id)
    return note
