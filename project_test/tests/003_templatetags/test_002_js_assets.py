"""
Tests against template tags for Codemirror config
"""
import json
import pytest

from djangocodemirror.manifest import CodeMirrorFieldBundle
from djangocodemirror.widgets import CodeMirrorWidget
from djangocodemirror.templatetags.djangocodemirror_tags import (
    codemirror_field_js_assets,
    codemirror_field_js_bundle,
)

from project.forms import SampleForm, ManyFieldsSampleForm, WrongForm


def test_codemirror_single_field_js_assets():
    """Test codemirror_field_js_assets tag for a single field"""
    f = SampleForm()

    f.as_p()

    assets = codemirror_field_js_assets(f.fields['foo'])

    assert assets == """<script type="text/javascript" src="/static/CodeMirror/lib/codemirror.js"></script>"""


def test_codemirror_multiple_field_js_assets():
    """Test codemirror_field_js_assets tag for many fields"""
    f = ManyFieldsSampleForm()

    f.as_p()

    assets = codemirror_field_js_assets(
        f.fields['foo'],
        f.fields['pika'],
        f.fields['ping']
    )

    assert assets == ("""<script type="text/javascript" src="/static/CodeMirror/lib/codemirror.js"></script>"""
                      """<script type="text/javascript" src="/static/CodeMirror/lib/util/dialog.js"></script>"""
                      """<script type="text/javascript" src="/static/CodeMirror/mode/rst/rst.js"></script>"""
                      """<script type="text/javascript" src="/static/CodeMirror/mode/python/python.js"></script>""")


def test_codemirror_field_js_bundle():
    """Test codemirror_field_js_bundle filter for a single field"""
    f = ManyFieldsSampleForm()

    f.as_p()

    name = codemirror_field_js_bundle(f.fields['foo'])

    assert name == 'dcm-basic_js'
