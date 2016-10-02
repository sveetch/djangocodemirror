
Default app settings
====================

.. note::
    Every file paths (as in ``settings.CODEMIRROR_BASE_JS``,
    ``settings.CODEMIRROR_BASE_CSS``, ``settings.CODEMIRROR_THEMES``,
    ``settings.CODEMIRROR_MODES``, etc..) must be relative to the static
    directory.

CODEMIRROR_FIELD_INIT_JS
------------------------

Template string for HTML Code to instanciate CodeMirror for a field.

Default value: ::

    <script>var {varname} = CodeMirror.fromTextArea(document.getElementById("{inputid}"),{settings});</script>

Contains two template variables:

* ``varname``: A Javascript variable name which will be set with the CodeMirror
  instance;
* ``inputid``: HTML element id;
* ``settings``: JSON string for CodeMirror parameters.


CODEMIRROR_SETTINGS
-------------------

Available CodeMirror configurations.

A CodeMirror configuration is a set of parameter for a CodeMirror instance plus
some internal ones reserved to the manifest to control some behaviors.

Usually, you should have at least the ``modes`` list parameter with a
valid mode name from ``settings.CODEMIRROR_MODES``. For other available
configuration parameters, see the CodeMirror documentation.

Every parameter in a configuration will be given to CodeMirror instance
excepted some internal ones:

modes
    List of mode names to load. Note that CodeMirror will assume to
    use the last loaded mode if you don't explicitely enable one using ``mode``
    parameter.
addons
    List of addons paths to load before modes.
themes
    List of theme name to load.
css_bundle_name
    CSS bundle name that is automatically builded from the
    configuration name.
js_bundle_name
    Javascript bundle name that is automatically builded from
    the configuration name.
extra_css
    List of paths for extra CSS files to append after themes.

Default shipped configurations implement a little subset of available
CodeMirror modes plus a ``empty`` configuration.

Default available configurations are:

* ``css``;
* ``django``;
* ``empty``;
* ``html``;
* ``javascript``;
* ``python``;
* ``restructuredtext``;
* ``scss``;

These modes are built from
`CodeMirror mode demonstrations <http://codemirror.net/mode/index.html>`_ to
reproduce the same behaviors.


CODEMIRROR_BASE_JS
------------------

List of CodeMirror Javascript base files that will be loaded before every
other CodeMirror Javascript components.

Default value: ::

    ["CodeMirror/lib/codemirror.js"]


CODEMIRROR_BASE_CSS
-------------------

List of CodeMirror CSS base files that will be loaded before themes.

Default value: ::

    ["CodeMirror/lib/codemirror.css"]

CODEMIRROR_THEMES
-----------------


Available CodeMirror CSS Theme files.

Default value contains only the *Ambiance* theme (a dark one), so you may add
yourself all your needed themes.

Default value: ::

    {
        "ambiance": "CodeMirror/theme/ambiance.css",
    }


CODEMIRROR_MODES
----------------

Available CodeMirror Javascript mode files.

Default shipped modes are built from default configurations requirements.


CODEMIRROR_JS_ASSET_TAG
-----------------------

HTML element to load a Javascript asset. Used by template tags and widget to
build assets HTML loaders.

Default value: ::

    u'<script type="text/javascript" src="{url}"></script>'

CODEMIRROR_CSS_ASSET_TAG
------------------------

HTML element to load a CSS asset. Used by template tags and widget to
build assets HTML loaders.

Default value: ::

    u'<link rel="stylesheet" href="{url}">'


CODEMIRROR_BUNDLE_CSS_NAME
--------------------------

Template string for Javascript bundle names where ``{settings_name}`` will
be filled with the configuration name.

Default value: ::

    "dcm-{settings_name}_css"


CODEMIRROR_BUNDLE_JS_NAME
-------------------------

Template string for CSS bundle names where ``{settings_name}`` will be
filled with the configuration name.

Default value: ::

    "dcm-{settings_name}_js"


CODEMIRROR_BUNDLE_CSS_OPTIONS
-----------------------------

Option arguments used to build CSS bundles with ``django-assets``.

Every CSS bundles will share the same arguments (excepted for the ``output``
one).

Default value: ::

    {
        'filters':'yui_css',
        'output':'css/dcm-{settings_name}.min.css',
    }


CODEMIRROR_BUNDLE_JS_OPTIONS
----------------------------

Option arguments used to build Javascript bundles with ``django-assets``.

Every Javascript bundles will share the same arguments (excepted for the
``output`` one).

Default value: ::

    {
        'filters':'yui_js',
        'output':'js/dcm-{settings_name}.min.js',
    }
