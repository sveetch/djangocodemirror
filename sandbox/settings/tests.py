"""
Django settings for tests
"""
from sandbox.settings.base import *  # noqa: F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Media directory dedicated to tests to avoid polluting other environment
# media directory
MEDIA_ROOT = VAR_PATH / "media-tests"  # noqa: F405

# Disable every cache because it can trouble test on expected results
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

"""
Not all those configs won't work for real, there are almost all just for
unittests
"""
CODEMIRROR_SETTINGS = {
    "empty": {},
    "basic": {
        "mode": "rst",
    },
    "with-options": {
        "mode": "rst",
        "lineWrapping": True,
        "lineNumbers": True,
    },
    "with-modes": {
        "mode": "rst",
        "modes": ["rst", "python"],
    },
    "with-themes": {
        "mode": "rst",
        "theme": "elegant",
        "themes": ["eclipse", "elegant"],
    },
    "with-addons": {
        "mode": "rst",
        "addons": [
            "CodeMirror/lib/util/dialog.js",
        ],
    },
    "with-extra_css": {
        "mode": "rst",
        "extra_css": [
            "CodeMirror/theme/ambiance.css",
        ],
    },
    "without-bundle": {
        "modes": ["rst", "python"],
        "css_bundle_name": None,
        "js_bundle_name": None,
        "themes": ["eclipse", "elegant"],
    },
    "with-all": {
        "mode": "rst",
        "lineWrapping": True,
        "lineNumbers": True,
        "addons": [
            "CodeMirror/lib/util/dialog.js",
        ],
        "modes": ["rst", "python"],
        "theme": "neat",
        "themes": ["eclipse", "neat"],
        "extra_css": [
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
