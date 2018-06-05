=============================
Django Simple User
=============================

.. image:: https://pyup.io/repos/github/valerymelou/django-simple-user/shield.svg
     :target: https://pyup.io/repos/github/valerymelou/django-simple-user/
     :alt: Updates

.. image:: https://badge.fury.io/py/django-simple-user.svg
    :target: https://badge.fury.io/py/django-simple-user

.. image:: https://travis-ci.org/valerymelou/django-simple-user.svg?branch=master
    :target: https://travis-ci.org/valerymelou/django-simple-user

.. image:: https://codecov.io/gh/valerymelou/django-simple-user/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/valerymelou/django-simple-user

Provides a simple abstract User model without first and last name fields.

Documentation
-------------

The full documentation is available at https://django-simple-user.readthedocs.io.

Quickstart
----------

Install Django Simple User::

    pip install django-simple-user

Features
--------

* Abstract User model without the fields ``first_name`` and ``last_name``
* Abstract User model without the fields ``first_name``, ``last_name`` and ``email``
* Abstract User model without the fields ``first_name``, ``last_name`` and ``username``

Usage
-----

If you are like me, you might have found yourself extending ``django.contrib.auth.base_user.AbstractBaseUser`` just to remove the ``first_name`` and ``last_name`` fields from your final User model. I was tired of doing that and I created this package. It defines an abstract User model without those fields so that you can just inherit from it to create your User model. It is as simple as doing this:

::

    from simple_user.models import AbstractUser


    class User(AbstractUser):
        pass

This will create a User model with all the fields that happen to exists in the default Django's User model except ``first_name`` and ``last_name``.

Bonuses
-------

There are some cases where you only want ``username`` or ``email`` but not both fields in your model. Django Simple User has got you covered. You can use ``SimpleUserWithUsername`` or ``SimpleUserWithEmail`` to achieve each scenario.

For a User model with ``username`` as identifying field but without ``first_name``, ``last_name`` and ``email`` do:

::

    from simple_user.models import SimpleUserWithUsername


    class User(SimpleUserWithUsername):
        pass

For a User model with ``email`` as identifying field but without ``first_name``, ``last_name`` and ``username`` do:

::

    from simple_user.models import SimpleUserWithUsername


    class User(SimpleUserWithEmail):
        pass

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
