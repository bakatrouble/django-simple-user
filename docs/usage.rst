=====
Usage
=====

To use Django Simple User in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'simple_user.apps.SimpleUserConfig',
        ...
    )

Add Django Simple User's URL patterns:

.. code-block:: python

    from simple_user import urls as simple_user_urls


    urlpatterns = [
        ...
        url(r'^', include(simple_user_urls)),
        ...
    ]
