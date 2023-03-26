from app.shared.infra.schemas.Note import Note as NoteSchema
from ..repositories.INotesRepository import INotesRepository

class CreateNoteService:
  def __init__(self, notesRepository: INotesRepository):
    self.notesRepository: INotesRepository = notesRepository

  async def execute(self, title: str, order: int | None = None) -> NoteSchema:
    note: NoteSchema = await self.notesRepository.create(title=title, order=order)
    return note
