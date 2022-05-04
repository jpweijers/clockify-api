from clockify.model.user_model import User
from clockify.config import BASE_URL
from clockify.wrapper import Wrapper


class UserWrapper(Wrapper):
    def get_current_user(self) -> User:
        """Return current user as a User Object

        Returns:
            User: Current user object.
        """
        url = f"{BASE_URL}/user"
        return self._get_one(url, User)
