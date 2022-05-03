from datetime import datetime, timedelta
from clockify.model.project_model import Project
from clockify.model.tag_model import Tag
from clockify.model.task_model import Task
from clockify.model.time_entry_model import (
    CreateTimeEntryDTO,
    TimeEntry,
    TimeEntryGetParams,
)
from tests.test import ClockifyTestCase


class TestTimeEntries(ClockifyTestCase):
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

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

    def test_create_time_entry(self):
        start = datetime.now()
        end = start + timedelta(minutes=30)
        time_entry_data = CreateTimeEntryDTO(
            start=start, end=end, description="Test Time Entry"
        )
        time_entry = self.session.time_entry.add_time_entry(
            self.WORKSPACE, self.USER, time_entry_data
        )
        self.assertIsInstance(time_entry, TimeEntry)

    def test_create_time_entry_full(self):
        start = datetime.now()
        end = start + timedelta(minutes=30)
        project = self.session.project.create_project(
            Project(name="Time Entry Test Project", workspace_id=self.WORKSPACE)
        )
        task = self.session.task.create_task(
            self.WORKSPACE, Task(name="Test task", project_id=project.id_)
        )
        tag = self.session.tag.create_tag(
            Tag(name="timeentrytest", workspace_id=self.WORKSPACE)
        )
        time_entry_data = CreateTimeEntryDTO(
            start=start,
            end=end,
            billable=True,
            description="doing work",
            project_id=project.id_,
            task_id=task.id_,
            tag_ids=[tag.id_],
        )
        time_entry = self.session.time_entry.add_time_entry(
            self.WORKSPACE, self.USER, time_entry_data
        )
        self.assertIsInstance(time_entry, TimeEntry)
