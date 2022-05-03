from datetime import datetime
from pydantic import BaseModel


class BaseModel(BaseModel):
    class Config:
        allow_population_by_field_name = True

    def dict(self, **kwargs):
        d = super().dict(exclude_unset=True, by_alias=True, **kwargs)
        for k, v in d.items():
            if type(v) == datetime:
                d[k] = v.isoformat()[:19] + "Z"
        return d
