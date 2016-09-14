"""
Tests against manifest for Javascript assets
"""
import pytest

from django.conf import settings

from djangocodemirror.manifest import UnknowConfig


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
            'modes': ['rst'],
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


def test_register_many(manifesto):
    """Register many config"""
    registred = manifesto.register_many('empty', 'rst-basic')

    assert registred == [
        {
            'mode': None,
            'modes': [],
            'addons': [],
            'themes': [],
            'css_bundle_name': 'dcm-empty_css',
            'js_bundle_name': 'dcm-empty_js',
        },
        {
            'mode': 'rst',
            'lineWrapping': True,
            'lineNumbers': True,
            'modes': ['rst'],
            'addons': [],
            'themes': [],
            'css_bundle_name': 'dcm-rst-basic_css',
            'js_bundle_name': 'dcm-rst-basic_js',
        },
    ]


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
