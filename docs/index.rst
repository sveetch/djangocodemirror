.. djangocodemirror documentation master file, created by
   sphinx-quickstart on Tue Sept 15 00:09:10 2016.

.. _CodeMirror: http://codemirror.net/
.. _Django: https://www.djangoproject.com/
.. _django-assets: http://pypi.python.org/pypi/django-assets

Welcome to Django CodeMirror's documentation!
=============================================

**Django CodeMirror** is a `Django`_ application to embed `CodeMirror`_.

It works exclusively from configuration sets to manage CodeMirror options and
assets. A dedicated field, widget and some template tags are available to make
CodeMirror instances using these configurations on any element.

Since configurations are aware of every assets to load this enable to
use CodeMirror without a Javascript module loader (like ``Browserify`` or
``RequireJS``).

.. Note::
    Version 1.0.0 is a major refactoring, API has changed and editor
    enhancement stuff has been dropped (will probably live again in a new
    project).

Links
*****

* Read the documentation on `Read the docs <http://djangocodemirror.readthedocs.io/>`_;
* Download its `PyPi package <https://pypi.python.org/pypi/djangocodemirror>`_;
* Clone it on its `Github repository <https://github.com/sveetch/djangocodemirror>`_;

Dependancies
************

* `Django`_ >= 1.6, < 1.8;
* Optionally `django-assets`_ == 0.8;

User’s Guide
************

.. toctree::
   :maxdepth: 1

   install.rst
   examples.rst
   settings.rst
   configurations.rst
   library_references/templatetags.rst
   library_references/widgets.rst
   library_references/fields.rst

Developer’s Guide
*****************

.. toctree::
   :maxdepth: 1

   library_references/manifest.rst
   library_references/assets.rst
   library_references/assetrender.rst
   development.rst
   changelog.rst
