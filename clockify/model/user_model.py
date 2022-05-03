from typing import List, Literal, Optional

from clockify.model.base_model import BaseModel


class Membership(BaseModel):
    user_id: Optional[str]
    hourly_rate: Optional[float]
    cost_rate: Optional[float]
    target_id: Optional[str]
    membership_type: Optional[str]
    membership_status: Optional[str]

    class Config:
        fields = {
            "user_id": "userId",
            "hourly_rate": "hourlyRate",
            "cost_rate": "costRate",
            "target_id": "targetId",
            "membership_type": "membershipType",
            "membership_status": "membershipStatus",
        }


class SummaryReportSettings(BaseModel):
    group: Optional[str]
    subgroup: Optional[str]


class Settings(BaseModel):
    week_start: Optional[
        Literal[
            "MONDAY",
            "TUESDAY",
            "WEDNESDAY",
            "THURSDAY",
            "FRIDAY",
            "SATURDAY",
            "SUNDAY",
        ]
    ]
    time_zone: Optional[str]
    time_format: Optional[str]
    date_format: Optional[str]
    send_newsletter: Optional[str]
    weekly_updates: Optional[str]
    long_running: Optional[str]
    scheduled_reports: Optional[str]
    approval: Optional[str]
    pto: Optional[str]
    alerts: Optional[str]
    reminders: Optional[str]
    time_tracking_manual: Optional[str]
    summary_report_settings: Optional[SummaryReportSettings]
    is_compact_view_on: Optional[str]
    dashboard_selection: Optional[str]
    dashboard_view_type: Optional[str]
    dashboard_pin_to_top: Optional[str]
    project_list_collapse: Optional[str]
    collapse_all_project_lists: Optional[str]
    group_similar_entries_disabled: Optional[str]
    my_start_of_day: Optional[str]
    project_picker_task_filter: Optional[str]
    lang: Optional[str]
    multi_factor_enabled: Optional[str]
    theme: Optional[str]
    scheduling: Optional[str]

    class Config:
        fields = {
            "week_start": "weekStart",
            "time_zone": "timeZone",
            "time_format": "timeFormat",
            "date_format": "dateFormat",
            "send_newsletter": "sendNewsletter",
            "weekly_updates": "weeklyUpdates",
            "long_running": "longRunning",
            "scheduled_reports": "scheduledReports",
            "approval": "approval",
            "pto": "pto",
            "alerts": "alerts",
            "reminders": "reminders",
            "time_tracking_manual": "timeTrackingManual",
            "summary_report_settings": "summaryReportSettings",
            "is_compact_view_on": "isCompactViewOn",
            "dashboard_selection": "dashboardSelection",
            "dashboard_view_type": "dashboardViewType",
            "dashboard_pin_to_top": "dashboardPinToTop",
            "project_list_collapse": "projectListCollapse",
            "collapse_all_project_lists": "collapseAllProjectLists",
            "group_similar_entries_disabled": "groupSimilarEntriesDisabled",
            "my_start_of_day": "myStartOfDay",
            "project_picker_task_filter": "projectPickerTaskFilter",
            "lang": "lang",
            "multi_factor_enabled": "multiFactorEnabled",
            "theme": "theme",
            "scheduling": "scheduling",
        }


class User(BaseModel):
    id_: Optional[str]
    email: Optional[str]
    name: str
    memberships: Optional[List[Membership]]
    profile_picture: Optional[str]
    active_workspace: Optional[str]
    default_workspace: Optional[str]
    settings: Optional[Settings]
    status: Optional[str]

    class Config:
        fields = {
            "id_": "id",
            "email": "email",
            "name": "name",
            "memberships": "memberships",
            "profile_picture": "profilePicture",
            "active_workspace": "activeWorkspace",
            "default_workspace": "defaultWorkspace",
            "settings": "settings",
            "status": "status",
        }
