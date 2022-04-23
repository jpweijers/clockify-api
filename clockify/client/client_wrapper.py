from typing import List
from clockify.wrapper import Wrapper
from clockify.client.client_dto import ClientDTO
from clockify.client.client_mapper import ClientMapper


class ClientWrapper(Wrapper):
    def __init__(self):
        pass

    def get_clients(self, workspace_id: str) -> List[ClientDTO]:
        path = f"workspaces/{workspace_id}/clients"
        url = "/".join([self.base_url, path])
        return self.get_list(url, ClientMapper(), ClientDTO)

    def get_client_by_id(self, workspace_id: str, client_id: str) -> ClientDTO:
        url = f"{self.base_url}/workspaces/{workspace_id}/clients/{client_id}"
        return self.get_one(url, ClientMapper(), ClientDTO)

    def create_client(self, workspace_id: str, client: ClientDTO) -> ClientDTO:
        url = f"{self.base_url}/workspaces/{workspace_id}/clients"
        return self.create_one(url, client, ClientMapper(), ClientDTO)

    def delete_client(self, workspace_id: str, client_id: str) -> ClientDTO:
        url = f"{self.base_url}/workspaces/{workspace_id}/clients/{client_id}"
        return self.delete_one(url, ClientMapper(), ClientDTO)
