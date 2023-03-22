from ..repositories.INotesRepository import INotesRepository
from ..infra.sqlalchemy.schemas.Note import Note as NoteSchema

class ListNotesService:
  def __init__(self, notesRepository: INotesRepository):
    self.notesRepository: INotesRepository = notesRepository

  async def execute(self) -> list[NoteSchema]:
    notes: list[NoteSchema] = await self.notesRepository.list()
    return notes
