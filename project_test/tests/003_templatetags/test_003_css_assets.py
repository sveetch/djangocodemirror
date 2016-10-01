"""
Tests against template tags for Codemirror config
"""
import json
import pytest

from djangocodemirror.widgets import CodeMirrorWidget
from djangocodemirror.templatetags.djangocodemirror_tags import (
    codemirror_field_css_assets,
    codemirror_field_css_bundle,
)

from project.forms import SampleForm, ManyFieldsSampleForm


def test_codemirror_single_field_js_assets():
    """Test codemirror_field_js_assets tag for a single field"""
    f = SampleForm({'foo': 'bar'})

    f.as_p()

    assets = codemirror_field_css_assets(f.fields['foo'])

    assert assets == '<link rel="stylesheet" href="/static/CodeMirror/lib/codemirror.css">'


def test_codemirror_multiple_field_js_assets():
    """Test codemirror_field_js_assets tag for a many field"""
    f = ManyFieldsSampleForm({'foo': 'bar'})

    f.as_p()

    assets = codemirror_field_css_assets(
        f.fields['foo'],
        f.fields['pika'],
        f.fields['ping']
    )

    assert assets == ("""<link rel="stylesheet" href="/static/CodeMirror/lib/codemirror.css">"""
                      """<link rel="stylesheet" href="/static/CodeMirror/theme/eclipse.css">"""
                      """<link rel="stylesheet" href="/static/CodeMirror/theme/neat.css">"""
                      """<link rel="stylesheet" href="/static/CodeMirror/theme/ambiance.css">""")


def test_codemirror_field_css_bundle():
    """Test codemirror_field_css_bundle filter for a single field"""
    f = ManyFieldsSampleForm({'foo': 'bar'})

    f.as_p()

    name = codemirror_field_css_bundle(f.fields['foo'])

    assert name == 'dcm-basic_css'
