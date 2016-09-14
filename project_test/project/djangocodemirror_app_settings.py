"""
Django Codemirror application settings to share between various 'project_test'
settings.
"""
CODEMIRROR_SETTINGS = {
    'empty': {},
    'mode-naive': {
        'lineWrapping': True,
        'lineNumbers': True,
        'modes': ['python', 'javascript'],
    },
    'rst-basic': {
        'mode': 'rst',
        'lineWrapping': True,
        'lineNumbers': True,
    },
    'rst-with-addons': {
        'mode': 'rst',
        'lineWrapping': True,
        'lineNumbers': True,
        'addons': [
            "CodeMirror/lib/util/dialog.js",
            "CodeMirror/lib/util/search.js",
            "CodeMirror/lib/util/searchcursor.js",
        ],
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
}
