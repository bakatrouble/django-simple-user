"""
test_django-clean-user
------------

Tests for `django-clean-user` models module.
"""

from django.test import TestCase

from clean_user.models import AbstractUser, AbstractUserWithUsername, AbstractUserWithEmail


class TestAbstractUser(TestCase):

    def setUp(self):
        self.user = AbstractUser(username="janedoe")

    def test_is_clean(self):
        with self.assertRaises(AttributeError):
            self.user.first_name
        with self.assertRaises(AttributeError):
            self.user.last_name
        self.assertEqual(self.user.USERNAME_FIELD, "username")
        self.assertEqual(self.user.EMAIL_FIELD, "email")
        self.assertEqual(self.user.REQUIRED_FIELDS, ["email"])

    def test_get_short_name(self):
        self.assertEqual(self.user.get_short_name(), "janedoe")

    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), "janedoe")


class TestAbstractUserWithUsername(TestCase):

    def setUp(self):
        self.user = AbstractUserWithUsername(username="janedoe")

    def test_is_clean(self):
        with self.assertRaises(AttributeError):
            self.user.first_name
        with self.assertRaises(AttributeError):
            self.user.last_name
        self.assertEqual(self.user.USERNAME_FIELD, "username")
        self.assertEqual(self.user.REQUIRED_FIELDS, [])

    def test_get_short_name(self):
        self.assertEqual(self.user.get_short_name(), "janedoe")

    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), "janedoe")


class TestAbstractUserWithEmail(TestCase):

    def setUp(self):
        self.user = AbstractUserWithEmail(email="johndoe@testserver.com")

    def test_is_clean(self):
        with self.assertRaises(AttributeError):
            self.user.first_name
        with self.assertRaises(AttributeError):
            self.user.last_name
        self.assertEqual(self.user.USERNAME_FIELD, "email")
        self.assertEqual(self.user.REQUIRED_FIELDS, [])

    def test_get_short_name(self):
        self.assertEqual(self.user.get_short_name(), "johndoe@testserver.com")

    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), "johndoe@testserver.com")
