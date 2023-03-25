from app.shared.infra.schemas.Note import Note as NoteSchema
from ..repositories.INotesRepository import INotesRepository

class UpdateNoteService:
  def __init__(self, notesRepository: INotesRepository):
    self.notesRepository: INotesRepository = notesRepository

  async def execute(self, id: int, note: NoteSchema) -> NoteSchema:
    note: NoteSchema = await self.notesRepository.update(id, note)
    return note
