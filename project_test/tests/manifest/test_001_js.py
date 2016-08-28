"""
Some dummy pinging to ensure urls are consistent
"""
import pytest

from djangocodemirror.manifest import CodeMirrorManifest


def test_empty_registry():
    """Empty registry"""
    manifesto = CodeMirrorManifest()

    assert manifesto.js() == ['CodeMirror/lib/codemirror.js']

def test_registred_empty():
    """An empty registred config"""
    manifesto = CodeMirrorManifest()

    manifesto.autoregister()

    assert manifesto.js('empty') == ['CodeMirror/lib/codemirror.js']

def test_registred_singles_js():
    """Explicitely registering some config"""
    manifesto = CodeMirrorManifest()

    manifesto.register('rst-basic') # Registred but not used
    manifesto.register('rst-with-addons')

    assert manifesto.js('rst-with-addons') == [
        'CodeMirror/lib/codemirror.js',
        'CodeMirror/lib/util/dialog.js',
        'CodeMirror/lib/util/search.js',
        'CodeMirror/lib/util/searchcursor.js',
        'CodeMirror/mode/rst/rst.js',
    ]

@pytest.mark.parametrize('name,assets', [
    (
        'rst-basic',
        [
        'CodeMirror/lib/codemirror.js',
        'CodeMirror/mode/rst/rst.js',
        ],
    ),
    (
        'rst-with-addons',
        [
            'CodeMirror/lib/codemirror.js',
            'CodeMirror/lib/util/dialog.js',
            'CodeMirror/lib/util/search.js',
            'CodeMirror/lib/util/searchcursor.js',
            'CodeMirror/mode/rst/rst.js',
        ],
    ),
    (
        'rst-with-modes',
        [
            'CodeMirror/lib/codemirror.js',
            'CodeMirror/mode/rst/rst.js',
            'CodeMirror/mode/python/python.js',
            'CodeMirror/mode/javascript/javascript.js',
        ],
    ),
    (
        'rst-with-all',
        [
            'CodeMirror/lib/codemirror.js',
            'CodeMirror/lib/util/dialog.js',
            'CodeMirror/lib/util/search.js',
            'CodeMirror/lib/util/searchcursor.js',
            'CodeMirror/mode/rst/rst.js',
            'CodeMirror/mode/python/python.js',
            'CodeMirror/mode/css/css.js',
        ],
    ),
    (
        None, # Mean all configs
        [
            'CodeMirror/lib/codemirror.js',
            'CodeMirror/lib/util/dialog.js',
            'CodeMirror/lib/util/search.js',
            'CodeMirror/lib/util/searchcursor.js',
            'CodeMirror/mode/rst/rst.js',
            'CodeMirror/mode/python/python.js',
            'CodeMirror/mode/javascript/javascript.js',
            'CodeMirror/mode/css/css.js',
        ],
    ),
])
def test_autoregister(name, assets):
    """Checking js assets after autoregister"""
    manifesto = CodeMirrorManifest()

    manifesto.autoregister()
    import json
    print json.dumps(manifesto.js(name), indent=4)
    assert manifesto.js(name) == assets
