from random import randint, sample
from requests.exceptions import HTTPError
from tests.test import ClockifyTestCase

from clockify.session import ClockifySession
from clockify.model.task_model import Task
from clockify.model.project_model import Project


class TestTasks(ClockifyTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = ClockifySession(cls.KEY)
        task_names = [f"Test Task #{i}" for i in sample(range(0, 99999), 5)]
        project = Project(
            name=f"Test Tasks {randint(0, 999999)}", workspace_id=cls.WORKSPACE
        )
        project = cls.session.create_project(project)
        cls.project_id = project.id_
        for name in task_names:
            task = Task(name=name, project_id=cls.project_id)
            cls.session.create_task(cls.WORKSPACE, task)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_get_list_of_tasks(self):
        tasks = self.session.get_tasks(self.WORKSPACE, self.project_id)
        for task in tasks:
            self.assertIsInstance(task, Task)

    def test_get_list_of_tasks_fail(self):
        self.assertRaises(
            HTTPError, self.session.get_tasks, "fake workspace id", "fake project id"
        )

    def test_get_task_by_id(self):
        task = Task(name=f"Test Task #{randint(0, 99999)}", project_id=self.project_id)
        task = self.session.create_task(self.WORKSPACE, task)
        search_task = self.session.get_task(self.WORKSPACE, self.project_id, task.id_)
        self.assertIsInstance(search_task, Task)
        self.assertEqual(task, search_task)

    def test_get_task_by_id_fail(self):
        self.assertRaises(
            HTTPError,
            self.session.get_task,
            self.WORKSPACE,
            "fake project id",
            "fake task id",
        )

    def test_update_task(self):
        task = Task(name=f"Test Task #{randint(0, 99999)}", project_id=self.project_id)
        task = self.session.create_task(self.WORKSPACE, task)
        task.name = "Bake Pizza"
        updated_task = self.session.update_task(self.WORKSPACE, task)
        self.assertIsInstance(updated_task, Task)
        self.assertEqual(task.name, "Bake Pizza")

    def test_create_task(self):
        task = Task(name=f"Test Task #{randint(0, 99999)}", project_id=self.project_id)
        created_task = self.session.create_task(self.WORKSPACE, task)
        self.assertIsInstance(created_task, Task)
        self.assertIsNotNone(created_task.id_)

    def test_delete_task(self):
        task = Task(name=f"Test Task #{randint(0, 99999)}", project_id=self.project_id)
        created_task = self.session.create_task(self.WORKSPACE, task)
        deleted_task = self.session.delete_task(
            self.WORKSPACE, created_task.project_id, created_task.id_
        )
        self.assertIsInstance(deleted_task, Task)
        self.assertRaises(
            HTTPError,
            self.session.get_task,
            self.WORKSPACE,
            created_task.project_id,
            created_task.id_,
        )

    def test_delete_task_fail(self):
        self.assertRaises(
            HTTPError,
            self.session.delete_task,
            self.WORKSPACE,
            "fake project id",
            "fake task id",
        )
