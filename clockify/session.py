import requests
from clockify.apis.project import ProjectWrapper
from clockify.apis.task_api import TaskWrapper
from clockify.apis.time_entry_api import TimeEntryWrapper
from clockify.apis.user import UserWrapper
from clockify.apis.client_api import ClientApi
from clockify.apis.tag_api import TagWrapper


class ClockifySession(
    ProjectWrapper,
    UserWrapper,
    TagWrapper,
    TaskWrapper,
    TimeEntryWrapper,
):
    def __init__(self, key: str) -> None:
        self.session = requests.Session()
        self.session.headers.update({"x-api-key": key})

        self.client = ClientApi(key)
