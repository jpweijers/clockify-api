from typing import List
from clockify.config import BASE_URL
from clockify.model.client_model import Client, ClientGetParams, ClientUpdateParams
from clockify.wrapper import Wrapper


class ClientApi(Wrapper):
    def get_clients(
        self, workspace_id: str, params: ClientGetParams = ClientGetParams()
    ) -> List[Client]:
        """Return a list of clients.

        Args:
            workspace_id (str): ID of the Clockify workspace.
            params (ClientGetParams, optional): Path Parameters. Defaults to ClientGetParams().

        Returns:
            List[Client]: List of Client objects
        """
        url = self.__url(workspace_id)
        return self._get_list(url, Client, params)

    def get_client(self, workspace_id: str, client_id: str) -> Client:
        """Return one client Object

        Args:
            workspace_id (str): ID of the clockify workspace
            client_id (str): Id of the clockify client

        Returns:
            Client: A Client object.
        """
        url = self.__url(workspace_id, client_id)
        return self._get_one(url, Client)

    def create_client(self, client: Client) -> Client:
        """Create one client and return it as a object.

        Args:
            client (Client): Client object.

        Returns:
            Client: Client object.
        """
        url = self.__url(client.workspace_id)
        return self._create_one(url, client, Client)

    def delete_client(self, workspace_id: str, client_id: str) -> Client:
        """Delete a Client, and return it as a Client object.

        Args:
            workspace_id (str): ID of the clockify workspace.
            client_id (str): ID of the clockify client.

        Returns:
            Client: Deleted Client object.
        """
        url = self.__url(workspace_id, client_id)
        return self._delete_one(url, Client)

    def update_client(
        self, client: Client, params: ClientUpdateParams = ClientUpdateParams()
    ) -> Client:
        """Update a Client and return it as a Client object.

        Args:
            client (Client): Client object.
            params (ClientUpdateParams, optional): Path parameters. Defaults to ClientUpdateParams().

        Returns:
            Client: Updated Client object.
        """
        url = self.__url(client.workspace_id, client.id_)
        return self._update_one(url, client, Client, params)

    def __url(self, workspace_id: str, client_id: str = None) -> str:
        """Return generated url

        Args:
            workspace_id (str): ID of the Clockify workspace.
            client_id (str, optional): ID of the Clockify Client. Defaults to None.

        Returns:
            str: Generated url
        """
        url = f"{BASE_URL}/workspaces/{workspace_id}/clients"
        if client_id:
            url += f"/{client_id}"
        return url
