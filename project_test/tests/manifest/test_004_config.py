"""
Tests against manifest for CodeMirror configurations
"""
import pytest


def test_config_empty(manifesto):
    """Empty config"""
    manifesto.autoregister()

    config = manifesto.get_codemirror_config('empty')

    assert config == {}


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
            'theme': 'nice_lesser_dark',
        },
    ),
])
def test_config_basic(manifesto, name, options):
    """Empty config"""
    manifesto.autoregister()

    config = manifesto.get_codemirror_config(name)

    assert config == options
