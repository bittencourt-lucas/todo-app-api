import abc
from app.shared.infra.schemas.Note import Note

class INotesRepository(abc.ABC):
  @abc.abstractmethod
  def create(self, title: str, order: int | None) -> Note:
    raise NotImplementedError

  @abc.abstractmethod
  def index(self, id: int) -> Note | None:
    raise NotImplementedError

  @abc.abstractmethod
  def list(self) -> list[Note]:
    raise NotImplementedError

  @abc.abstractmethod
  def update(self, id: int, note: Note) -> Note:
    raise NotImplementedError
  
  @abc.abstractmethod
  def delete(self, id: int) -> None:
    raise NotImplementedError
  