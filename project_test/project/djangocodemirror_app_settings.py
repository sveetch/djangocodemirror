"""
Django Codemirror application settings to share between various 'project_test'
settings.
"""
# Some CodeMirror configurations for testing purposes
# These configs won't work for real, this is just for unittests
CODEMIRROR_SETTINGS = {
    'empty': {},
    'basic': {
        'mode': 'rst',
    },
    'with-options': {
        'mode': 'rst',
        'lineWrapping': True,
        'lineNumbers': True,
    },
    'with-modes': {
        'mode': 'rst',
        'modes': ['rst', 'python'],
    },
    'with-themes': {
        'mode': 'rst',
        'theme': 'elegant',
        'themes': ['eclipse', 'elegant'],
    },
    'with-addons': {
        'mode': 'rst',
        'addons': [
            "CodeMirror/lib/util/dialog.js",
        ],
    },
    'with-extra_css': {
        'mode': 'rst',
        'extra_css': [
            "CodeMirror/theme/ambiance.css",
        ],
    },
    'with-all': {
        'mode': 'rst',
        'lineWrapping': True,
        'lineNumbers': True,
        'addons': [
            "CodeMirror/lib/util/dialog.js",
        ],
        'modes': ['rst', 'python'],
        'theme': 'neat',
        'themes': ['eclipse', 'neat'],
        'extra_css': [
            "CodeMirror/theme/ambiance.css",
        ],
    },
}

# Subset of some available themes
CODEMIRROR_THEMES = {
    "ambiance": "CodeMirror/theme/ambiance.css",
    "eclipse": "CodeMirror/theme/eclipse.css",
    "elegant": "CodeMirror/theme/elegant.css",
    "neat": "CodeMirror/theme/neat.css",
}

    #<script src="../vbscript/vbscript.js"></script>
# Subset of some available modes
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
