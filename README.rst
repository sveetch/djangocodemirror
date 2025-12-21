.. _Python: https://www.python.org/
.. _Django: https://www.djangoproject.com/
.. _CodeMirror: http://codemirror.net/

=================
Django CodeMirror
=================

A Django application to embed `CodeMirror`_

It works exclusively from configuration sets to manage CodeMirror options and
assets. A dedicated field, widget and some template tags are available to make
CodeMirror instances using these configurations on any element.

Since configurations are aware of every assets to load this enable you to
use CodeMirror without a Javascript module loader (like ``Browserify`` or
``RequireJS``).

Links
*****

* Read the documentation on `Read the docs <http://djangocodemirror.readthedocs.io/>`_;
* Download its `PyPi package <https://pypi.python.org/pypi/djangocodemirror>`_;
* Clone it on its `Github repository <https://github.com/sveetch/djangocodemirror>`_;

Dependancies
************

* `Python`_>=3.10;
* `Django`_>=4.2;
