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

* ``modes``: List of mode names to load in addition to the current ``mode``;
* ``addons``: List of addons path to load in addition to the modes;
* ``themes`` List of theme name to load;
* ``css_bundle_name``: CSS bundle name that is automatically builded from the
  configuration name;
* ``js_bundle_name``: Javascript bundle name that is automatically builded from
  the configuration name;

There is only one default configuration named ``empty`` that is an empty
configuration without any parameter.
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
    "rst": "CodeMirror/mode/rst/rst.js",
}
"""Available CodeMirror Javascript mode files.

Default value contains only the *reSructuredText* mode, so you may add yourself
all your needed modes."""


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
