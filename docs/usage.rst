=====
Usage
=====

To use Django Clean User in a project, add it to your `INSTALLED_APPS`:

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
