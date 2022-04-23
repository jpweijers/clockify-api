import os

from clockify.user.user_dto import UserDTO
from clockify.user.user_mapper import UserMapper
from clockify.wrapper import Wrapper

CLOCKIFY_API_KEY = os.environ.get("CLOCKIFY_API_KEY")


class UserWrapper(Wrapper):
    USER_PATH = "user"

    def get_current_user(self):
        url = "/".join([self.BASE_URL, self.USER_PATH])
        res = self.get(url)
        dto = UserMapper().to_dto(res)
        return UserDTO(**dto)
