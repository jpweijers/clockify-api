from bidict import bidict
from dataclasses import asdict
from enum import Enum
from clockify.dto import DTO


class Mapper:
    MAPPING_DICT = bidict()

    def dict_factory(self, data):
        def convert_value(obj):
            if isinstance(obj, Enum):
                return obj.value
            return obj

        return dict((k, convert_value(v)) for k, v in data)

    def to_api(self, input: DTO) -> dict:
        input_dict = asdict(input, dict_factory=self.dict_factory)
        return {self.MAPPING_DICT[k]: v for k, v in input_dict.items()}

    def to_dto(self, input_dict: dict) -> dict:
        return {self.MAPPING_DICT.inverse[k]: v for k, v in input_dict.items()}
