import requests
from clockify.apis.project import ProjectWrapper
from clockify.apis.user import UserWrapper


class ClockifySession(ProjectWrapper, UserWrapper):
    def __init__(self, key: str) -> None:
        self.session = requests.Session()
        self.session.headers.update({"x-api-key": key})
