.. _install_intro:

=======
Install
=======

Install package in your environment : ::

    pip install djangocodemirror

For development usage see :ref:`development_install`.

Configuration
*************

Add it to your installed Django apps in settings : ::

    INSTALLED_APPS = (
        ...
        "djangocodemirror",
    )

Then load default application settings in your settings file: ::

    from djangocodemirror.settings import *

There is no URL to mount or database migrations to apply.

.. _install_settings:

Settings
********

.. automodule:: djangocodemirror.settings
   :members:
