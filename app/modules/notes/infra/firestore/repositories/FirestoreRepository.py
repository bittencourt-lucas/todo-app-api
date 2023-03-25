from google.cloud.firestore_v1 import Client
from app.shared.infra.schemas.Note import Note as NoteSchema
from ....repositories.INotesRepository import INotesRepository

class FirestoreRepository(INotesRepository):
  def __init__(self, client: Client):
    self.client = client

  async def create(self, title: str) -> NoteSchema:
    note = dict(id=0, title=title, order=0, completed=False)
    self.client.collection('notes').document().set(note)
    return note

  async def index(self, id: int):
    note_found = []
    created_note = self.client.collection('notes').where('id', '==', id).stream()
    for doc in created_note:
      note_found.append(doc.to_dict())
    return note_found[0]

  async def list(self):
    pass

  async def update(self, id: int, note: dict):
    pass

  async def delete(self, id: int):
    pass
