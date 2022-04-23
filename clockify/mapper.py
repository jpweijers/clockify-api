from typing import Dict
from bidict import bidict


class Mapper:
    MAPPING_DICT = bidict()

    def to_api(self, input_dict: Dict) -> Dict:
        return {self.MAPPING_DICT[k]: v for k, v in input_dict.items()}

    def to_dto(self, input_dict: Dict) -> Dict:
        return {self.MAPPING_DICT.inverse[k]: v for k, v in input_dict.items()}
