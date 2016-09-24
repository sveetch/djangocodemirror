"""
Tests against template tags for Codemirror config
"""
import json
import pytest

from djangocodemirror.widgets import CodeMirrorWidget
from djangocodemirror.templatetags.djangocodemirror_tags import CodemirrorAssetTagRender

from project.forms import SampleForm, ManyFieldsSampleForm


def test_resolve_widget():
    """
    Check widget resolving from a field

    Note:
        We should test also against BoundField but it seems to involve template
        resolving and i'm too lazy for that now.
    """
    f = SampleForm()

    w = CodemirrorAssetTagRender().resolve_widget(f.fields['foo'])

    assert isinstance(w, CodeMirrorWidget) == True


def test_register_from_fields(settings):
    manifesto = CodemirrorAssetTagRender()

    f = ManyFieldsSampleForm()
    f.as_p()

    configs = manifesto.register_from_fields(
        f.fields['foo'],
        f.fields['pika'],
        f.fields['ping']
    )

    assert configs == ['rst-basic', 'rst-with-all']


def test_render_asset_html(settings):
    manifesto = CodemirrorAssetTagRender()

    css = manifesto.render_asset_html("foo/bar.css",
                               settings.CODEMIRROR_CSS_ASSET_TAG)

    js = manifesto.render_asset_html("foo/plop/bar.js",
                              settings.CODEMIRROR_JS_ASSET_TAG)

    assert css == """<link rel="stylesheet" href="/static/foo/bar.css">"""

    assert js == ("""<script type="text/javascript" """
                  """src="/static/foo/plop/bar.js"></script>""")


def test_css_html(settings):
    manifesto = CodemirrorAssetTagRender()

    f = SampleForm()
    f.as_p()

    manifesto.register_from_fields(
        f.fields['foo'],
    )

    assets = manifesto.css_html()

    assert assets == '<link rel="stylesheet" href="/static/CodeMirror/lib/codemirror.css">'


def test_js_html(settings):
    manifesto = CodemirrorAssetTagRender()

    f = SampleForm()
    f.as_p()

    manifesto.register_from_fields(
        f.fields['foo'],
    )

    assets = manifesto.js_html()

    assert assets == ("""<script type="text/javascript" src="/static/CodeMirror/lib/codemirror.js"></script>"""
                      """<script type="text/javascript" src="/static/CodeMirror/mode/rst/rst.js"></script>""")


def test_instance_html(settings):
    # manifesto.
    manifesto = CodemirrorAssetTagRender()

    f = SampleForm()
    f.as_p()

    manifesto.register_from_fields(
        f.fields['foo'],
    )

    w = manifesto.resolve_widget(f.fields['foo'])

    html = manifesto.codemirror_html(w.config_name, "plop_codemirror", "plop")

    output = ("""<script>var plop_codemirror = CodeMirror.fromTextArea("""
              """document.getElementById("plop"),"""
              """{"lineNumbers": true, "lineWrapping": true, "mode": "rst"});"""
              """</script>""")

    assert html == output
