import requests

from clockify.mapper import Mapper
from clockify.dto import DTO


class Wrapper:
    session: requests.Session
    key: str
    workspace_id: str

    def get(self, url: str) -> dict:
        res = self.session.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            raise requests.HTTPError(f"HTTP Error {res.status_code}: {res.reason}")

    def get_list(self, url: str, mapper: Mapper, dto: DTO) -> DTO:
        res = self.get(url)
        dtos = [mapper().to_dto(r) for r in res]
        return [dto(**d) for d in dtos]
