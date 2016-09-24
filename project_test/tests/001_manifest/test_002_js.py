"""
Tests against manifest for Javascript assets
"""
import pytest

from django.conf import settings as legacy_settings

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
    assert manifesto.resolve_mode('python') == settings.CODEMIRROR_MODES['python']


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
            legacy_settings.CODEMIRROR_MODES['rst'],
        ],
    ),
    (
        'rst-with-addons',
        [
            ADDON_DIALOG,
            ADDON_SEARCH,
            ADDON_SEARCHCURSOR,
            legacy_settings.CODEMIRROR_MODES['rst'],
        ],
    ),
    (
        'rst-with-modes',
        [
            legacy_settings.CODEMIRROR_MODES['rst'],
            legacy_settings.CODEMIRROR_MODES['python'],
            legacy_settings.CODEMIRROR_MODES['javascript'],
        ],
    ),
    (
        'rst-with-all',
        [
            ADDON_DIALOG,
            ADDON_SEARCH,
            ADDON_SEARCHCURSOR,
            legacy_settings.CODEMIRROR_MODES['rst'],
            legacy_settings.CODEMIRROR_MODES['python'],
            legacy_settings.CODEMIRROR_MODES['css'],
        ],
    ),
    (
        None, # Mean all configs
        [
            ADDON_DIALOG,
            ADDON_SEARCH,
            ADDON_SEARCHCURSOR,
            legacy_settings.CODEMIRROR_MODES['rst'],
            legacy_settings.CODEMIRROR_MODES['python'],
            legacy_settings.CODEMIRROR_MODES['javascript'],
            legacy_settings.CODEMIRROR_MODES['css'],
        ],
    ),
])
def test_js_autoregister(settings, manifesto, name, assets):
    """Checking js assets after autoregister"""

    manifesto.autoregister()
    #import json
    #print json.dumps(manifesto.js(name), indent=4)
    assert manifesto.js(name) == settings.CODEMIRROR_BASE_JS+assets


def test_js_bundle_names_single(settings, manifesto):
    """Checking Javascript bundle names for a single config"""
    manifesto.register('rst-basic') # Registred but not used
    manifesto.register('rst-with-addons')

    assert manifesto.js_bundle_names('rst-with-addons') == [
        'dcm-rst-with-addons_js',
    ]


def test_js_bundle_names_all(settings, manifesto):
    """Checking Javascript bundle names for every registered config"""
    manifesto.autoregister()

    assert manifesto.js_bundle_names() == [
        'dcm-rst-with-themes_js',
        'dcm-rst-with-modes_js',
        'dcm-mode-naive_js',
        'dcm-rst-with-all_js',
        'dcm-rst-with-addons_js',
        'dcm-empty_js',
        'dcm-rst-basic_js',
    ]
