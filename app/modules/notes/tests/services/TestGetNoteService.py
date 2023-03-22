import unittest
from ...services.CreateNoteService import CreateNoteService
from ...services.GetNoteService import GetNoteService
from ...repositories.fakes.FakeNotesRepository import FakeNotesRepository

class TestGetNoteService(unittest.IsolatedAsyncioTestCase):
  def setUp(self):
    notes_repository = FakeNotesRepository()
    self.create_note = CreateNoteService(notes_repository)
    self.get_note = GetNoteService(notes_repository)

  async def test_execute(self):
    title = 'Hello World'

    note = await self.create_note.execute(title)
    storedNote = await self.get_note.execute(note.id)

    self.assertEqual(note.id, storedNote.id)
    self.assertEqual(note.title, storedNote.title)
    self.assertEqual(note.completed, storedNote.completed)
    self.assertEqual(note.order, storedNote.order)
    