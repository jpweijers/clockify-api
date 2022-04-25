from clockify.model.user_model import User
from clockify.config import BASE_URL
from clockify.wrapper import Wrapper


class UserWrapper(Wrapper):
    def get_current_user(self) -> User:
        url = f"{BASE_URL}/user"
        return self.get_one(url, User)
