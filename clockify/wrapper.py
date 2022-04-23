import requests

import os

KEY = os.environ.get("CLOCKIFY_API_KEY")


class Wrapper:
    session: requests.Session

    def get(self, url):
        res = self.session.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            raise requests.HTTPError(f"HTTP Error {res.status_code}: {res.reason}")
