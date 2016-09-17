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

# Subset of some available themes
CODEMIRROR_THEMES = {
    "ambiance": "CodeMirror/theme/ambiance.css",
    "ambiance-mobile": "CodeMirror/theme/ambiance-mobile.css",
    "base16-dark": "CodeMirror/theme/base16-dark.css",
    "bespin": "CodeMirror/theme/bespin.css",
    "dracula": "CodeMirror/theme/dracula.css",
    "eclipse": "CodeMirror/theme/eclipse.css",
    "elegant": "CodeMirror/theme/elegant.css",
    "neat": "CodeMirror/theme/neat.css",
    "neo": "CodeMirror/theme/neo.css",
    "night": "CodeMirror/theme/night.css",
    "panda-syntax": "CodeMirror/theme/panda-syntax.css",
    "xq-light": "CodeMirror/theme/xq-light.css",
    "yeti": "CodeMirror/theme/yeti.css",
    "zenburn": "CodeMirror/theme/zenburn.css",
}

# Subset of some available modes
CODEMIRROR_MODES = {
    "css": "CodeMirror/mode/css/css.js",
    "django": "CodeMirror/mode/django/django.js",
    "html": "CodeMirror/mode/html/html.js",
    "json": "CodeMirror/mode/json/json.js",
    "javascript": "CodeMirror/mode/javascript/javascript.js",
    "markdown": "CodeMirror/mode/markdown/markdown.js",
    "php": "CodeMirror/mode/php/php.js",
    "perl": "CodeMirror/mode/perl/perl.js",
    "python": "CodeMirror/mode/python/python.js",
    "scss": "CodeMirror/mode/scss/scss.js",
    "rst": "CodeMirror/mode/restructuredtext/restructuredtext.js",
    "shell": "CodeMirror/mode/shell/shell.js",
}
