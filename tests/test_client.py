from tests.test import ClockifyTestCase
from clockify.client.client_dto import ClientDTO
from clockify.session import ClockifySession


class TestGetClients(ClockifyTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = ClockifySession(cls.KEY)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_get_list_of_projects(self):
        clients = self.session.get_clients(self.WORKSPACE)
        # self.fail(projects)
        for client in clients:
            self.assertIsInstance(client, ClientDTO)
