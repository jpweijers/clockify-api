from typing import List
from clockify.model.time_entry_model import TimeEntry
from clockify.config import BASE_URL
from clockify.wrapper import Wrapper


class TimeEntryWrapper(Wrapper):
    def get_time_entries(self, workspace_id: str) -> List[TimeEntry]:
        url = self.__url(workspace_id)
        return self.get_list(url, TimeEntry)

    def get_time_entry(self, workspace_id: str, time_entry_id: str) -> TimeEntry:
        url = self.__url(workspace_id, time_entry_id)
        return self.get_one(url, TimeEntry)

    def __url(self, workspace_id: str, time_entry_id: str = None) -> str:
        url = f"{BASE_URL}/workspaces/{workspace_id}/time-entries"
        if time_entry_id:
            url += f"/{time_entry_id}"
        return url
