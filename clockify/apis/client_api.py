from typing import List
from clockify.config import BASE_URL
from clockify.model.client_model import Client
from clockify.wrapper import Wrapper


class ClientWrapper(Wrapper):
    def get_clients(self, workspace_id: str) -> List[Client]:
        url = self.__url(workspace_id)
        return self.get_list(url, Client)

    def get_client(self, workspace_id: str, client_id: str) -> Client:
        url = self.__url(workspace_id, client_id)
        return self.get_one(url, Client)

    def create_client(self, client: Client) -> Client:
        url = self.__url(client.workspace_id)
        return self.create_one(url, client, Client)

    def delete_client(self, workspace_id: str, client_id: str) -> Client:
        url = self.__url(workspace_id, client_id)
        return self.delete_one(url, Client)

    def update_client(self, client: Client) -> Client:
        url = self.__url(client.workspace_id, client.id_)
        return self.update_one(url, client, Client)

    def __url(self, workspace_id: str, client_id: str = None) -> str:
        url = f"{BASE_URL}/workspaces/{workspace_id}/clients"
        if client_id:
            url += f"/{client_id}"
        return url
