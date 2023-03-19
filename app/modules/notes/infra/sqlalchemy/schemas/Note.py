from pydantic import BaseModel

class NoteBase(BaseModel):
  title: str
  content: str | None = None

class NoteCreate(NoteBase):
  pass

class Note(NoteBase):
  id: int
  title: str
  content: str

  class Config:
    orm_mode = True
