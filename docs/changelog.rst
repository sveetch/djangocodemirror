
=========
Changelog
=========

Version 2.0.0 - 2018/09/28
--------------------------

**Add support for Django 1.11, 2.0, 2.1 and CodeMirror 5.40.2**

* Rewrite package to use ``setup.cfg``;
* Add support for Django 1.11, Django 2.0 and Django 2.1, close #22;
* Drop support for Django 1.8 and 1.9;
* Django 1.11 support is the last one for Python2;
* Change old demo project to more cleaner sandbox;
* Change widget to use new Django widget API;
* Upgraded included copy of CodeMirror to 5.40.2;

Version 1.1.0 - 2017/05/18
--------------------------

* Added support from Django 1.9 to 1.10, close #18;
* Added support for Python 3.5, close #19;
* Dropped support for Django 1.6 and 1.7;


Version 1.0.5 - 2016/10/16
--------------------------

* Added helper to change parameters on many configs, close #14;


Version 1.0.4 - 2016/10/11
--------------------------

* Better explicit name for internal exceptions, close #16;


Version 1.0.3 - 2016/10/10
--------------------------

* Validated support for Django 1.8 from tox tests;
* Allow to disable asset bundle on a configuration using None value on bundle names, close #15;


Version 1.0.2 - 2016/10/09
--------------------------

* A dummy bump because previous version lacked of bumping to 1.0.1;


Version 1.0.1 - 2016/10/09
--------------------------

* Fixed some minor packages flaws (MANIFEST, classifiers, etc..);


Version 1.0.0 - 2016/10/09
--------------------------

This is a major refactoring to adopt Test Driven Development, cleaner behaviors and better core API.

* Added Unittests with Py.test;
* Added documentation, close #11;
* Added tox configuration to validate support for Django 1.6 and 1.7;
* Flake8 coverage;
* Rewrited every template tags and filters;
* Better docstring for code;
* Removed all stuff about reStructuredText editor addons;
* Removed everything about the CodeMirror rst editor (may probably live again in its own app);
* Removed deprecated templates;
* Replaced old Codemirror git submodule with a static copy from ``5.18.2`` version, close #9;
* Dropped ``mode`` as an internal parameter since CodeMirror can use it in many different ways (as a string for a name, as a string for a mime-type, as a dict of mode options);


Version 0.9.8 - 2016/08/24
--------------------------

Last release for previous Django CodeMirror API with CodeMirror 3.x and reStructuredText editor addons.
