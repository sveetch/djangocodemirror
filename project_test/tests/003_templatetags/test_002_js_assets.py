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

    assets = djangocodemirror_tags.codemirror_field_js_assets(f.fields['foo'])

    assert assets == ("""<script type="text/javascript" src="/static/CodeMirror/lib/codemirror.js"></script>\n"""
                      """<script type="text/javascript" src="/static/CodeMirror/mode/restructuredtext/restructuredtext.js"></script>""")


def test_codemirror_multiple_field_js_assets():
    """Test codemirror_field_js_assets tag"""
    f = ManyFieldsSampleForm({'foo': 'bar'})

    f.as_p()

    assets = djangocodemirror_tags.codemirror_field_js_assets(
        f.fields['foo'],
        f.fields['pika'],
        f.fields['ping']
    )

    assert assets == ("""<script type="text/javascript" src="/static/CodeMirror/lib/codemirror.js"></script>\n"""
                      """<script type="text/javascript" src="/static/CodeMirror/lib/util/dialog.js"></script>\n"""
                      """<script type="text/javascript" src="/static/CodeMirror/lib/util/search.js"></script>\n"""
                      """<script type="text/javascript" src="/static/CodeMirror/lib/util/searchcursor.js"></script>\n"""
                      """<script type="text/javascript" src="/static/CodeMirror/mode/restructuredtext/restructuredtext.js"></script>\n"""
                      """<script type="text/javascript" src="/static/CodeMirror/mode/python/python.js"></script>\n"""
                      """<script type="text/javascript" src="/static/CodeMirror/mode/css/css.js"></script>""")
