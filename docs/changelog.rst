
=========
Changelog
=========

Version 1.0.0 - Unreleased
--------------------------

This is a major refactoring to adopt Test Driven Development, cleaner behaviors and better core API.

* Added Unittests with Py.test;
* Added documentation;
* Rewrited every template tags and filters;
* Better docstring for code;
* Removed all stuff about reStructuredText editor addons;
* Removed everything about the CodeMirror rst editor (may probably live again in its own app);
* Removed deprecated templates;
* Replaced old Codemirror git submodule with a static copy from ``5.18.2`` version;
* Dropped ``mode`` as an internal parameter since CodeMirror can use it in many different ways (as a string for a name, as a string for a mime-type, as a dict of mode options);

Todo:

* Finish documentation

  * Ensure everything is documented about config;

* Added tox configuration;
