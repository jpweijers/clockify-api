from random import randint, sample
from requests.exceptions import HTTPError
from tests.test import ClockifyTestCase
from clockify.client.client_dto import ClientDTO, ClientQueryDTO, SortColumn, SortOrder
from clockify.session import ClockifySession


class TestClients(ClockifyTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = ClockifySession(cls.KEY)
        clients = [f"Test Client #{i}" for i in sample(range(0, 99999), 5)]
        for client in clients:
            cls.session.create_client(cls.WORKSPACE, ClientDTO(client))
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        clients = cls.session.get_clients(cls.WORKSPACE)
        for client in clients:
            cls.session.delete_client(cls.WORKSPACE, client.id_)

    def test_get_list_of_clients(self):
        clients = self.session.get_clients(self.WORKSPACE)
        # self.fail(projects)
        for client in clients:
            self.assertIsInstance(client, ClientDTO)

    def test_get_list_of_clients_fail(self):
        self.assertRaises(HTTPError, self.session.get_clients, "fakeworkspace")

    def test_query_name_ascending(self):
        query = ClientQueryDTO(False, "", 1, 50, SortColumn.NAME, SortOrder.ASCENDING)
        clients = self.session.get_clients(self.WORKSPACE, query)
        for client in clients:
            self.assertIsInstance(client, ClientDTO)

    def test_query_id_descending(self):
        query = ClientQueryDTO(True, "", 1, 200, SortColumn.ID, SortOrder.DESCENDING)
        clients = self.session.get_clients(self.WORKSPACE, query)
        for client in clients:
            self.assertIsInstance(client, ClientDTO)

    def test_query_fail(self):
        query = ClientQueryDTO(sort_column="FAKE")
        self.assertRaises(HTTPError, self.session.get_clients, self.WORKSPACE, query)

        query = ClientQueryDTO(sort_order="UPSIDEDOWN")
        self.assertRaises(HTTPError, self.session.get_clients, self.WORKSPACE, query)

    def test_get_client_by_id(self):
        client = ClientDTO(f"Test Get {randint(0, 99999)}")
        client = self.session.create_client(self.WORKSPACE, client)
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

    def test_delete_client(self):
        client = ClientDTO(f"Test Create {randint(0, 9999)}")
        client = self.session.create_client(self.WORKSPACE, client)
        client = self.session.delete_client(self.WORKSPACE, client.id_)
        self.assertIsInstance(client, ClientDTO)
        self.assertRaises(
            HTTPError, self.session.get_client_by_id, self.WORKSPACE, client.id_
        )
