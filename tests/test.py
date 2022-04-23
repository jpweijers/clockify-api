import os
from unittest import TestCase


class ClockifyTestCase(TestCase):
    KEY = os.environ.get("API_KEY")
    WORKSPACE = os.environ.get("WORKSPACE")
