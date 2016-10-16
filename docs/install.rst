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

Finally you may want to change available CodeMirror configurations from ``settings.CODEMIRROR_SETTINGS``:

* If you need to add your own new configuration see :ref:`configurations-intro`;
* If you just need to  add/change some parameters from configurations see :ref:`helper-intro`.

