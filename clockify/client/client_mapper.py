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


class ClientQueryMapper(Mapper):
    MAPPING_DICT = bidict(
        {
            "archived": "archived",
            "name": "name",
            "page": "page",
            "page_size": "page-size",
            "sort_column": "sort-column",
            "sort_order": "sort-order",
        }
    )
