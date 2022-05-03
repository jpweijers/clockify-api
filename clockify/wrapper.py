from typing import List
import requests
from pydantic import BaseModel


class Wrapper:
    def __init__(self, key: str) -> None:
        self.session = requests.Session()
        self.session.headers.update({"x-api-key": key})

    def _get(self, url: str, query: dict = {}) -> dict:
        res = self.session.get(url, params=query)
        if res.status_code == 200:
            return res.json()
        else:
            raise requests.HTTPError(
                f"HTTP ERROR {res.status_code}: {res.reason} - {res.text}"
            )

    def _post(self, url: str, payload: dict) -> dict:
        res = self.session.post(url, json=payload)
        if res.status_code == 201:
            return res.json()
        else:
            raise requests.HTTPError(
                f"HTTP ERROR {res.status_code}: {res.reason} - {res.text}"
            )

    def _delete(self, url: str) -> dict:
        res = self.session.delete(url)
        if res.status_code == 200:
            return res.json()
        else:
            raise requests.HTTPError(
                f"HTTP ERROR {res.status_code}: {res.reason} - {res.text}"
            )

    def _put(self, url: str, payload: dict) -> dict:
        res = self.session.put(url, json=payload)
        if res.status_code == 200:
            return res.json()
        else:
            raise requests.HTTPError(
                f"HTTP ERROR {res.status_code}: {res.reason} - {res.text}"
            )

    def get_one(self, url: str, schema: BaseModel) -> BaseModel:
        res = self._get(url)
        return schema(**res)

    def get_list(
        self, url: str, schema: BaseModel, params: BaseModel = None
    ) -> List[BaseModel]:
        try:
            params = params.dict(exclude_unset=True)
        except:
            params = {}
        res = self._get(url, params)
        return [schema(**r) for r in res]

    def create_one(self, url: str, object: BaseModel, schema: BaseModel) -> BaseModel:
        res = self._post(url, object.dict(exclude_unset=True, by_alias=True))
        return schema(**res)

    def delete_one(self, url: str, schema: BaseModel) -> BaseModel:
        res = self._delete(url)
        return schema(**res)

    def update_one(self, url: str, object: BaseModel, schema: BaseModel) -> BaseModel:
        res = self._put(url, object.dict(exclude_unset=True, by_alias=True))
        return schema(**res)
