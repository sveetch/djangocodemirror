"""
Tests against template tags for CSS assets
"""
import json
import pytest

from djangocodemirror.exceptions import CodeMirrorFieldBundleError
from djangocodemirror.widgets import CodeMirrorWidget
from djangocodemirror.templatetags.djangocodemirror_tags import (
    codemirror_field_css_assets,
    codemirror_field_css_bundle,
)

from sandbox.forms import SampleForm, ManyFieldsSampleForm, NoBundleForm


def test_codemirror_single_field_js_assets():
    """Test codemirror_field_js_assets tag for a single field"""
    f = SampleForm()

    f.as_p()

    assets = codemirror_field_css_assets(f.fields['foo'])

    assert assets == '<link rel="stylesheet" href="/static/CodeMirror/lib/codemirror.css">'


def test_codemirror_multiple_field_js_assets():
    """Test codemirror_field_js_assets tag for a many field"""
    f = ManyFieldsSampleForm()

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
    f = ManyFieldsSampleForm()

    f.as_p()

    name = codemirror_field_css_bundle(f.fields['foo'])

    assert name == 'dcm-basic_css'


def test_codemirror_field_css_bundle_error():
    """Test bundle exception from codemirror_field_css_bundle filter for a
       single field"""
    f = NoBundleForm()

    f.as_p()

    with pytest.raises(CodeMirrorFieldBundleError) as e:
        name = codemirror_field_css_bundle(f.fields['foo'])
