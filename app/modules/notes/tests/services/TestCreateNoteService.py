import unittest
from ...services.CreateNoteService import CreateNoteService
from ...repositories.fakes.FakeNotesRepository import FakeNotesRepository

class TestCreateNoteService(unittest.IsolatedAsyncioTestCase):
  def setUp(self):
    notes_repository = FakeNotesRepository()
    self.create_note = CreateNoteService(notes_repository)

  async def test_execute(self):
    title = 'Hello World'
    content = 'This is a note'
    note = await self.create_note.execute(title, content)
    self.assertIsInstance(note.id, int)
    self.assertEqual(note.title, title)
    self.assertEqual(note.content, content)
    