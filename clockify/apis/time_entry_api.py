from typing import List
from clockify.model.time_entry_model import TimeEntry
from clockify.config import BASE_URL
from clockify.wrapper import Wrapper


class TimeEntryWrapper(Wrapper):
    def get_time_entries(self, workspace_id: str, user_id: str) -> List[TimeEntry]:
        url = f"{BASE_URL}/workspaces/{workspace_id}/user/{user_id}/time-entries"
        return self._get_list(url, TimeEntry)

    def get_time_entry(self, workspace_id: str, time_entry_id: str) -> TimeEntry:
        url = f"{BASE_URL}/workspaces/{workspace_id}/time-entries/{time_entry_id}"
        return self._get_one(url, TimeEntry)
