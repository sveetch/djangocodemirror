"""
Tests against template tags for Codemirror config
"""
import pytest

from djangocodemirror.templatetags.djangocodemirror_tags import (
    codemirror_instance,
)

from sandbox.forms import SampleForm


def test_codemirror_instance_without_assets():
    html = codemirror_instance('basic', 'foo_codemirror', 'id_foo', assets=False)

    output = ("""<script>var foo_codemirror = CodeMirror.fromTextArea("""
              """document.getElementById("id_foo"),"""
              """{"mode": "rst"});"""
              """</script>""")

    assert html == output


def test_codemirror_instance_with_assets():
    html = codemirror_instance('basic', 'foo_codemirror', 'id_foo', assets=True)

    output = ("""<link rel="stylesheet" href="/static/CodeMirror/lib/codemirror.css">"""
              """<script type="text/javascript" src="/static/CodeMirror/lib/codemirror.js"></script>"""
              """<script>var foo_codemirror = CodeMirror.fromTextArea("""
              """document.getElementById("id_foo"),{"mode": "rst"});"""
              """</script>""")

    assert html == output
