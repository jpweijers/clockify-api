from pydantic import BaseModel, Field
from typing import List, Literal, Optional


class CostRate_HourlyRate(BaseModel):
    amount: int
    currency: str


class Task(BaseModel):
    id_: str = None
    name: str
    project_id: str
    assignee_ids: List[str] = []
    estimate: str = None
    billable: bool = None
    hourly_rate: CostRate_HourlyRate = None
    cost_rate: CostRate_HourlyRate = None
    status: Literal["ACTIVE", "Done"] = None

    class Config:
        allow_population_by_field_name = True
        fields = {
            "id_": "id",
            "project_id": "projectId",
            "assignee_ids": "assigneIds",
            "hourly_rate": "hourlyRate",
            "cost_rate": "costRate",
        }


class TaskGetParams(BaseModel):
    is_active: Optional[bool]
    name: Optional[str]
    page: int = 1
    page_size: int = 50
    strict_name_search: Optional[bool]
    sort_column: Optional[Literal["ID", "NAME"]]
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]]

    class Config:
        allow_population_by_field_name = True
        fields = {
            "is_active": "is-active",
            "page_size": "page-size",
            "strict_name_search": "strict-name-search",
            "sort_column": "sort-column",
            "sort_order": "sort-order",
        }
