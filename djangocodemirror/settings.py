# -*- coding: utf-8 -*-
"""
Default app settings
====================

Note:
    Every file paths (as in ``settings.CODEMIRROR_BASE_JS``,
    ``settings.CODEMIRROR_BASE_CSS``, ``settings.CODEMIRROR_THEMES``,
    ``settings.CODEMIRROR_MODES``, etc..) must be relative to the static
    directory.

"""
CODEMIRROR_FIELD_INIT_JS = (u"""<script>var {varname} = """
                            """CodeMirror.fromTextArea("""
                            """document.getElementById("{inputid}"),"""
                            """{settings});</script>""")
"""Template string for HTML Code to instanciate CodeMirror for a field.

Contains two template variables:

* ``varname``: A Javascript variable name which will be set with the CodeMirror
  instance;
* ``inputid``: Input field id;
* ``settings``: JSON string for CodeMirror parameters.
"""


CODEMIRROR_SETTINGS = {
    'empty': {},

    'javascript': {
        'modes': ['javascript'],
        'lineWrapping': True,
        'lineNumbers': True,
        'matchBrackets': True,
        'continueComments': "Enter",
        'extraKeys': {"Ctrl-Q": "toggleComment"},
        'addons': [
            "CodeMirror/addon/edit/matchbrackets.js",
            "CodeMirror/addon/comment/continuecomment.js",
            "CodeMirror/addon/comment/comment.js",
        ],
    },

    'restructuredtext': {
        'mode': 'rst',
        'modes': ['python', 'stex', 'rst'],
        'lineWrapping': True,
        'lineNumbers': True,
        'addons': [
            "CodeMirror/addon/mode/overlay.js",
        ],
    },

    'html': {
        'mode': 'htmlmixed',
        'modes': ['xml', 'javascript', 'css', 'vbscript', 'htmlmixed'],
        'lineWrapping': True,
        'lineNumbers': True,
    },

    'django': {
        'mode': 'django',
        'modes': ['xml', 'javascript', 'css', 'vbscript', 'htmlmixed',
                  'django'],
        'lineWrapping': True,
        'lineNumbers': True,
        'addons': [
            "CodeMirror/addon/mode/overlay.js",
        ],
    },

    'css': {
        'modes': ['css'],
        'lineWrapping': True,
        'lineNumbers': True,
        'matchBrackets': True,
        'extraKeys': {"Ctrl-Space": "autocomplete"},
        'addons': [
            "CodeMirror/addon/edit/matchbrackets.js",
            "CodeMirror/addon/hint/show-hint.js",
            "CodeMirror/addon/hint/css-hint.js",
        ],
        'extra_css': [
            "CodeMirror/addon/hint/show-hint.css",
        ],
    },

    'scss': {
        'mode': 'text/x-scss',
        'modes': ['css'],
        'lineWrapping': True,
        'lineNumbers': True,
        'matchBrackets': True,
        'addons': [
            "CodeMirror/addon/edit/matchbrackets.js",
        ],
    },

    'python': {
        'mode': {
            'name': "python",
            'version': 3,
            'singleLineStringErrors': False,
        },
        'modes': ['python'],
        'lineWrapping': True,
        'lineNumbers': True,
        'matchBrackets': True,
        'addons': [
            "CodeMirror/addon/edit/matchbrackets.js",
        ],
    },
}
"""
Available CodeMirror configurations.

A CodeMirror configuration is a set of parameter for a CodeMirror instance plus
some internal ones reserved to the manifest to control some behaviors.

Usually, you should have at least the ``mode`` parameter that should contains a
valid mode name from ``settings.CODEMIRROR_MODES``. For other available
configuration parameters, see the CodeMirror documentation.

Every parameter in a configuration will be given to CodeMirror instance
excepted some internal ones:

* ``modes``: List of mode names to load. Note that CodeMirror will assume to
  use the last loaded mode if you don't explicitely enable one using ``mode``
  parameter;
* ``addons``: List of addons paths to load before modes;
* ``themes`` List of theme name to load;
* ``css_bundle_name``: CSS bundle name that is automatically builded from the
  configuration name;
* ``js_bundle_name``: Javascript bundle name that is automatically builded from
  the configuration name;
* ``extra_css``: List of paths for extra CSS files to append after themes;

Default shipped configurations implement a little subset of available
CodeMirror modes plus a ``empty`` configuration.

Default configurations are:

* ``css``;
* ``django``;
* ``empty``;
* ``html``;
* ``javascript``;
* ``python``;
* ``restructuredtext``;
* ``scss``;

Excepted ``empty``, these modes are built from CodeMirror mode demonstrations.
"""


CODEMIRROR_BASE_JS = ["CodeMirror/lib/codemirror.js"]
"""List of CodeMirror Javascript base files that will be loaded before every
other CodeMirror Javascript components."""


CODEMIRROR_BASE_CSS = ["CodeMirror/lib/codemirror.css"]
"""List of CodeMirror CSS base files that will be loaded before themes."""


CODEMIRROR_THEMES = {
    "ambiance": "CodeMirror/theme/ambiance.css",
}
"""Available CodeMirror CSS Theme files.

Default value contains only the *Ambiance* theme (a dark one), so you may add
yourself all your needed themes."""


CODEMIRROR_MODES = {
    "css": "CodeMirror/mode/css/css.js",
    "django": "CodeMirror/mode/django/django.js",
    "htmlmixed": "CodeMirror/mode/htmlmixed/htmlmixed.js",
    "javascript": "CodeMirror/mode/javascript/javascript.js",
    "python": "CodeMirror/mode/python/python.js",
    "rst": "CodeMirror/mode/rst/rst.js",
    "stex": "CodeMirror/mode/stex/stex.js",
    "vbscript": "CodeMirror/mode/vbscript/vbscript.js",
    "xml": "CodeMirror/mode/xml/xml.js",
}
"""Available CodeMirror Javascript mode files.

Default shipped modes are built from default configurations requirements."""


CODEMIRROR_JS_ASSET_TAG = u'<script type="text/javascript" src="{url}"></script>'
"""HTML element to load a Javascript asset. Used by template tags and widget to
build assets HTML loaders."""

CODEMIRROR_CSS_ASSET_TAG = u'<link rel="stylesheet" href="{url}">'
"""HTML element to load a CSS asset. Used by template tags and widget to
build assets HTML loaders."""


CODEMIRROR_BUNDLE_CSS_NAME = "dcm-{settings_name}_css"
"""Template string for Javascript bundle names where ``{settings_name}`` will
be filled with the configuration name."""


CODEMIRROR_BUNDLE_JS_NAME = "dcm-{settings_name}_js"
"""Template string for CSS bundle names where ``{settings_name}`` will be
filled with the configuration name."""


CODEMIRROR_BUNDLE_CSS_OPTIONS = {
    'filters':'yui_css',
    'output':'css/dcm-{settings_name}.min.css',
}
"""Option arguments used to build CSS bundles with ``django-assets``.

Every CSS bundles will share the same arguments (excepted for the ``output``
one)."""


CODEMIRROR_BUNDLE_JS_OPTIONS = {
    'filters':'yui_js',
    'output':'js/dcm-{settings_name}.min.js',
}
"""Option arguments used to build Javascript bundles with ``django-assets``.

Every Javascript bundles will share the same arguments (excepted for the
``output`` one)."""
