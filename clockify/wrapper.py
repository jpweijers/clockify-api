import requests

from clockify.mapper import Mapper
from clockify.dto import DTO


class Wrapper:
    base_url: str
    session: requests.Session
    key: str
    workspace_id: str
    user_id: str

    def __inif__(self):
        pass

    def get(self, url: str) -> dict:
        res = self.session.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            raise requests.HTTPError(f"HTTP Error {res.status_code}: {res.reason}")

    def get_one(self, url: str, mapper: Mapper, dto: DTO) -> DTO:
        res = self.get(url)
        dto_dict = mapper().to_dto(res)
        return dto(**dto_dict)

    def get_list(self, url: str, mapper: Mapper, dto: DTO) -> DTO:
        res = self.get(url)
        dto_dicts = [mapper().to_dto(r) for r in res]
        return [dto(**d) for d in dto_dicts]
