"""
Django settings for project demonstration (will not work for unittests)

Actually inherits from settings for Django 1.6. Intended to be used with
``make server``.
"""

from settings_django16 import *

# Some CodeMirror configurations for testing purposes
CODEMIRROR_SETTINGS.update({
    # Validated
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

    # Validated
    'restructuredtext': {
        'mode': 'rst',
        'modes': ['python', 'stex', 'rst'],
        'lineWrapping': True,
        'lineNumbers': True,
        'addons': [
            "CodeMirror/addon/mode/overlay.js",
        ],
    },

    # Validated
    'html': {
        'mode': 'htmlmixed',
        'modes': ['xml', 'javascript', 'css', 'vbscript', 'htmlmixed'],
        'lineWrapping': True,
        'lineNumbers': True,
    },

    # Validated
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

    # To do: we need to add CSS assets that are not themes
    #<link rel="stylesheet" href="../../addon/hint/show-hint.css">
    'css': {
        'modes': ['css'],
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
        #'mode': 'css',
        'mode': 'text/x-scss',
        'modes': ['css'],
        'lineWrapping': True,
        'lineNumbers': True,
        'matchBrackets': True,
        'addons': [
            "CodeMirror/addon/edit/matchbrackets.js",
        ],
    },

    # To valid
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
})
