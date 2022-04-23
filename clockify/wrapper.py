import requests
import os
import json

from requests.exceptions import HTTPError

from user import UserMapper, UserDTO

CLOCKIFY_API_KEY = os.environ.get("CLOCKIFY_API_KEY")


class ClockifyWrapper:
    ROOT = "https://api.clockify.me/api/v1"
    USER_PATH = "user"

    def __init__(self, api_key) -> None:
        self.headers = {"x-api-key": api_key}
        pass

    def get_current_user(self):
        url = "/".join([self.ROOT, self.USER_PATH])
        res = requests.get(url, headers=self.headers)

        if res.status_code == 200:
            api_dict = res.json()
            dto_dict = UserMapper().to_dto(api_dict)
            return UserDTO(**dto_dict)

        else:
            raise HTTPError(f"HTTP Error {res.status_code}: {res.reason}")


clockify = ClockifyWrapper(CLOCKIFY_API_KEY)
user = clockify.get_current_user()
