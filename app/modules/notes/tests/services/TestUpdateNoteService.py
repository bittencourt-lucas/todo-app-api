import unittest
from ...services.CreateNoteService import CreateNoteService
from ...services.UpdateNoteService import UpdateNoteService
from ...repositories.fakes.FakeNotesRepository import FakeNotesRepository

class TestCreateNoteService(unittest.IsolatedAsyncioTestCase):
  def setUp(self):
    self.notes_repository = FakeNotesRepository()
    self.create_note = CreateNoteService(self.notes_repository)
    self.update_note = UpdateNoteService(self.notes_repository)

  def tearDown(self):
    self.notes_repository.clear()

  async def test_execute(self):
    title = 'Hello World'

    note = await self.create_note.execute(title)
    note.order = 10
    updated_note = await self.update_note.execute(note.id, note)
    
    self.assertEqual(note.id, updated_note.id)
    self.assertEqual(note.title, updated_note.title)
    self.assertEqual(note.completed, updated_note.completed)
    self.assertEqual(updated_note.order, 10)
    