"""
Tests against template tags for Codemirror config
"""
import pytest

from djangocodemirror.templatetags.djangocodemirror_tags import (
    codemirror_instance,
)

from project.forms import SampleForm


def test_codemirror_instance_without_assets():
    html = codemirror_instance('rst-basic', 'foo_codemirror', 'id_foo', assets=False)

    output = ("""<script>var foo_codemirror = CodeMirror.fromTextArea("""
              """document.getElementById("id_foo"),"""
              """{"lineNumbers": true, "lineWrapping": true, "mode": "rst"});"""
              """</script>""")

    assert html == output


def test_codemirror_instance_with_assets():
    html = codemirror_instance('rst-basic', 'foo_codemirror', 'id_foo', assets=True)

    output = ("""<link rel="stylesheet" href="/static/CodeMirror/lib/codemirror.css">"""
              """<script type="text/javascript" src="/static/CodeMirror/lib/codemirror.js"></script>"""
              """<script type="text/javascript" src="/static/CodeMirror/mode/restructuredtext/restructuredtext.js"></script>"""
              """<script>var foo_codemirror = CodeMirror.fromTextArea(document.getElementById("id_foo"),{"lineNumbers": true, "lineWrapping": true, "mode": "rst"});</script>""")

    assert html == output
