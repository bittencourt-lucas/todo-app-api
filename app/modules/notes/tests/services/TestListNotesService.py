import unittest
from app.shared.infra.schemas.Note import Note as NoteSchema
from ...services.CreateNoteService import CreateNoteService
from ...services.ListNotesService import ListNotesService
from ...repositories.fakes.FakeNotesRepository import FakeNotesRepository

class TestListNotesService(unittest.IsolatedAsyncioTestCase):
  def setUp(self):
    self.notes_repository = FakeNotesRepository()
    self.create_note = CreateNoteService(self.notes_repository)
    self.list_notes = ListNotesService(self.notes_repository)

  def tearDown(self):
    self.notes_repository.clear()

  async def test_execute(self):
    titles = ['Note 1', 'Note 2', 'Note 3']

    for title in titles:
      await self.create_note.execute(title)

    stored_notes = await self.list_notes.execute()

    self.assertEqual(stored_notes[0].title, titles[0])
    self.assertEqual(len(stored_notes), 3)
    self.assertIsInstance(stored_notes, list)
    