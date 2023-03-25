from google.cloud.firestore_v1 import Client
from app.shared.infra.schemas.Note import Note as NoteSchema
from ....repositories.INotesRepository import INotesRepository

class FirestoreRepository(INotesRepository):
  def __init__(self, client: Client):
    self.client = client

  async def create(self, title: str) -> NoteSchema:
    notes = await self.list()
    if (len(notes) > 0):
      last_note = notes[-1]
    else:
      last_note = dict(id=-1, order=-1)
    note = dict(id=last_note['id']+1, title=title, order=last_note['id']+1, completed=False)
    self.client.collection('notes').document(str(note['id'])).set(note)
    return note

  async def index(self, id: int) -> NoteSchema:
    stored_notes = []
    notes = self.client.collection('notes').where('id', '==', id).stream()
    for note in notes:
      stored_notes.append(note.to_dict())
    return stored_notes[0]

  async def list(self) -> list[NoteSchema]:
    stored_notes = []
    notes = self.client.collection('notes').stream()
    for note in notes:
      stored_notes.append(note.to_dict())
    return stored_notes

  async def update(self, id: int, note: dict):
    pass

  async def delete(self, id: int):
    pass
