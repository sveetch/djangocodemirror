"""
Tests against manifest for CodeMirror configurations
"""
import pytest

from djangocodemirror.manifest import NotRegistered


def test_raw_config_empty(manifesto):
    """Empty config"""
    manifesto.autoregister()

    config = manifesto.get_codemirror_config('empty')

    assert config == {}


def test_get_config_success(settings, manifesto):
    """Use get_config on non registered name"""
    manifesto.autoregister()
    assert manifesto.get_config('empty') == {
        'mode': None,
        'modes': [],
        'addons': [],
        'themes': [],
        'css_bundle_name': 'dcm-empty_css',
        'js_bundle_name': 'dcm-empty_js',
    }


def test_get_config_error(settings, manifesto):
    """Use get_config on non registered name"""
    manifesto.autoregister()
    with pytest.raises(NotRegistered):
        registred = manifesto.get_config('nope')


def test_get_configs_single_success(settings, manifesto):
    """Use get_configs for one registred config"""
    manifesto.register('empty')
    manifesto.register('rst-basic')

    registred = manifesto.get_configs('empty')

    assert registred == {
        'empty': {
            'mode': None,
            'modes': [],
            'addons': [],
            'themes': [],
            'css_bundle_name': 'dcm-empty_css',
            'js_bundle_name': 'dcm-empty_js',
        },
    }


def test_get_configs_multiple_success(settings, manifesto):
    """Use get_configs for all registred configs"""
    manifesto.register('empty')
    manifesto.register('rst-basic')

    registred = manifesto.get_configs()

    assert registred == {
        'empty': {
            'mode': None,
            'modes': [],
            'addons': [],
            'themes': [],
            'css_bundle_name': 'dcm-empty_css',
            'js_bundle_name': 'dcm-empty_js',
        },
        'rst-basic': {
            'mode': 'reStructuredText',
            'lineWrapping': True,
            'lineNumbers': True,
            'modes': ['reStructuredText'],
            'addons': [],
            'themes': [],
            'css_bundle_name': 'dcm-rst-basic_css',
            'js_bundle_name': 'dcm-rst-basic_js',
        },
    }


def test_get_configs_single_error(settings, manifesto):
    """Use get_configs on single non registered name"""
    manifesto.autoregister()
    with pytest.raises(NotRegistered):
        registred = manifesto.get_configs('nope')


@pytest.mark.parametrize('name,options', [
    (
        'empty',
        {},
    ),
    (
        'rst-basic',
        {
            'mode': 'reStructuredText',
            'lineWrapping': True,
            'lineNumbers': True,
        },
    ),
    (
        'rst-with-themes',
        {
            'mode': 'reStructuredText',
            'lineWrapping': True,
            'lineNumbers': True,
            'theme': 'elegant',
        },
    ),
    (
        'rst-with-all',
        {
            'mode': 'reStructuredText',
            'lineWrapping': True,
            'lineNumbers': True,
            'theme': 'neat',
        },
    ),
])
def test_config_basic(manifesto, name, options):
    """Empty config"""
    manifesto.autoregister()

    config = manifesto.get_codemirror_config(name)

    assert config == options
