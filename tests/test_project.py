from random import randint, sample
from clockify.model.project_model import Project, ProjectGetParams
from clockify.session import ClockifySession
from tests.test import ClockifyTestCase


class TestProject(ClockifyTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        project_names = [f"Test Project #{i}" for i in sample(range(0, 99999), 5)]
        for name in project_names:
            project = Project(name=name, workspace_id=cls.WORKSPACE)
            cls.session.project.create_project(project)

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def test_get_projects(self):
        projects = self.session.project.get_projects(self.WORKSPACE)
        self.assertGreater(len(projects), 0)
        for project in projects:
            self.assertIsInstance(project, Project)

    def test_get_project_by_id(self):
        projects = self.session.project.get_projects(self.WORKSPACE)
        project = self.session.project.get_project(
            projects[0].workspace_id, projects[0].id_
        )
        self.assertIsInstance(project, Project)

    def test_get_projects_with_params(self):
        params = ProjectGetParams(hydrated=True)
        projects = self.session.project.get_projects(self.WORKSPACE, params)
        for project in projects:
            self.assertIsInstance(project, Project)

    def test_create_project(self):
        project = Project(
            name=f"Test Create {randint(0, 99999)}", workspace_id=self.WORKSPACE
        )
        project = self.session.project.create_project(project)
        self.assertIsInstance(project, Project)

    def test_archive_project(self):
        project = Project(
            name=f"Test Archive {randint(0, 99999)}", workspace_id=self.WORKSPACE
        )
        project = self.session.project.create_project(project)
        project.archived = True
        project = self.session.project.update_project(project)

    def test_delete_project(self):
        project = Project(
            name=f"Test Delete {randint(0, 99999)}", workspace_id=self.WORKSPACE
        )

        project = self.session.project.create_project(project)
        project.archived = True
        project = self.session.project.update_project(project)
        project = self.session.project.delete_project(project.workspace_id, project.id_)
        self.assertIsInstance(project, Project)
