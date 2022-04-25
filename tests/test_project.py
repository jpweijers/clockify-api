from random import randint
from clockify.model.project_model import Project
from clockify.session import ClockifySession
from tests.test import ClockifyTestCase


class TestProject(ClockifyTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = ClockifySession(cls.KEY)
        return super().setUpClass()

    @classmethod
    def tearDownClass(self):
        return super().setUpClass()

    def test_get_projects(self):
        projects = self.session.get_projects(self.WORKSPACE)
        for project in projects:
            self.assertIsInstance(project, Project)

    def test_get_project_by_id(self):
        project = self.session.get_project(self.WORKSPACE, "6264286ef7a4597cbca48059")
        self.assertIsInstance(project, Project)

    def test_create_project(self):
        project = Project(
            name=f"Test Create {randint(0, 99999)}", workspace_id=self.WORKSPACE
        )
        project = self.session.create_project(project)
        self.assertIsInstance(project, Project)

    def test_archive_project(self):
        project = Project(
            name=f"Test Archive {randint(0, 99999)}", workspace_id=self.WORKSPACE
        )
        project = self.session.create_project(project)
        project.archived = True
        project = self.session.update_project(project)

    def test_delete_project(self):
        project = Project(
            name=f"Test Delete {randint(0, 99999)}", workspace_id=self.WORKSPACE
        )

        project = self.session.create_project(project)
        project.archived = True
        project = self.session.update_project(project)
        project = self.session.delete_project(project.workspace_id, project.id_)
        self.assertIsInstance(project, Project)
