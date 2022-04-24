import os

from clockify.user.user_dto import UserDTO
from clockify.user.user_mapper import UserMapper
from clockify.wrapper import Wrapper


class UserWrapper(Wrapper):
    path = "user"

    def get_current_user(self):
        url = "/".join([self.base_url, self.path])
        return self.get_one(url, UserMapper(), UserDTO)
