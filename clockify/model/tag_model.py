from typing import Optional
from pydantic import BaseModel


class Tag(BaseModel):
    id_: str = None
    name: str
    workspace_id: str
    archived: bool = False

    class Config:
        allow_population_by_field_name = True
        fields = {"id_": "id", "workspace_id": "workspaceId"}


class TagGetParams(BaseModel):
    name: Optional[str]
    archived: Optional[bool]
    page: int = 1
    page_size: int = 50

    class Config:
        allow_population_by_field_name = True
        fields = {"page_size": "page-size"}
