import unittest
from ...services.CreateNoteService import CreateNoteService
from ...services.GetNoteService import GetNoteService
from ...services.DeleteNoteService import DeleteNoteService
from ...repositories.fakes.FakeNotesRepository import FakeNotesRepository

class TestGetNoteService(unittest.IsolatedAsyncioTestCase):
  def setUp(self):
    self.notes_repository = FakeNotesRepository()
    self.create_note = CreateNoteService(self.notes_repository)
    self.get_note = GetNoteService(self.notes_repository)
    self.delete_note = DeleteNoteService(self.notes_repository)

  def tearDown(self):
    self.notes_repository.clear()

  async def test_execute(self):
    title = 'Hello World'

    note = await self.create_note.execute(title)
    await self.delete_note.execute(note.id)
    storedNote = await self.get_note.execute(note.id)

    self.assertIsNone(storedNote)
    