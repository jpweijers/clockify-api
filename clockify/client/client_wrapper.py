from typing import List
from clockify.wrapper import Wrapper
from clockify.client.client_dto import ClientDTO
from clockify.client.client_mapper import ClientMapper


class ClientWrapper(Wrapper):
    def __init__(self):
        pass

    def get_clients(self, workspace_id: str) -> List[ClientDTO]:
        path = f"workspaces/{workspace_id}/clients"
        url = "/".join([self.BASE_URL, path])
        return self.get_list(url, ClientMapper, ClientDTO)
