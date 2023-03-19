import abc

class INotesRepository(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def create(self, data: tuple(str, str)) -> Note:
    return

  @abc.abstractmethod
  def index(self, id: int) -> Note:
    return
