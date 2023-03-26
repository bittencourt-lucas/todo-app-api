from google.cloud.firestore_v1 import Client
from app.shared.infra.schemas.Note import Note as NoteSchema
from ....repositories.INotesRepository import INotesRepository

class FirestoreRepository(INotesRepository):
  def __init__(self, client: Client):
    self.client = client

  async def create(self, title: str, order: int | None = None) -> NoteSchema:
    notes = await self.list()
    num_notes = len(notes)
    store_order = order if order else num_notes+1
    note = dict(id=num_notes+1, title=title, order=store_order, completed=False)
    self.client.collection('notes').document(str(num_notes+1)).set(note)
    return note

  async def index(self, id: int) -> NoteSchema:
    note = self.client.collection('notes').document(str(id)).get().to_dict()
    return note

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
