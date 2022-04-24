from tests.test import ClockifyTestCase
from clockify.user.user_dto import UserDTO
from clockify.session import ClockifySession


class TestGetUser(ClockifyTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = ClockifySession(cls.KEY)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_get_current_user(self):
        user = self.session.get_current_user()
        self.assertIsInstance(user, UserDTO)
