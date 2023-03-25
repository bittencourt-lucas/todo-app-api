from app.shared.infra.schemas.Note import Note as NoteSchema
from ..repositories.INotesRepository import INotesRepository

class GetNoteService:
  def __init__(self, notesRepository: INotesRepository):
    self.notesRepository: INotesRepository = notesRepository

  async def execute(self, id: int) -> NoteSchema:
    note: NoteSchema = await self.notesRepository.index(id=id)
    return note
