"""
test_django-simple-user
------------

Tests for `django-simple-user` models module.
"""

from django.core import mail
from django.test import TestCase

from simple_user.models import AbstractUser, SimpleUserWithUsername, SimpleUserWithEmail


class TestAbstractUser(TestCase):

    def setUp(self):
        self.user = AbstractUser(username="janedoe", email="janedoe@testserver.com")

    def test_is_simple(self):
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

    def test_email_user(self):
        self.user.email_user("Dummy message", "This is a dummy message")
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Dummy message")


class TestSimpleUserWithUsername(TestCase):

    def setUp(self):
        self.user = SimpleUserWithUsername(username="janedoe")

    def test_is_simple(self):
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


class TestSimpleUserWithEmail(TestCase):

    def setUp(self):
        self.user = SimpleUserWithEmail(email="johndoe@testserver.com")

    def test_is_simple(self):
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

    def test_email_user(self):
        self.user.email_user("Dummy message", "This is a dummy message")
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Dummy message")
