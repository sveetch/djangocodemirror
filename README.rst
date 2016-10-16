.. _CodeMirror: http://codemirror.net/
.. _Django: https://www.djangoproject.com/
.. _django-assets: http://pypi.python.org/pypi/django-assets

Django CodeMirror
=================

This is a `Django`_ application to embed `CodeMirror`_.

It works exclusively from configuration sets to manage CodeMirror options and
assets. A dedicated field, widget and some template tags are available to make
CodeMirror instances using these configurations on any element.

Since configurations are aware of every assets to load this enable you to
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

* `Django`_ >= 1.6, < 1.9;
* Optionally `django-assets`_ == 0.8;
