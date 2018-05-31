=============================
Django Clean User
=============================

.. image:: https://badge.fury.io/py/django-clean-user.svg
    :target: https://badge.fury.io/py/django-clean-user

.. image:: https://travis-ci.org/valerymelou/django-clean-user.svg?branch=master
    :target: https://travis-ci.org/valerymelou/django-clean-user

.. image:: https://codecov.io/gh/valerymelou/django-clean-user/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/valerymelou/django-clean-user

Provides an abstract base User model without first and last name fields.

Documentation
-------------

The full documentation is at https://django-clean-user.readthedocs.io.

Quickstart
----------

Install Django Clean User::

    pip install django-clean-user

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'clean_user.apps.CleanUserConfig',
        ...
    )

Add Django Clean User's URL patterns:

.. code-block:: python

    from clean_user import urls as clean_user_urls


    urlpatterns = [
        ...
        url(r'^', include(clean_user_urls)),
        ...
    ]

Features
--------

* TODO

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
