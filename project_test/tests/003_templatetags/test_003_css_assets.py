"""
Tests against template tags for Codemirror config

TODO: Static dir prefixed for sanity!!!
"""
import json
import pytest

from djangocodemirror.widgets import CodeMirrorWidget
from djangocodemirror.templatetags import djangocodemirror_tags

from project.forms import SampleForm, ManyFieldsSampleForm


def test_codemirror_single_field_js_assets():
    """Test codemirror_field_js_assets tag"""
    f = SampleForm({'foo': 'bar'})

    f.as_p()

    assets = djangocodemirror_tags.codemirror_field_css_assets(f.fields['foo'])

    assert assets == '<link rel="stylesheet" href="/static/CodeMirror/lib/codemirror.css">'


def test_codemirror_multiple_field_js_assets():
    """Test codemirror_field_js_assets tag"""
    f = ManyFieldsSampleForm({'foo': 'bar'})

    f.as_p()

    assets = djangocodemirror_tags.codemirror_field_css_assets(
        f.fields['foo'],
        f.fields['pika'],
        f.fields['ping']
    )

    assert assets == ("""<link rel="stylesheet" href="/static/CodeMirror/lib/codemirror.css">\n"""
                      """<link rel="stylesheet" href="/static/CodeMirror/theme/eclipse.css">\n"""
                      """<link rel="stylesheet" href="/static/CodeMirror/theme/neat.css">""")
