from datetime import datetime
from pydantic import BaseModel


class BaseModel(BaseModel):
    class Config:
        allow_population_by_field_name = True

    def json_dict(self, **kwargs):
        """
        Parse dict so that it can be json serialized by Python's json module
        """
        d = super().dict(exclude_unset=True, by_alias=True, **kwargs)
        for k, v in d.items():
            if type(v) == datetime:
                d[k] = v.isoformat()[:19] + "Z"
        return d
