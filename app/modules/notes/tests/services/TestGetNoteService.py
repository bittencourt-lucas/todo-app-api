import unittest
from ...services.CreateNoteService import CreateNoteService
from ...services.GetNoteService import GetNoteService
from ...repositories.fakes.FakeNotesRepository import FakeNotesRepository

class TestGetNoteService(unittest.IsolatedAsyncioTestCase):
  def setUp(self):
    self.notes_repository = FakeNotesRepository()
    self.create_note = CreateNoteService(self.notes_repository)
    self.get_note = GetNoteService(self.notes_repository)

  def tearDown(self):
    self.notes_repository.clear()

  async def test_execute(self):
    title = 'Hello World'

    note = await self.create_note.execute(title)
    storedNote = await self.get_note.execute(note.id)

    self.assertEqual(note.id, storedNote.id)
    self.assertEqual(note.title, storedNote.title)
    self.assertEqual(note.completed, storedNote.completed)
    self.assertEqual(note.order, storedNote.order)
    