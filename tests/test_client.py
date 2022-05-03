from random import randint, sample
import pytest
from requests.exceptions import HTTPError
from tests.test import ClockifyTestCase

from clockify.session import ClockifySession
from clockify.model.client_model import Client, ClientGetParams, ClientUpdateParams


class TestClients(ClockifyTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = ClockifySession(cls.KEY)
        client_names = [f"Test Client #{i}" for i in sample(range(0, 99999), 5)]
        for name in client_names:
            client = Client(name=name, workspace_id=cls.WORKSPACE)
            cls.session.client.create_client(client)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        clients = cls.session.client.get_clients(cls.WORKSPACE)
        for client in clients:
            cls.session.client.delete_client(cls.WORKSPACE, client.id_)

    def test_get_list_of_clients(self):
        clients = self.session.client.get_clients(self.WORKSPACE)
        # self.fail(projects)
        for client in clients:
            self.assertIsInstance(client, Client)

    def test_get_list_of_clients_fail(self):
        self.assertRaises(HTTPError, self.session.client.get_clients, "fakeworkspace")

    def test_get_list_of_clients_with_query(self):
        query = ClientGetParams(sort_order="ASCENDING", page_size=1)
        clients = self.session.client.get_clients(self.WORKSPACE, query)
        for client in clients:
            self.assertIsInstance(client, Client)

    def test_get_client_by_id(self):
        client = Client(
            name=f"Test Get {randint(0, 99999)}", workspace_id=self.WORKSPACE
        )
        client = self.session.client.create_client(client)
        client = self.session.client.get_client(self.WORKSPACE, client.id_)
        self.assertIsInstance(client, Client)

    def test_get_client_by_id_fail(self):
        self.assertRaises(
            HTTPError,
            self.session.client.get_client,
            self.WORKSPACE,
            self.NON_EXISTING_CLIENT,
        )

    def test_create_client(self):
        client = Client(
            name=f"Test Create {randint(0, 9999)}", workspace_id=self.WORKSPACE
        )
        client = self.session.client.create_client(client)
        self.assertIsInstance(client, Client)

    def test_delete_client(self):
        client = Client(
            name=f"Test Delete {randint(0, 9999)}", workspace_id=self.WORKSPACE
        )
        client = self.session.client.create_client(client)
        client = self.session.client.delete_client(self.WORKSPACE, client.id_)
        self.assertIsInstance(client, Client)

    def test_delete_client_fail(self):
        self.assertRaises(
            HTTPError,
            self.session.client.delete_client,
            self.WORKSPACE,
            "this is not a client ID",
        )

    def test_update_client(self):
        client = Client(
            name=f"Test Client {randint(0, 9999)}", workspace_id=self.WORKSPACE
        )
        client = self.session.client.create_client(client)
        client.archived = True
        params = ClientUpdateParams(archive_projects=True)
        client = self.session.client.update_client(client, params)
        self.assertIsInstance(client, Client)
