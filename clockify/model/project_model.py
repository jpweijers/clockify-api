from pydantic import BaseModel, Required

from typing import Optional, List


class HourlyRate(BaseModel):
    amount: Optional[str]
    currency: Optional[str]

    class Config:
        allow_population_by_field_name = True
        fields = {"ammount": "amount", "amount": "amount"}


class MemberShip(BaseModel):
    user_Id: Optional[str]
    hourly_Rate: Optional[str]
    cost_Rate: Optional[str]
    target_Id: Optional[str]
    membership_Type: Optional[str]
    membership_Status: Optional[str]

    class Config:
        allow_population_by_field_name = True
        fields = {
            "user_Id": "userId",
            "hourly_Rate": "hourlyRate",
            "cost_Rate": "costRate",
            "target_Id": "targetId",
            "membership_Type": "membershipType",
            "membership_Status": "membershipStatus",
        }


class Estimate(BaseModel):
    estimate: Optional[str]
    type: Optional[str]

    class Config:
        fields = {"estimate": "estimate", "type": "type"}


class TimeEstimate(BaseModel):
    estimate: Optional[str]
    type: Optional[str]
    reset_option: Optional[str]
    active: Optional[bool]
    include_non_billable: Optional[bool]

    class Config:
        allow_population_by_field_name = True
        fields = {
            "estimate": "estimate",
            "type": "type",
            "reset_option": "resetOption",
            "active": "active",
            "include_non_billable": "includeNonBillable",
        }


class Project(BaseModel):
    name: str
    workspace_id: str
    id_: Optional[str]
    hourly_rate: Optional[HourlyRate]
    client_id: Optional[str]
    billable: Optional[bool]
    memberships: Optional[List[MemberShip]]
    color: Optional[str]
    estimate: Optional[Estimate]
    archived: Optional[bool]
    duration: Optional[str]
    client_name: Optional[str]
    note: Optional[str]
    cost_rate: Optional[str]
    time_estimate: Optional[TimeEstimate]
    budget_estimate: Optional[str]
    template: Optional[bool]
    public_: Optional[bool]

    class Config:
        allow_population_by_field_name = True
        fields = {
            "id_": "id",
            "name": "name",
            "hourly_rate": "hourlyRate",
            "client_id": "clientId",
            "workspace_id": "workspaceId",
            "billable": "billable",
            "memberships": "memberships",
            "color": "color",
            "estimate": "estimate",
            "archived": "archived",
            "duration": "duration",
            "client_name": "clientName",
            "note": "note",
            "cost_rate": "costRate",
            "time_estimate": "timeEstimate",
            "budget_estimate": "budgetEstimate",
            "template": "template",
            "public_": "public",
        }
