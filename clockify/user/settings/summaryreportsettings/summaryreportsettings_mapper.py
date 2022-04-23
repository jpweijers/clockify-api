from clockify.mapper import Mapper
from bidict import bidict


class SummaryreportsettingsMapper(Mapper):
    MAPPING_DICT = bidict({"group": "group", "subgroup": "subgroup"})
