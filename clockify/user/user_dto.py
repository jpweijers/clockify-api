from typing import List

from clockify.user.membership.membership_dto import MembershipDTO
from clockify.user.membership.membership_mapper import MembershipMapper
from clockify.user.settings.settings_dto import SettingsDTO
from clockify.user.settings.settings_mapper import SettingsMapper


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
        id_: str,
        email: str,
        name: str,
        memberships: List[MembershipDTO],
        profile_picture: str,
        active_workspace: str,
        default_workspace: str,
        settings: SettingsDTO,
        status: str,
    ) -> None:
        membership_dtos = [MembershipMapper().to_dto(m) for m in memberships]
        settings_dto = SettingsMapper().to_dto(settings)

        self.id_ = id_
        self.email = email
        self.name = name
        self.memberships = [MembershipDTO(**dto) for dto in membership_dtos]
        self.profile_picture = profile_picture
        self.active_workspace = active_workspace
        self.default_workspace = default_workspace
        self.settings = SettingsDTO(**settings_dto)
        self.status = status
