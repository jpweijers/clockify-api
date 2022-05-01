from random import randint, sample
import pytest
from requests.exceptions import HTTPError
from tests.test import ClockifyTestCase

from clockify.session import ClockifySession
from clockify.model.tag_model import Tag


class TestTags(ClockifyTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = ClockifySession(cls.KEY)
        tag_names = [f"Test Tag #{i}" for i in sample(range(0, 99999), 5)]
        for name in tag_names:
            tag = Tag(name=name, workspace_id=cls.WORKSPACE)
            cls.session.create_tag(tag)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        tags = cls.session.get_tags(cls.WORKSPACE)
        for tag in tags:
            cls.session.delete_tag(cls.WORKSPACE, tag.id_)
        return super().tearDownClass()

    def test_get_list_of_tags(self):
        tags = self.session.get_tags(self.WORKSPACE)
        for tag in tags:
            self.assertIsInstance(tag, Tag)

    def test_get_list_of_tags_fail(self):
        self.assertRaises(HTTPError, self.session.get_tags, "fake workspace id")

    def test_get_tag_by_id(self):
        tag = Tag(name=f"Test Tag #{randint(0, 99999)}", workspace_id=self.WORKSPACE)
        tag = self.session.create_tag(tag)
        search_tag = self.session.get_tag(self.WORKSPACE, tag.id_)
        self.assertIsInstance(search_tag, Tag)
        self.assertEqual(tag, search_tag)

    def test_get_tag_by_id_fail(self):
        self.assertRaises(
            HTTPError, self.session.get_tag, self.WORKSPACE, "fake tag id"
        )

    def test_update_tag(self):
        tag = Tag(name=f"Test Tag #{randint(0, 99999)}", workspace_id=self.WORKSPACE)
        tag = self.session.create_tag(tag)
        tag.name = "pizza"
        updated_tag = self.session.update_tag(tag)
        self.assertIsInstance(updated_tag, Tag)
        self.assertEqual(updated_tag.name, "pizza")

    def test_create_tag(self):
        tag = Tag(name=f"Test Tag #{randint(0, 99999)}", workspace_id=self.WORKSPACE)
        created_tag = self.session.create_tag(tag)
        self.assertIsInstance(created_tag, Tag)
        self.assertIsNotNone(created_tag.id_)

    def test_delete_tag(self):
        tag = Tag(name=f"Test Tag #{randint(0, 99999)}", workspace_id=self.WORKSPACE)
        tag = self.session.create_tag(tag)
        tag.archived = True
        archived_tag = self.session.update_tag(tag)
        deleted_tag = self.session.delete_tag(
            archived_tag.workspace_id, archived_tag.id_
        )
        self.assertIsInstance(deleted_tag, Tag)

    def test_delete_tag_fail(self):
        self.assertRaises(
            HTTPError,
            self.session.delete_tag,
            self.WORKSPACE,
            "fake tag id",
        )
