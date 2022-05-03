import os
from unittest import TestCase

from clockify.session import ClockifySession


class ClockifyTestCase(TestCase):
    KEY = os.environ.get("API_KEY")
    WORKSPACE = os.environ.get("WORKSPACE")

    CLIENT = "6263de4b5ca9a1421d1cdbaa"
    USER = "626399702993d4192cb61a97"

    NON_EXISTING_CLIENT = "1234abcd"
    NON_EXISTING_WORKSPACE = "1234abcd"

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = ClockifySession(cls.KEY)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        projects = cls.session.project.get_projects(cls.WORKSPACE)
        for project in projects:
            project.archived = True
            cls.session.project.update_project(project)
            cls.session.project.delete_project(cls.WORKSPACE, project.id_)
        return super().tearDownClass()
