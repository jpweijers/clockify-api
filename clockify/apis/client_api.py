from typing import List
from clockify.config import BASE_URL
from clockify.model.client_model import Client, ClientGetParams, ClientUpdateParams
from clockify.wrapper import Wrapper


class ClientApi(Wrapper):
    def get_clients(
        self, workspace_id: str, params: ClientGetParams = ClientGetParams()
    ) -> List[Client]:
        url = self.__url(workspace_id)
        return self._get_list(url, Client, params)

    def get_client(self, workspace_id: str, client_id: str) -> Client:
        url = self.__url(workspace_id, client_id)
        return self._get_one(url, Client)

    def create_client(self, client: Client) -> Client:
        url = self.__url(client.workspace_id)
        return self._create_one(url, client, Client)

    def delete_client(self, workspace_id: str, client_id: str) -> Client:
        url = self.__url(workspace_id, client_id)
        return self._delete_one(url, Client)

    def update_client(
        self, client: Client, params: ClientUpdateParams = ClientUpdateParams()
    ) -> Client:
        url = self.__url(client.workspace_id, client.id_)
        return self._update_one(url, client, Client, params)

    def __url(self, workspace_id: str, client_id: str = None) -> str:
        url = f"{BASE_URL}/workspaces/{workspace_id}/clients"
        if client_id:
            url += f"/{client_id}"
        return url
