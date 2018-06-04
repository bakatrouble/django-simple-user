"""
test_django-simple-user
------------

Tests for `django-simple-user` managers module.
"""

from django.test import TestCase

from .models import UserWithUsername, UserWithEmail


class TestUserWithUsernameManager(TestCase):

    def test_create_user(self):
        # Make sure it works perfectly
        UserWithUsername.objects.create_user("johndoe", "password")

        self.assertRaisesMessage(
            ValueError,
            "The given username must be set",
            UserWithUsername.objects.create_user,
            ""
        )

    def test_create_superuser(self):
        # Make sure it works perfectly
        UserWithUsername.objects.create_superuser("janedoe", "password")

        self.assertRaisesMessage(
            ValueError,
            "Superuser must have is_staff=True.",
            UserWithUsername.objects.create_superuser,
            "superuser",
            "password",
            is_staff=False
        )

        self.assertRaisesMessage(
            ValueError,
            "Superuser must have is_superuser=True.",
            UserWithUsername.objects.create_superuser,
            "superuser",
            "password",
            is_superuser=False
        )


class TestUserWithEmailManager(TestCase):

    def test_create_user(self):
        # Make sure it works perfectly
        UserWithEmail.objects.create_user("johndoe@testserver.com", "password")

        self.assertRaisesMessage(
            ValueError,
            "The given email address must be set",
            UserWithEmail.objects.create_user,
            ""
        )

    def test_create_superuser(self):
        # Make sure it works perfectly
        UserWithEmail.objects.create_superuser("janedoe@testserver.com", "password")

        self.assertRaisesMessage(
            ValueError,
            "Superuser must have is_staff=True.",
            UserWithEmail.objects.create_superuser,
            "superuser@testserver.com",
            "password",
            is_staff=False
        )

        self.assertRaisesMessage(
            ValueError,
            "Superuser must have is_superuser=True.",
            UserWithEmail.objects.create_superuser,
            "superuser@testsever.com",
            "password",
            is_superuser=False
        )
