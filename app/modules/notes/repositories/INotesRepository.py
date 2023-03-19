import abc
from ..infra.sqlalchemy.schemas.NoteSchema import Note

class INotesRepository(abc.ABC):
  @abc.abstractmethod
  def create(self, data: tuple([str, str])) -> Note:
    raise NotImplementedError

  @abc.abstractmethod
  def index(self, id: int) -> Note:
    raise NotImplementedError
