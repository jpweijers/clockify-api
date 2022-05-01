from pydantic import BaseModel, Field
from typing import Any, List, Literal


class TimeEntry(BaseModel):
    description: str = ""
    user_id: str
    workspace_id: str
    id_: str = None
    billable: bool = None
    is_locked: bool = None
    project_id: str = None
    tag_ids: List[str] = []
    task_id: str = None
    time_interval: "TimeInterval"
    custom_field_values: List["CustomFieldValue"] = []

    class Config:
        allow_population_by_field_name = True
        fields = {
            "id_": "id",
            "is_locked": "isLocked",
            "project_id": "projectId",
            "tag_ids": "tagIds",
            "task_id": "taskId",
            "time_interval": "timeInterval",
            "user_id": "userId",
            "workspace_id": "workspaceId",
            "custom_field_values": "customFieldValues",
        }


class TimeInterval(BaseModel):
    duration: str
    end: str
    start: str


class CustomFieldValue(BaseModel):
    custom_field_id: str
    time_entry_id: str
    value: Any
    name: str
    type_: Literal[
        "TXT",
        "NUMBER",
        "DROPDOWN_SINGLE",
        "DROPDOWN_MULTIPLE",
        "CHECKBOX",
        "LINK",
    ]

    class Config:
        allow_population_by_field_name = True
        fields = {
            "custom_field_id": "customFieldId",
            "time_entry_id": "timeEntryId",
            "type_": "type",
        }
