from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserWithUsernameManager, UserWithEmailManager


class SimpleAbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    Base abstract User class for all abstract classes defined in this module.
    """
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True


class SimpleUserWithUsername(SimpleAbstractUser):
    """
    And abstract base class implementing a fully featured user Model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    objects = UserWithUsernameManager()

    USERNAME_FIELD = 'username'

    class Meta(SimpleAbstractUser.Meta):
        abstract = True

    def get_full_name(self):
        """
        Returns the full name for the user.
        """
        return self.username

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.username


class SimpleUserWithEmail(SimpleAbstractUser):
    """
    And abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Email and password are required. Other fields are optional.
    """
    email = models.EmailField(
        _('email address'),
        max_length=255,
        unique=True,
        error_messages={
            'unique': _("A user with that username already exists."),
        }
    )

    objects = UserWithEmailManager()

    USERNAME_FIELD = 'email'

    class Meta(SimpleAbstractUser.Meta):
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.email

    def get_full_name(self):
        """
        Returns the full name for the user.
        """
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this user.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class AbstractUser(SimpleUserWithUsername):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    email = models.EmailField(_('email address'), blank=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta(SimpleUserWithUsername.Meta):
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this user.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
