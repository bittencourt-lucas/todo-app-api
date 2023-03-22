import unittest
from ...services.CreateNoteService import CreateNoteService
from ...services.ListNotesService import ListNotesService
from ...repositories.fakes.FakeNotesRepository import FakeNotesRepository
from ...infra.sqlalchemy.schemas.Note import NoteSchema

class TestListNotesService(unittest.IsolatedAsyncioTestCase):
  def setUp(self):
    notes_repository = FakeNotesRepository()
    self.create_note = CreateNoteService(notes_repository)
    self.get_note = ListNotesService(notes_repository)

  async def test_execute(self):
    titles = ['Note 1', 'Note 2', 'Note 3']

    for title in tiles:
      await self.create_note.execute(title)

    storedNotes = await self.get_note.execute()

    self.assertEqual(storedNotes[0].titles, titles[0])
    self.assertEqual(len(storedNotes), 3)
    self.assertIsInstance(storedNotes, list[NoteSchema])
    