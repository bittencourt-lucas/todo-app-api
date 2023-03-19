import abc
from ..infra.sqlalchemy.schemas.NoteSchema import Note

class INotesRepository(metaclass=abc.ABCMeta):
  def __init_subclass__(cls, **kwargs):
    # always make it colaborative:
    super().__init_subclass__(**kwargs)
    register_class(cls)

  @abc.abstractmethod
  async def create(self, data: tuple([str, str])) -> Note:
    return

  @abc.abstractmethod
  async def index(self, id: int) -> Note:
    return
