from typing import Any, List, Optional

from pydantic import BaseModel

from clockify.model.user_model import User
from clockify.model.tag_model import Tag
from clockify.model.task_model import Task
from clockify.model.project_model import Project


class TimeInterval(BaseModel):
    start: Optional[str]
    end: Optional[str]
    duration: Optional[str]


class HourlyRate(BaseModel):
    amount: Optional[float]
    currency: Optional[str]


class TimeEntry(BaseModel):
    id_: Optional[str]
    description: str
    tags: Optional[List[Tag]]
    tag_ids: Optional[List[str]]
    user: Optional[User]
    user_id: Optional[str]
    billable: Optional[bool]
    task: Optional[Task]
    task_id: Optional[str]
    project: Optional[Project]
    project_id: Optional[str]
    time_interval: Optional[TimeInterval]
    workspace_id: Optional[str]
    hourly_rate: Optional[HourlyRate]
    custom_field_values: List[Any]
    is_locked: Optional[bool]

    class Config:
        allow_population_by_field_name = True
        fields = {
            "id_": "id",
            "tag_ids": "tagIds",
            "user_id": "userId",
            "task_id": "taskId",
            "project_id": "projectId",
            "time_interval": "timeInterval",
            "workspace_id": "workspaceId",
            "hourly_rate": "hourlyRate",
            "custom_field_values": "customFieldValues",
            "is_locked": "isLocked",
        }


class TimeEntryGetParams(BaseModel):
    hydrated: Optional[bool]
