"""
Tests against manifest for CSS assets
"""
import pytest

from django.conf import settings

from djangocodemirror.manifest import UnknowTheme


def test_css_empty_registry(settings, manifesto):
    """Empty registry"""
    assert manifesto.css() == settings.CODEMIRROR_BASE_CSS


def test_css_registred_empty(settings, manifesto):
    """An empty registred config"""
    manifesto.autoregister()

    assert manifesto.css('empty') == settings.CODEMIRROR_BASE_CSS


def test_resolve_theme_success(settings, manifesto):
    """Resolve a theme name"""
    result = manifesto.resolve_theme('ambiance')
    attempt = settings.CODEMIRROR_THEMES['ambiance']

    assert result == attempt


def test_resolve_theme_error(settings, manifesto):
    """Try to resolve a theme name that does not exist"""
    with pytest.raises(UnknowTheme):
        manifesto.resolve_theme('theme-nope')


def test_css_registred_singles(settings, manifesto):
    """Explicitely registering some config"""
    manifesto.register('basic') # Registred but not used
    manifesto.register('with-themes')

    assert manifesto.css('with-themes') == settings.CODEMIRROR_BASE_CSS+[
        settings.CODEMIRROR_THEMES['eclipse'],
        settings.CODEMIRROR_THEMES['elegant'],
    ]


@pytest.mark.parametrize('name,assets', [
    (
        'empty',
        [],
    ),
    (
        'with-themes',
        [
            settings.CODEMIRROR_THEMES['eclipse'],
            settings.CODEMIRROR_THEMES['elegant'],
        ],
    ),
    (
        'with-all',
        [
            settings.CODEMIRROR_THEMES['eclipse'],
            settings.CODEMIRROR_THEMES['neat'],
            settings.CODEMIRROR_THEMES['ambiance'],
        ],
    ),
    (
        None, # Mean all configs
        [
            settings.CODEMIRROR_THEMES['eclipse'],
            settings.CODEMIRROR_THEMES['elegant'],
            settings.CODEMIRROR_THEMES['neat'],
            settings.CODEMIRROR_THEMES['ambiance'],
        ],
    ),
])
def test_css_autoregister(settings, manifesto, name, assets):
    """Checking CSS assets after autoregister"""
    manifesto.autoregister()

    assert manifesto.css(name) == settings.CODEMIRROR_BASE_CSS+assets


def test_css_bundle_names_single(settings, manifesto):
    """Checking CSS bundle names for a single config"""
    manifesto.register('basic') # Registred but not used
    manifesto.register('with-addons')

    assert manifesto.css_bundle_names('with-addons') == [
        'dcm-with-addons_css',
    ]


def test_css_bundle_names_all(settings, manifesto):
    """Checking CSS bundle names for every registered config"""
    manifesto.autoregister()

    assert manifesto.css_bundle_names() == [
        'dcm-basic_css',
        'dcm-empty_css',
        'dcm-with-addons_css',
        'dcm-with-all_css',
        'dcm-with-extra_css_css',
        'dcm-with-modes_css',
        'dcm-with-options_css',
        'dcm-with-themes_css'
    ]
