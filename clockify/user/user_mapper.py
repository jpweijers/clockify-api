from bidict import bidict
from clockify.mapper import Mapper


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
