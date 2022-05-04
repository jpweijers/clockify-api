from typing import List
from clockify.model.time_entry_model import (
    TimeEntry,
    TimeEntryGetParams,
    CreateTimeEntryDTO,
)
from clockify.config import BASE_URL
from clockify.wrapper import Wrapper


class TimeEntryApi(Wrapper):
    def get_time_entries(
        self,
        workspace_id: str,
        user_id: str,
        params: TimeEntryGetParams = TimeEntryGetParams(),
    ) -> List[TimeEntry]:
        """Return list of TimeEntry object.

        Args:
            workspace_id (str): ID of the clockify workspace.
            user_id (str): ID of the clockify user.
            params (TimeEntryGetParams, optional): Path params. Defaults to TimeEntryGetParams().

        Returns:
            List[TimeEntry]: List of TimeEntry objects.
        """
        url = f"{BASE_URL}/workspaces/{workspace_id}/user/{user_id}/time-entries"
        return self._get_list(url, TimeEntry, params)

    def get_time_entry(self, workspace_id: str, time_entry_id: str) -> TimeEntry:
        """Return one TimeEntry object

        Args:
            workspace_id (str): ID of the clockify workspace.
            time_entry_id (str): ID of the clockify time-entry.

        Returns:
            TimeEntry: TimeEntry object.
        """
        url = f"{BASE_URL}/workspaces/{workspace_id}/time-entries/{time_entry_id}"
        return self._get_one(url, TimeEntry)

    def add_time_entry(
        self, workspace_id: str, user_id: str, time_entry: CreateTimeEntryDTO
    ) -> TimeEntry:
        """Add new TimeEntry and return it as a TimeEntry object.

        Args:
            workspace_id (str): ID of the clockify workspace.
            user_id (str): ID of the clockify user.
            time_entry (CreateTimeEntryDTO): TimeEntry to create.

        Returns:
            TimeEntry: Added TimeEntry object.
        """
        url = f"{BASE_URL}/workspaces/{workspace_id}/user/{user_id}/time-entries"
        return self._create_one(url, time_entry, TimeEntry)
