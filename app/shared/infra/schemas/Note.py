from pydantic import BaseModel

class NoteBase(BaseModel):
  order: int | None

class NoteCreate(NoteBase):
  title: str

class NoteUpdate(NoteBase):
  completed: bool

class Note(NoteBase):
  id: int
  title: str
  completed: bool

  class Config:
    orm_mode = True
