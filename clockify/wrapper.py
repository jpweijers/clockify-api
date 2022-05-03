from typing import List
import requests

from clockify.model.base_model import BaseModel


class Wrapper:
    def __init__(self, key: str) -> None:
        self.session = requests.Session()
        self.session.headers.update({"x-api-key": key})

    def __get(self, url: str, query: dict = {}) -> dict:
        res = self.session.get(url, params=query)
        if res.status_code == 200:
            return res.json()
        else:
            raise requests.HTTPError(
                f"HTTP ERROR {res.status_code}: {res.reason} - {res.text}"
            )

    def __post(self, url: str, payload: dict) -> dict:
        res = self.session.post(url, json=payload)
        if res.status_code == 201:
            return res.json()
        else:
            raise requests.HTTPError(
                f"HTTP ERROR {res.status_code}: {res.reason} - {res.text}"
            )

    def __delete(self, url: str) -> dict:
        res = self.session.delete(url)
        if res.status_code == 200:
            return res.json()
        else:
            raise requests.HTTPError(
                f"HTTP ERROR {res.status_code}: {res.reason} - {res.text}"
            )

    def __put(self, url: str, payload: dict, params: dict) -> dict:
        res = self.session.put(url, json=payload, params=params)
        if res.status_code == 200:
            return res.json()
        else:
            raise requests.HTTPError(
                f"HTTP ERROR {res.status_code}: {res.reason} - {res.text}"
            )

    def _get_one(self, url: str, schema: BaseModel) -> BaseModel:
        res = self.__get(url)
        return schema(**res)

    def _get_list(
        self, url: str, schema: BaseModel, params: BaseModel = None
    ) -> List[BaseModel]:
        if params:
            params = params.json_dict()
        else:
            params = {}
        res = self.__get(url, params)
        return [schema(**r) for r in res]

    def _create_one(self, url: str, object: BaseModel, schema: BaseModel) -> BaseModel:
        res = self.__post(url, object.json_dict())
        return schema(**res)

    def _delete_one(self, url: str, schema: BaseModel) -> BaseModel:
        res = self.__delete(url)
        return schema(**res)

    def _update_one(
        self, url: str, object: BaseModel, schema: BaseModel, params: BaseModel = None
    ) -> BaseModel:
        if params:
            params = params.json_dict()
        else:
            params = {}
        res = self.__put(url, object.json_dict(), params)
        return schema(**res)
