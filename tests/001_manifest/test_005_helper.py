"""
Tests against configuration helper
"""
import pytest

from djangocodemirror.helper import codemirror_settings_update


SAMPLE_DICT = {
    'empty': {},
    'basic': {
        'mode': 'rst',
    },
    'with-options': {
        'mode': 'rst',
        'lineWrapping': True,
    },
    'with-all': {
        'mode': 'rst',
        'lineWrapping': True,
        'modes': ['rst', 'python'],
    },
}


SAMPLE_PARAMETERS = {
    'foo': 'bar',
    'css_bundle_name': None,
    'lineWrapping': False,
    'modes': ['rst'],
}


@pytest.mark.parametrize('on,names,attempted', [
    # On some configs and unfiltered
    (
        ['basic', 'with-all'],
        None,
        {
            'empty': {},
            'basic': {
                'mode': 'rst',
                'foo': 'bar',
                'css_bundle_name': None,
                'lineWrapping': False,
                'modes': ['rst'],
            },
            'with-options': {
                'mode': 'rst',
                'lineWrapping': True,
            },
            'with-all': {
                'mode': 'rst',
                'foo': 'bar',
                'css_bundle_name': None,
                'lineWrapping': False,
                'modes': ['rst'],
            },
        }
    ),

    # On every configs and filtered
    (
        None,
        ['basic', 'with-all'],
        {
            'basic': {
                'mode': 'rst',
                'foo': 'bar',
                'css_bundle_name': None,
                'lineWrapping': False,
                'modes': ['rst'],
            },
            'with-all': {
                'mode': 'rst',
                'foo': 'bar',
                'css_bundle_name': None,
                'lineWrapping': False,
                'modes': ['rst'],
            },
        }
    ),

    # On some configs and filtered
    (
        ['basic'],
        ['empty', 'basic', 'with-all'],
        {
            'empty': {},
            'basic': {
                'mode': 'rst',
                'foo': 'bar',
                'css_bundle_name': None,
                'lineWrapping': False,
                'modes': ['rst'],
            },
            'with-all': {
                'mode': 'rst',
                'lineWrapping': True,
                'modes': ['rst', 'python'],
            },
        }
    ),

    # On every configs and unfiltered
    (
        None,
        None,
        {
            'empty': {
                'foo': 'bar',
                'css_bundle_name': None,
                'lineWrapping': False,
                'modes': ['rst'],
            },
            'basic': {
                'mode': 'rst',
                'foo': 'bar',
                'css_bundle_name': None,
                'lineWrapping': False,
                'modes': ['rst'],
            },
            'with-options': {
                'mode': 'rst',
                'foo': 'bar',
                'css_bundle_name': None,
                'lineWrapping': False,
                'modes': ['rst'],
            },
            'with-all': {
                'mode': 'rst',
                'foo': 'bar',
                'css_bundle_name': None,
                'lineWrapping': False,
                'modes': ['rst'],
            },
        }
    ),
])
def test_config_helper(on, names, attempted):
    """Helper to update parameters from selected config and with filtered
       returned dict"""
    result = codemirror_settings_update(SAMPLE_DICT, SAMPLE_PARAMETERS, on=on,
                                        names=names)

    assert result == attempted
