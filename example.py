import os

from clockify.session import ClockifySession

CLOCKIFY_API_KEY = os.environ.get("CLOCKIFY_API_KEY")

session = ClockifySession(CLOCKIFY_API_KEY)
user = session.get_current_user()
print(user)


data = """{
	"id": "626399702993d4192cb61234",
	"email": "test@example.com",
	"name": "Test User",
	"memberships": [
		{
			"userId": "626399702993d4192cb61234",
			"hourlyRate": null,
			"costRate": null,
			"targetId": "626399702993d4192cb61a9a",
			"membershipType": "WORKSPACE",
			"membershipStatus": "ACTIVE"
		}
	],
	"profilePicture": "https://img.clockify.me/no-user-image.png",
	"activeWorkspace": "626399702993d4192cb61a9a",
	"defaultWorkspace": "626399702993d4192cb61a9a",
	"settings": {
		"weekStart": "MONDAY",
		"timeZone": "Europe/Amsterdam",
		"timeFormat": "HOUR24",
		"dateFormat": "DD/MM/YYYY",
		"sendNewsletter": false,
		"weeklyUpdates": true,
		"longRunning": true,
		"scheduledReports": true,
		"approval": true,
		"pto": true,
		"alerts": true,
		"reminders": true,
		"timeTrackingManual": false,
		"summaryReportSettings": {
			"group": "Project",
			"subgroup": "Time Entry"
		},
		"isCompactViewOn": false,
		"dashboardSelection": "ME",
		"dashboardViewType": "PROJECT",
		"dashboardPinToTop": false,
		"projectListCollapse": 50,
		"collapseAllProjectLists": false,
		"groupSimilarEntriesDisabled": false,
		"myStartOfDay": "09:00",
		"projectPickerTaskFilter": false,
		"lang": "EN",
		"multiFactorEnabled": false,
		"theme": "DEFAULT",
		"scheduling": true
	},
	"status": "ACTIVE"
}"""
