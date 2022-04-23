from bidict import bidict
from typing import List, Dict


class MembershipDTO:
    __slots__ = ["id_"]

    def __init__(
        self,
        id_: int,
    ):
        self.id_ = id_


class Membership:
    id_: int


class SettingsDTO:
    __slots__ = ["week_start"]

    def __init__(self, week_start: str):
        self.week_start = week_start


class Settings:
    week_start: str

    def __init__(self, settings: SettingsDTO) -> None:
        self.week_start = settings.week_start


class UserMeta:
    id_: int
    email: str
    name: str
    memberships: List[Membership] = []


class UserDTO:
    __slots__ = [
        "id_",
        "email",
        "name",
        "memberships",
        "profile_picture",
        "active_workspace",
        "default_workspace",
        "settings",
        "status",
    ]

    def __init__(
        self,
        id_: int,
        email: str,
        name: str,
        memberships: List[Membership],
        profile_picture: str,
        active_workspace: str,
        default_workspace: str,
        settings: Settings,
        status: str,
    ) -> None:
        self.id_ = id_
        self.email = email
        self.name = name
        self.memberships = memberships
        self.profile_picture = profile_picture
        self.active_workspace = active_workspace
        self.default_workspace = default_workspace
        self.settings = settings
        self.status = status


class User(UserMeta):
    def __init__(self, user: UserDTO):
        self.id_ = user.id_
        self.email = user.email
        self.name = user.name
        self.memberships = user.memberships
        self.profile_picture = user.profile_picture
        self.active_workspace = user.active_workspace
        self.default_workspace = user.default_workspace
        self.settings = user.settings
        self.status = user.status


class Mapper:
    MAPPING_DICT = bidict()

    def to_api(self, input_dict: Dict) -> Dict:
        return {self.MAPPING_DICT[k]: v for k, v in input_dict.items()}

    def to_dto(self, input_dict: Dict) -> Dict:
        return {self.MAPPING_DICT.inverse[k]: v for k, v in input_dict.items()}


class UserMapper(Mapper):
    MAPPING_DICT = bidict(
        {
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
    )


data = {
    "id": "625cf4a6a7d9d34012f70d123",
    "email": "test@example.com",
    "name": "Test User",
    "memberships": [
        {
            "userId": "625cf4a6a7d9d34012f70de1",
            "hourlyRate": None,
            "costRate": None,
            "targetId": "625cf4a6a7d9d34012f70de2",
            "membershipType": "WORKSPACE",
            "membershipStatus": "ACTIVE",
        }
    ],
    "profilePicture": "https://img.clockify.me/no-user-image.png",
    "activeWorkspace": "625cf4a6a7d9d34012f70de2",
    "defaultWorkspace": "625cf4a6a7d9d34012f70de2",
    "settings": {
        "weekStart": "MONDAY",
        "timeZone": "Europe/Amsterdam",
        "timeFormat": "HOUR24",
        "dateFormat": "DD/MM/YYYY",
        "sendNewsletter": False,
        "weeklyUpdates": True,
        "longRunning": True,
        "scheduledReports": True,
        "approval": True,
        "pto": True,
        "alerts": True,
        "reminders": True,
        "timeTrackingManual": True,
        "summaryReportSettings": {"group": "Project", "subgroup": "Time Entry"},
        "isCompactViewOn": False,
        "dashboardSelection": "ME",
        "dashboardViewType": "PROJECT",
        "dashboardPinToTop": False,
        "projectListCollapse": 50,
        "collapseAllProjectLists": False,
        "groupSimilarEntriesDisabled": False,
        "myStartOfDay": "09:00",
        "projectPickerTaskFilter": False,
        "lang": "EN",
        "multiFactorEnabled": False,
        "theme": "DEFAULT",
        "scheduling": True,
    },
    "status": "ACTIVE",
}
mapper = UserMapper()
dto = UserDTO(**mapper.to_dto(data))
user = User(dto)
print(user)
