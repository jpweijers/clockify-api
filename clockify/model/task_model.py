from pydantic import BaseModel, Field
from typing import List, Literal


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
