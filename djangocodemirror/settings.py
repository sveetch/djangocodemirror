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
# Template string for HTML Code to instanciate CodeMirror for a field.
CODEMIRROR_FIELD_INIT_JS = (u"""<script>var {varname} = """
                            """CodeMirror.fromTextArea("""
                            """document.getElementById("{inputid}"),"""
                            """{settings});</script>""")

# Available CodeMirror configurations.
CODEMIRROR_SETTINGS = {
    'empty': {},

    'javascript': {
        'modes': ['javascript'],
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
        'addons': [
            "CodeMirror/addon/mode/overlay.js",
        ],
    },

    'html': {
        'mode': 'htmlmixed',
        'modes': ['xml', 'javascript', 'css', 'vbscript', 'htmlmixed'],
    },

    'django': {
        'mode': 'django',
        'modes': ['xml', 'javascript', 'css', 'vbscript', 'htmlmixed',
                  'django'],
        'addons': [
            "CodeMirror/addon/mode/overlay.js",
        ],
    },

    'css': {
        'modes': ['css'],
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
        'matchBrackets': True,
        'addons': [
            "CodeMirror/addon/edit/matchbrackets.js",
        ],
    },
}

# List of CodeMirror Javascript base files that will be loaded before every
# other CodeMirror Javascript components.
CODEMIRROR_BASE_JS = ["CodeMirror/lib/codemirror.js"]

# List of CodeMirror CSS base files that will be loaded before themes.
CODEMIRROR_BASE_CSS = ["CodeMirror/lib/codemirror.css"]

# Available CodeMirror CSS Theme files.
CODEMIRROR_THEMES = {
    "ambiance": "CodeMirror/theme/ambiance.css",
}

# Available CodeMirror Javascript mode files.
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

# HTML element to load a Javascript asset
CODEMIRROR_JS_ASSET_TAG = (u'<script type="text/javascript" '
                           'src="{url}"></script>')

# HTML element to load a CSS asset
CODEMIRROR_CSS_ASSET_TAG = u'<link rel="stylesheet" href="{url}">'

# Template string for Javascript bundle names
CODEMIRROR_BUNDLE_CSS_NAME = "dcm-{settings_name}_css"

# Template string for CSS bundle names
CODEMIRROR_BUNDLE_JS_NAME = "dcm-{settings_name}_js"

# Option arguments used to build CSS bundles with ``django-assets``.
CODEMIRROR_BUNDLE_CSS_OPTIONS = {
    'filters': 'yui_css',
    'output': 'css/dcm-{settings_name}.min.css',
}

# Option arguments used to build Javascript bundles with ``django-assets``.
CODEMIRROR_BUNDLE_JS_OPTIONS = {
    'filters': 'yui_js',
    'output': 'js/dcm-{settings_name}.min.js',
}
