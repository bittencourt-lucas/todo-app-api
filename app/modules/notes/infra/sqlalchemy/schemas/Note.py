from pydantic import BaseModel

class NoteBase(BaseModel):
  title: str

class NoteCreate(NoteBase):
  pass

class Note(NoteBase):
  id: int
  title: str
  completed: bool
  order: int

  class Config:
    orm_mode = True
