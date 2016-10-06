.. _django-assets: http://pypi.python.org/pypi/django-assets

.. _install-intro:

=======
Install
=======

::

    pip install djangocodemirror


#. In your *settings* file add **djangocodemirror** to your installed apps:

    .. sourcecode:: python

        INSTALLED_APPS = (
            ...
            'djangocodemirror',
            ...
        )

#. Import default settings:

    .. sourcecode:: python

        from djangocodemirror.settings import *

#. Optionally install `django-assets`_ to use asset bundles;

#. You may eventually add some CodeMirror configurations in ``settings.CODEMIRROR_SETTINGS``, see **TODO** for more details.

