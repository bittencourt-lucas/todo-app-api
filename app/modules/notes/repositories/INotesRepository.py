import abc
from ..infra.sqlalchemy.schemas.Note import Note

class INotesRepository(abc.ABC):
  @abc.abstractmethod
  def create(self, title: str) -> Note:
    raise NotImplementedError

  @abc.abstractmethod
  def index(self, id: int) -> Note:
    raise NotImplementedError

  @abc.abstractmethod
  def list(self) -> list[Note]:
    raise NotImplementedError

  @abc.abstractmethod
  def update(self, id: str, note: Note) -> Note:
    raise NotImplementedError
  
  @abc.abstractmethod
  def delete(self, id: str) -> None:
    raise NotImplementedError
  