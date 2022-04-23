import requests

from clockify.client.client_wrapper import ClientWrapper
from clockify.user.user_wrapper import UserWrapper


class ClockifySession(UserWrapper, ClientWrapper):
    BASE_URL = "https://api.clockify.me/api/v1"

    def __init__(self, key):
        self.session = requests.Session()
        self.session.headers.update({"x-api-key": key})
