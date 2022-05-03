from clockify.model.time_entry_model import TimeEntry, TimeEntryGetParams
from tests.test import ClockifyTestCase


class TestTimeEntries(ClockifyTestCase):
    def test_get_list_of_time_entries(self):
        time_entries = self.session.time_entry.get_time_entries(
            self.WORKSPACE, self.USER
        )
        for time_entry in time_entries:
            self.assertIsInstance(time_entry, TimeEntry)

    def test_get_hydrated_list_of_time_entries(self):
        params = TimeEntryGetParams(hydrated=True)
        time_entries = self.session.time_entry.get_time_entries(
            self.WORKSPACE, self.USER, params
        )
        for time_entry in time_entries:
            self.assertIsInstance(time_entry, TimeEntry)

    def test_get_time_entry_by_id(self):
        time_entries = self.session.time_entry.get_time_entries(
            self.WORKSPACE, self.USER
        )
        for time_entry in time_entries:
            search_time_entry = self.session.time_entry.get_time_entry(
                self.WORKSPACE, time_entry.id_
            )
            self.assertIsInstance(search_time_entry, TimeEntry)
            self.assertEqual(search_time_entry, time_entry)
