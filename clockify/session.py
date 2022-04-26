import requests
from clockify.apis.project import ProjectWrapper
from clockify.apis.user import UserWrapper
from clockify.apis.client_api import ClientWrapper


class ClockifySession(ClientWrapper, ProjectWrapper, UserWrapper):
    def __init__(self, key: str) -> None:
        self.session = requests.Session()
        self.session.headers.update({"x-api-key": key})
