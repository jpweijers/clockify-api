from random import randint, sample
from clockify.model.project_model import Project
from clockify.session import ClockifySession
from tests.test import ClockifyTestCase


class TestProject(ClockifyTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = ClockifySession(cls.KEY)
        project_names = [f"Test Project #{i}" for i in sample(range(0, 99999), 5)]
        for name in project_names:
            project = Project(name=name, workspace_id=cls.WORKSPACE)
            cls.session.create_project(project)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        projects = cls.session.get_projects(cls.WORKSPACE)
        for project in projects:
            project.archived = True
            cls.session.update_project(project)
            cls.session.delete_project(project.workspace_id, project.id_)

    def test_get_projects(self):
        projects = self.session.get_projects(self.WORKSPACE)
        self.assertGreater(len(projects), 0)
        for project in projects:
            self.assertIsInstance(project, Project)

    def test_get_project_by_id(self):
        projects = self.session.get_projects(self.WORKSPACE)
        project = self.session.get_project(projects[0].workspace_id, projects[0].id_)
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
