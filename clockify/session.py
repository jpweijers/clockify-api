import requests
from clockify.apis.project import ProjectWrapper
from clockify.apis.user import UserWrapper
from clockify.apis.client_api import ClientWrapper
from clockify.apis.tag_api import TagWrapper


class ClockifySession(ClientWrapper, ProjectWrapper, UserWrapper, TagWrapper):
    def __init__(self, key: str) -> None:
        self.session = requests.Session()
        self.session.headers.update({"x-api-key": key})
