from pydantic import BaseModel


class Tag(BaseModel):
    id_: str = None
    name: str
    workspace_id: str
    archived: bool = False

    class Config:
        allow_population_by_field_name = True
        fields = {"id_": "id", "workspace_id": "workspaceId"}

    def json(self):
        return super().json(exclude_unset=True)
