from dataclasses import dataclass
from enum import Enum
from clockify.dto import DTO


class SortOrder(Enum):
    DESCENDING = "DESCENDING"
    ASCENDING = "DESCENDING"


class SortColumn(Enum):
    NAME = "NAME"
    ID = "ID"


@dataclass
class ClientDTO(DTO):
    name: str
    id_: str = None
    workspace_id: str = None
    archived: str = None
    address: str = None


@dataclass
class ClientQueryDTO(DTO):
    archived: bool = None
    name: str = None
    page: int = 1
    page_size: int = 50
    sort_column: SortColumn = None
    sort_order: SortOrder = None
