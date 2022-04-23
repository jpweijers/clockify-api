from clockify.mapper import Mapper
from bidict import bidict


class ClientMapper(Mapper):
    MAPPING_DICT = bidict(
        {
            "name": "name",
            "id_": "id",
            "workspace_id": "workspaceId",
            "archived": "archived",
            "address": "address",
        }
    )
