
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

Todo:

* Don't use 'mode' parameter anymore as internal parameter since 'mode' parameter can be used in various forms (a simple mode name, a mode mime-type, a dict of mode options);
* Finish and validate basic configs for some modes;
* Added tox configuration;
