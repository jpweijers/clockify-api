from clockify.mapper import Mapper
from bidict import bidict


class SettingsMapper(Mapper):
    MAPPING_DICT = bidict(
        {
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
    )
