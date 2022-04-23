from random import randint
from requests.exceptions import HTTPError
from tests.test import ClockifyTestCase
from clockify.client.client_dto import ClientDTO
from clockify.session import ClockifySession


class TestClients(ClockifyTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = ClockifySession(cls.KEY)
        cls.created_clients = []
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        for client in cls.created_clients:
            cls.session.delete_client(cls.WORKSPACE, client)
        return super().tearDownClass()

    def test_get_list_of_clients(self):
        clients = self.session.get_clients(self.WORKSPACE)
        # self.fail(projects)
        for client in clients:
            self.assertIsInstance(client, ClientDTO)

    def test_get_list_of_clients_fail(self):
        self.assertRaises(HTTPError, self.session.get_clients, "fakeworkspace")

    def test_get_client_by_id(self):
        client = ClientDTO(f"Test Get {randint(0, 99999)}")
        client = self.session.create_client(self.WORKSPACE, client)
        self.created_clients.append(client.id_)
        client = self.session.get_client_by_id(self.WORKSPACE, client.id_)
        self.assertIsInstance(client, ClientDTO)

    def test_get_client_by_id_fail(self):
        self.assertRaises(
            HTTPError,
            self.session.get_client_by_id,
            self.WORKSPACE,
            self.NON_EXISTING_CLIENT,
        )

    def test_create_client(self):
        client = ClientDTO(f"Test Create {randint(0, 9999)}")
        client = self.session.create_client(self.WORKSPACE, client)
        self.assertIsInstance(client, ClientDTO)
        self.created_clients.append(client.id_)

    def test_delete_client(self):
        client = ClientDTO(f"Test Create {randint(0, 9999)}")
        client = self.session.create_client(self.WORKSPACE, client)
        client = self.session.delete_client(self.WORKSPACE, client.id_)
        self.assertIsInstance(client, ClientDTO)
        self.assertRaises(
            HTTPError, self.session.get_client_by_id, self.WORKSPACE, client.id_
        )
