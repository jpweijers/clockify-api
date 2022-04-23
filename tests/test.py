import os
from unittest import TestCase


class ClockifyTestCase(TestCase):
    KEY = os.environ.get("API_KEY")
    WORKSPACE = os.environ.get("WORKSPACE")

    CLIENT = "6263de4b5ca9a1421d1cdbaa"

    NON_EXISTING_CLIENT = "1234abcd"
    NON_EXISTING_WORKSPACE = "1234abcd"
