from ..dtos.ICreateNoteDTO import ICreateNoteDTO

class INotesRepository(type):
  def create(self, data: ICreateNoteDTO) -> Note:
    pass

  def index(self, id: Integer) -> Note:
    pass
