from clockify.dto import DTO


class ClientDTO(DTO):
    __slots__ = [
        "id_",
        "name",
        "workspace_id",
        "archived",
        "address",
    ]

    def __init__(
        self,
        id_: str,
        name: str,
        workspace_id: str,
        archived: str,
        address: str,
    ) -> None:
        self.id_ = id_
        self.name = name
        self.workspace_id = workspace_id
        self.archived = archived
        self.address = address
