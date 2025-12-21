import pytest

from django.conf import settings as legacy_settings

from djangocodemirror.exceptions import UnknowModeError


# Path shortcut
ADDON_DIALOG = "CodeMirror/lib/util/dialog.js"
ADDON_SEARCH = "CodeMirror/lib/util/search.js"
ADDON_SEARCHCURSOR = "CodeMirror/lib/util/searchcursor.js"


def test_js_empty_registry(settings, manifesto):
    """
    Empty registry
    """
    assert manifesto.js() == settings.CODEMIRROR_BASE_JS


def test_js_registred_empty(settings, manifesto):
    """
    An empty registred config
    """
    manifesto.autoregister()

    assert manifesto.js("empty") == settings.CODEMIRROR_BASE_JS


def test_resolve_mode_success(settings, manifesto):
    """
    Resolve a mode name
    """
    assert manifesto.resolve_mode("python") == settings.CODEMIRROR_MODES["python"]


def test_resolve_mode_error(settings, manifesto):
    """
    Try to resolve a mode name that does not exist
    """
    with pytest.raises(UnknowModeError):
        manifesto.resolve_mode("mode-nope")


def test_js_registred_singles(settings, manifesto):
    """
    Explicitely registering some config
    """
    manifesto.register("basic")
    manifesto.register("with-addons")

    assert manifesto.js("with-addons") == settings.CODEMIRROR_BASE_JS + [
        ADDON_DIALOG,
    ]


@pytest.mark.parametrize("name,expected_assets", [
    (
        "empty",
        [],
    ),
    (
        "basic",
        [],
    ),
    (
        "with-addons",
        [
            ADDON_DIALOG,
        ],
    ),
    (
        "with-modes",
        [
            legacy_settings.CODEMIRROR_MODES["rst"],
            legacy_settings.CODEMIRROR_MODES["python"],
        ],
    ),
    (
        "with-all",
        [
            ADDON_DIALOG,
            legacy_settings.CODEMIRROR_MODES["rst"],
            legacy_settings.CODEMIRROR_MODES["python"],
        ],
    ),
    (
        # Mean all configs
        None,
        [
            ADDON_DIALOG,
            legacy_settings.CODEMIRROR_MODES["rst"],
            legacy_settings.CODEMIRROR_MODES["python"],
        ],
    ),
])
def test_js_autoregister(settings, manifesto, name, expected_assets):
    """
    Checking js assets after autoregister
    """
    manifesto.autoregister()

    # Expected value includes base JS files and files from parameters
    expected = settings.CODEMIRROR_BASE_JS + expected_assets

    assert manifesto.js(name) == expected


def test_js_bundle_names_single(settings, manifesto):
    """
    Checking Javascript bundle names for a single config
    """
    manifesto.register("basic")
    manifesto.register("with-addons")

    assert manifesto.js_bundle_names("with-addons") == [
        "dcm-with-addons_js",
    ]


def test_js_bundle_names_all(settings, manifesto):
    """
    Checking Javascript bundle names for every registered config
    """
    manifesto.autoregister()

    assert manifesto.js_bundle_names() == [
        "dcm-basic_js",
        "dcm-empty_js",
        "dcm-with-addons_js",
        "dcm-with-all_js",
        "dcm-with-extra_css_js",
        "dcm-with-modes_js",
        "dcm-with-options_js",
        "dcm-with-themes_js",
    ]
