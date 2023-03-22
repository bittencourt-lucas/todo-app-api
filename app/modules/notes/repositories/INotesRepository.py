import abc
from ..infra.sqlalchemy.schemas.Note import Note

class INotesRepository(abc.ABC):
  @abc.abstractmethod
  def create(self, title: str) -> Note:
    raise NotImplementedError

  @abc.abstractmethod
  def index(self, id: int) -> Note:
    raise NotImplementedError
