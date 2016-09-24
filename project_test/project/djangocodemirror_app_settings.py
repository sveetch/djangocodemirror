"""
Django Codemirror application settings to share between various 'project_test'
settings.
"""
# Some CodeMirror configurations for testing purposes
CODEMIRROR_SETTINGS = {
    'empty': {},
    'mode-naive': {
        'lineWrapping': True,
        'lineNumbers': True,
        'modes': ['python', 'javascript'],
    },
    'rst-with-modes': {
        'mode': 'rst',
        'lineWrapping': True,
        'lineNumbers': True,
        'modes': ['rst', 'python', 'javascript'],
    },
    'rst-with-themes': {
        'mode': 'rst',
        'lineWrapping': True,
        'lineNumbers': True,
        'theme': 'elegant',
        'themes': ['eclipse', 'elegant'],
    },
    'rst-with-all': {
        'mode': 'rst',
        'lineWrapping': True,
        'lineNumbers': True,
        'addons': [
            "CodeMirror/lib/util/dialog.js",
            "CodeMirror/lib/util/search.js",
            "CodeMirror/lib/util/searchcursor.js",
        ],
        'modes': ['rst', 'python', 'css'],
        'theme': 'neat',
        'themes': ['eclipse', 'neat'],
    },
    'rst-basic': {
        'mode': 'rst',
        'lineWrapping': True,
        'lineNumbers': True,
    },

    # NOTE: Real configurations to port to app settings

    # Validated
    'javascript': {
        'mode': 'javascript',
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

    # Validated
    'restructuredtext': {
        'mode': 'rst',
        'modes': ['python', 'stex'],
        'lineWrapping': True,
        'lineNumbers': True,
        'addons': [
            "CodeMirror/addon/mode/overlay.js",
        ],
    },

    # Validated
    'html': {
        'mode': 'htmlmixed',
        'modes': ['xml', 'javascript', 'css', 'vbscript'],
        'lineWrapping': True,
        'lineNumbers': True,
    },

    # Validated
    'django': {
        'mode': 'django',
        'modes': ['xml', 'javascript', 'css', 'vbscript', 'htmlmixed'],
        'lineWrapping': True,
        'lineNumbers': True,
        'addons': [
            "CodeMirror/addon/mode/overlay.js",
        ],
    },

    # To do
    #<link rel="stylesheet" href="../../addon/hint/show-hint.css">
    'css': {
        'mode': 'css',
        'lineWrapping': True,
        'lineNumbers': True,
        'matchBrackets': True,
        'addons': [
            "CodeMirror/addon/edit/matchbrackets.js",
            "CodeMirror/addon/hint/show-hint.js",
            "CodeMirror/addon/hint/css-hint.js",
        ],
    },

    # To valid
    'scss': {
        'mode': 'css',
        #'mode': 'text/x-scss',
        'lineWrapping': True,
        'lineNumbers': True,
        'matchBrackets': True,
        'addons': [
            "CodeMirror/addon/edit/matchbrackets.js",
        ],
    },

    # To valid
    'python': {
        'mode': 'python',
        #'mode': {
            #'name': "python",
            #'version': 3,
            #'singleLineStringErrors': false,
        #}
        'lineWrapping': True,
        'lineNumbers': True,
        'matchBrackets': True,
        'addons': [
            "CodeMirror/addon/edit/matchbrackets.js",
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
