"""
Tests against manifest for CodeMirror configurations
"""
import pytest

from djangocodemirror.manifest import NotRegistered


def test_raw_config_empty(manifesto):
    """Empty config"""
    manifesto.autoregister()

    config = manifesto.get_codemirror_parameters('empty')

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
            'mode': 'rst',
            'lineWrapping': True,
            'lineNumbers': True,
            'modes': ['rst'],
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
            'mode': 'rst',
            'lineWrapping': True,
            'lineNumbers': True,
        },
    ),
    (
        'rst-with-themes',
        {
            'mode': 'rst',
            'lineWrapping': True,
            'lineNumbers': True,
            'theme': 'elegant',
        },
    ),
    (
        'rst-with-all',
        {
            'mode': 'rst',
            'lineWrapping': True,
            'lineNumbers': True,
            'theme': 'neat',
        },
    ),
])
def test_codemirror_parameters(manifesto, name, options):
    """CodeMirror parameters"""
    manifesto.autoregister()

    config = manifesto.get_codemirror_parameters(name)

    assert config == options
