from pydantic import BaseModel

class NoteBase(BaseModel):
  pass

class NoteCreate(NoteBase):
  title: str

class NoteUpdate(NoteBase):
  completed: bool
  order: int

class Note(NoteBase):
  id: int
  title: str
  completed: bool
  order: int

  class Config:
    orm_mode = True
