"""
Tests against manifest for Javascript assets
"""
import pytest

from django.conf import settings

from djangocodemirror.manifest import UnknowMode


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


def test_resolve_mode_success(settings, manifesto):
    """Resolve a mode name"""
    assert manifesto.resolve_mode('Python') == settings.CODEMIRROR_MODES['Python']


def test_resolve_mode_error(settings, manifesto):
    """Try to resolve a mode name that does not exist"""
    with pytest.raises(UnknowMode):
        manifesto.resolve_mode('mode-nope')


def test_js_registred_singles(settings, manifesto):
    """Explicitely registering some config"""
    manifesto.register('rst-basic') # Registred but not used
    manifesto.register('rst-with-addons')

    assert manifesto.js('rst-with-addons') == settings.CODEMIRROR_BASE_JS+[
        ADDON_DIALOG,
        ADDON_SEARCH,
        ADDON_SEARCHCURSOR,
        settings.CODEMIRROR_MODES['reStructuredText'],
    ]


@pytest.mark.parametrize('name,assets', [
    (
        'empty',
        [],
    ),
    (
        'rst-basic',
        [
            settings.CODEMIRROR_MODES['reStructuredText'],
        ],
    ),
    (
        'rst-with-addons',
        [
            ADDON_DIALOG,
            ADDON_SEARCH,
            ADDON_SEARCHCURSOR,
            settings.CODEMIRROR_MODES['reStructuredText'],
        ],
    ),
    (
        'rst-with-modes',
        [
            settings.CODEMIRROR_MODES['reStructuredText'],
            settings.CODEMIRROR_MODES['Python'],
            settings.CODEMIRROR_MODES['JavaScript'],
        ],
    ),
    (
        'rst-with-all',
        [
            ADDON_DIALOG,
            ADDON_SEARCH,
            ADDON_SEARCHCURSOR,
            settings.CODEMIRROR_MODES['reStructuredText'],
            settings.CODEMIRROR_MODES['Python'],
            settings.CODEMIRROR_MODES['CSS'],
        ],
    ),
    (
        None, # Mean all configs
        [
            ADDON_DIALOG,
            ADDON_SEARCH,
            ADDON_SEARCHCURSOR,
            settings.CODEMIRROR_MODES['reStructuredText'],
            settings.CODEMIRROR_MODES['Python'],
            settings.CODEMIRROR_MODES['JavaScript'],
            settings.CODEMIRROR_MODES['CSS'],
        ],
    ),
])
def test_js_autoregister(settings, manifesto, name, assets):
    """Checking js assets after autoregister"""
    manifesto.autoregister()
    #import json
    #print json.dumps(manifesto.js(name), indent=4)
    assert manifesto.js(name) == settings.CODEMIRROR_BASE_JS+assets
