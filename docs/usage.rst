=====
Usage
=====

You can start using Django Simple User right after installing it. No need to add it to your `INSTALLED_APPS`:

Default User model of Django but without ``first_name`` and ``last_name`` fields.
---------------------------------------------------------------------------------

You can simply remove the first and last name fields from the default User model of Django by doing the following:

::
    from simple_user.models import AbstractUser


    class User(AbstractUser):
        pass


And set it as your ``AUTH_USER_MODEL`` in ``settings.py``.

::
    AUTH_USER_MODEL = your_users_app_label.User

You can even add your own custom fields to the new User model:

::
    from django.db import models

    from simple_user.models import AbstractUser


    class User(AbstractUser):
        name = models.CharField('Name', max_length=100)
        birth_date = models.DateField('birth date', null=True, blank=True)
