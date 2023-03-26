import unittest
from ...services.CreateNoteService import CreateNoteService
from ...repositories.fakes.FakeNotesRepository import FakeNotesRepository

class TestCreateNoteService(unittest.IsolatedAsyncioTestCase):
  def setUp(self):
    self.notes_repository = FakeNotesRepository()
    self.create_note = CreateNoteService(self.notes_repository)

  def tearDown(self):
    self.notes_repository.clear()

  async def test_execute(self):
    title = 'Hello World'

    note = await self.create_note.execute(title=title)
    
    self.assertIsInstance(note.id, int)
    self.assertEqual(note.title, title)
    self.assertEqual(note.completed, False)
    self.assertIsInstance(note.order, int)
    