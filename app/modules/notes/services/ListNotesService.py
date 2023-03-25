from app.shared.infra.schemas.Note import Note as NoteSchema
from ..repositories.INotesRepository import INotesRepository

class ListNotesService:
  def __init__(self, notesRepository: INotesRepository):
    self.notesRepository: INotesRepository = notesRepository

  async def execute(self) -> list[NoteSchema]:
    notes: list[NoteSchema] = await self.notesRepository.list()
    return notes
