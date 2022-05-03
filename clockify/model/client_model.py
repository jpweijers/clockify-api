from typing import Literal, Optional

from clockify.model.base_model import BaseModel


class Client(BaseModel):
    id_: str = None
    name: str
    workspace_id: str
    archived: bool = False

    class Config:
        fields = {"id_": "id", "workspace_id": "workspaceId"}


class ClientGetParams(BaseModel):
    archived: bool = None
    name: str = None
    page: int = 1
    page_size: int = 50
    sort_column: Literal["NAME"] = None
    sort_order: Literal["ASCENDING", "DESCENDING"] = None

    class Config:
        fields = {
            "page_size": "page-size",
            "sort_column": "sort-column",
            "sort_order": "sort-order",
        }


class ClientUpdateParams(BaseModel):
    class Config:
        fields = {"archive_projects": "archive-projects"}
