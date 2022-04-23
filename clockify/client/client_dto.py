from dataclasses import dataclass
from clockify.dto import DTO


@dataclass
class ClientDTO(DTO):
    name: str
    id_: str = None
    workspace_id: str = None
    archived: str = None
    address: str = None
