import requests
from clockify.apis.project_api import ProjectApi
from clockify.apis.task_api import TaskApi
from clockify.apis.time_entry_api import TimeEntryApi
from clockify.apis.user import UserWrapper
from clockify.apis.client_api import ClientApi
from clockify.apis.tag_api import TagApi


class ClockifySession(
    UserWrapper,
):
    def __init__(self, key: str) -> None:
        """Initialize a Clockfiy Session

        Args:
            key (str): Your Clockify API Key
        """
        self.session = requests.Session()
        self.session.headers.update({"x-api-key": key})

        self.client = ClientApi(key)
        self.project = ProjectApi(key)
        self.tag = TagApi(key)
        self.task = TaskApi(key)
        self.time_entry = TimeEntryApi(key)
