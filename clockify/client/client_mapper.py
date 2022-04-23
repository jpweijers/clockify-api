from clockify.mapper import Mapper
from bidict import bidict


class ClientMapper(Mapper):
    MAPPING_DICT = bidict(
        {
            "id_": "id",
            "name": "name",
            "workspace_id": "workspaceId",
            "archived": "archived",
            "address": "address",
        }
    )
