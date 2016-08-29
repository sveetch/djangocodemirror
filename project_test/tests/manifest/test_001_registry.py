"""
Tests against manifest for Javascript assets
"""
import pytest

from django.conf import settings

from djangocodemirror.manifest import NotRegistered, UnknowConfig


def test_registry_empty(settings, manifesto):
    """Empty registry"""
    assert manifesto.get_configs() == {}


@pytest.mark.parametrize('name,options', [
    (
        'empty',
        {
            'mode': None,
            'modes': [],
            'addons': [],
            'themes': [],
            'css_bundle_name': 'dcm-empty_css',
            'js_bundle_name': 'dcm-empty_js',
        },
    ),
    (
        'rst-basic',
        {
            'mode': 'rst',
            'lineWrapping': True,
            'lineNumbers': True,
            'modes': [],
            'addons': [],
            'themes': [],
            'css_bundle_name': 'dcm-rst-basic_css',
            'js_bundle_name': 'dcm-rst-basic_js',
        },
    ),
])
def test_register(settings, manifesto, name, options):
    """Register a config"""
    registred = manifesto.register(name)

    assert registred == options


def test_autoregister(manifesto):
    """Auto register every config from settings"""
    manifesto.autoregister()
    # Check only about some names, not all
    assert ('empty' in manifesto.registry) == True
    assert ('rst-basic' in manifesto.registry) == True
    assert ('rst-with-all' in manifesto.registry) == True


def test_register_nonexistent(settings, manifesto):
    """Try to register a config name that does not exist"""
    with pytest.raises(UnknowConfig):
        registred = manifesto.register('nope')


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
            'modes': [],
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
