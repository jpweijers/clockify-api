from typing import List
from clockify.user.settings.summaryreportsettings.summaryreportsettings_dto import (
    SummaryreportsettingsDTO,
)
from clockify.user.settings.summaryreportsettings.summaryreportsettings_mapper import (
    SummaryreportsettingsMapper,
)


class SettingsDTO:
    __slots__ = [
        "week_start",
        "time_zone",
        "time_format",
        "date_format",
        "send_newsletter",
        "weekly_updates",
        "long_running",
        "scheduled_reports",
        "approval",
        "pto",
        "alerts",
        "reminders",
        "time_tracking_manual",
        "summary_report_settings",
        "is_compact_view_on",
        "dashboard_selection",
        "dashboard_view_type",
        "dashboard_pin_to_top",
        "project_list_collapse",
        "collapse_all_project_lists",
        "group_similar_entries_disabled",
        "my_start_of_day",
        "project_picker_task_filter",
        "lang",
        "multi_factor_enabled",
        "theme",
        "scheduling",
    ]

    def __init__(
        self,
        week_start: str,
        time_zone: str,
        time_format: str,
        date_format: str,
        send_newsletter: str,
        weekly_updates: str,
        long_running: str,
        scheduled_reports: str,
        approval: str,
        pto: str,
        alerts: str,
        reminders: str,
        time_tracking_manual: str,
        summary_report_settings: List[SummaryreportsettingsDTO],
        is_compact_view_on: str,
        dashboard_selection: str,
        dashboard_view_type: str,
        dashboard_pin_to_top: str,
        project_list_collapse: str,
        collapse_all_project_lists: str,
        group_similar_entries_disabled: str,
        my_start_of_day: str,
        project_picker_task_filter: str,
        lang: str,
        multi_factor_enabled: str,
        theme: str,
        scheduling: str,
    ) -> None:
        summary_report_settings_dto = SummaryreportsettingsMapper().to_dto(
            summary_report_settings
        )

        self.week_start = week_start
        self.time_zone = time_zone
        self.time_format = time_format
        self.date_format = date_format
        self.send_newsletter = send_newsletter
        self.weekly_updates = weekly_updates
        self.long_running = long_running
        self.scheduled_reports = scheduled_reports
        self.approval = approval
        self.pto = pto
        self.alerts = alerts
        self.reminders = reminders
        self.time_tracking_manual = time_tracking_manual
        self.summary_report_settings = SummaryreportsettingsDTO(
            **summary_report_settings_dto
        )
        self.is_compact_view_on = is_compact_view_on
        self.dashboard_selection = dashboard_selection
        self.dashboard_view_type = dashboard_view_type
        self.dashboard_pin_to_top = dashboard_pin_to_top
        self.project_list_collapse = project_list_collapse
        self.collapse_all_project_lists = collapse_all_project_lists
        self.group_similar_entries_disabled = group_similar_entries_disabled
        self.my_start_of_day = my_start_of_day
        self.project_picker_task_filter = project_picker_task_filter
        self.lang = lang
        self.multi_factor_enabled = multi_factor_enabled
        self.theme = theme
        self.scheduling = scheduling
