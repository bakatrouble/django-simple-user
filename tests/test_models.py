"""
test_django-clean-user
------------

Tests for `django-clean-user` models module.
"""

from django.test import TestCase

from .models import CustomUser


class TestCustomUserManager(TestCase):

    def test_create_user(self):
        user = CustomUser.objects.create_user("johndoe", "password")
        self.assertIsInstance(user, CustomUser)

        # This is a must, ensure that `first_name` and `last_name` fields are
        # missing from the custom User model
        with self.assertRaises(AttributeError):
            user.first_name
        with self.assertRaises(AttributeError):
            user.last_name

    def test_create_user_fails(self):
        self.assertRaisesMessage(
            ValueError,
            "The given username must be set",
            CustomUser.objects.create_user,
            ""
        )

    def test_create_superuser(self):
        user = CustomUser.objects.create_superuser("superuser", "password")
        self.assertIsInstance(user, CustomUser)

    def test_create_superuser_fails(self):
        self.assertRaisesMessage(
            ValueError,
            "Superuser must have is_staff=True.",
            CustomUser.objects.create_superuser,
            "superuser",
            "password",
            is_staff=False
        )

        self.assertRaisesMessage(
            ValueError,
            "Superuser must have is_superuser=True.",
            CustomUser.objects.create_superuser,
            "superuser",
            "password",
            is_superuser=False
        )


class TestCustomUserModel(TestCase):

    def setUp(self):
        self.user = CustomUser(username="johndoe")
        self.user.set_password("password")

    def test_get_short_name(self):
        self.assertEqual(self.user.get_short_name(), "johndoe")

    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), "johndoe")
