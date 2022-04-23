import dataclasses
from attr import asdict
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

    def get(self, url: str, query: dict = {}) -> dict:
        res = self.session.get(url, params=query)
        if res.status_code == 200:
            return res.json()
        else:
            raise requests.HTTPError(
                f"HTTP ERROR {res.status_code}: {res.reason} - {res.text}"
            )

    def post(self, url: str, api_dto: dict):
        res = self.session.post(url, json=api_dto)
        if res.status_code == 201:
            return res.json()
        else:
            raise requests.HTTPError(
                f"HTTP ERROR {res.status_code}: {res.reason} - {res.text}"
            )

    def delete(self, url: str):
        res = self.session.delete(url)
        if res.status_code == 200:
            return res.json()
        else:
            raise requests.HTTPError(
                f"HTTP ERROR {res.status_code}: {res.reason} - {res.text}"
            )

    def get_one(self, url: str, mapper: Mapper, dto: DTO) -> DTO:
        res = self.get(url)
        dto_dict = mapper.to_dto(res)
        return dto(**dto_dict)

    def get_list(
        self,
        url: str,
        mapper: Mapper,
        dto: DTO,
        query_mapper: Mapper = None,
        query_dto: DTO = None,
    ) -> DTO:
        query = {}
        if query_mapper and query_dto:
            query = query_mapper.to_api(query_dto)
        res = self.get(url, query)
        dto_dicts = [mapper.to_dto(r) for r in res]

        return [dto(**d) for d in dto_dicts]

    def create_one(self, url, data: DTO, mapper: Mapper, dto: DTO) -> DTO:
        api_dto = mapper.to_api(data)
        res = self.post(url, api_dto)
        dto_dict = mapper.to_dto(res)
        return dto(**dto_dict)

    def delete_one(self, url, mapper: Mapper, dto: DTO) -> DTO:
        res = self.delete(url)
        dto_dict = mapper.to_dto(res)
        return dto(**dto_dict)
