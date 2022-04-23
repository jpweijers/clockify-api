from shutil import ExecError
from requests.exceptions import HTTPError
from tests.test import ClockifyTestCase
from clockify.client.client_dto import ClientDTO
from clockify.session import ClockifySession


class TestClients(ClockifyTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = ClockifySession(cls.KEY)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_get_list_of_clients(self):
        clients = self.session.get_clients(self.WORKSPACE)
        # self.fail(projects)
        for client in clients:
            self.assertIsInstance(client, ClientDTO)

    def test_get_list_of_clients_fail(self):
        self.assertRaises(
            HTTPError, self.session.get_clients, self.NON_EXISTING_WORKSPACE
        )

    def test_get_client_by_id(self):
        client = self.session.get_client_by_id(self.WORKSPACE, self.CLIENT)
        self.assertIsInstance(client, ClientDTO)

    def test_get_client_by_id_fail(self):
        self.assertRaises(
            HTTPError,
            self.session.get_client_by_id,
            self.WORKSPACE,
            self.NON_EXISTING_CLIENT,
        )
