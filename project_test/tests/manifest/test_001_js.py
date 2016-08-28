"""
Tests against manifest for Javascript assets
"""
import pytest

from django.conf import settings


# Since we dont have names for addons, name it here to avoid retyping them for
# every test
ADDON_DIALOG = 'CodeMirror/lib/util/dialog.js'
ADDON_SEARCH = 'CodeMirror/lib/util/search.js'
ADDON_SEARCHCURSOR = 'CodeMirror/lib/util/searchcursor.js'


def test_js_empty_registry(settings, manifesto):
    """Empty registry"""
    assert manifesto.js() == settings.CODEMIRROR_BASE_JS


def test_js_registred_empty(settings, manifesto):
    """An empty registred config"""
    manifesto.autoregister()

    assert manifesto.js('empty') == settings.CODEMIRROR_BASE_JS


def test_js_registred_singles(settings, manifesto):
    """Explicitely registering some config"""
    manifesto.register('rst-basic') # Registred but not used
    manifesto.register('rst-with-addons')

    assert manifesto.js('rst-with-addons') == settings.CODEMIRROR_BASE_JS+[
        ADDON_DIALOG,
        ADDON_SEARCH,
        ADDON_SEARCHCURSOR,
        settings.CODEMIRROR_MODES['rst'],
    ]


@pytest.mark.parametrize('name,assets', [
    (
        'empty',
        [],
    ),
    (
        'rst-basic',
        [
            settings.CODEMIRROR_MODES['rst'],
        ],
    ),
    (
        'rst-with-addons',
        [
            ADDON_DIALOG,
            ADDON_SEARCH,
            ADDON_SEARCHCURSOR,
            settings.CODEMIRROR_MODES['rst'],
        ],
    ),
    (
        'rst-with-modes',
        [
            settings.CODEMIRROR_MODES['rst'],
            settings.CODEMIRROR_MODES['python'],
            settings.CODEMIRROR_MODES['javascript'],
        ],
    ),
    (
        'rst-with-all',
        [
            ADDON_DIALOG,
            ADDON_SEARCH,
            ADDON_SEARCHCURSOR,
            settings.CODEMIRROR_MODES['rst'],
            settings.CODEMIRROR_MODES['python'],
            settings.CODEMIRROR_MODES['css'],
        ],
    ),
    (
        None, # Mean all configs
        [
            ADDON_DIALOG,
            ADDON_SEARCH,
            ADDON_SEARCHCURSOR,
            settings.CODEMIRROR_MODES['rst'],
            settings.CODEMIRROR_MODES['python'],
            settings.CODEMIRROR_MODES['javascript'],
            settings.CODEMIRROR_MODES['css'],
        ],
    ),
])
def test_js_autoregister(settings, manifesto, name, assets):
    """Checking js assets after autoregister"""
    manifesto.autoregister()
    #import json
    #print json.dumps(manifesto.js(name), indent=4)
    assert manifesto.js(name) == settings.CODEMIRROR_BASE_JS+assets
