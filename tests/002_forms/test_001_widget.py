"""
Tests against field widgets
"""
import pytest

from djangocodemirror.widgets import CodeMirrorWidget, CodeMirrorAdminWidget

from tests.utils import assert_and_parse_html


def test_widget_init_manifest():
    """Check registered config"""
    widget = CodeMirrorWidget(config_name="empty")

    config = widget.init_manifest("empty")

    assert config.get_configs() == {
        'empty': {
            'modes': [],
            'addons': [],
            'themes': [],
            'css_bundle_name': 'dcm-empty_css',
            'js_bundle_name': 'dcm-empty_js',
        }
    }


def test_widget_basic():
    """Basic widget usage"""
    widget = CodeMirrorWidget(config_name="basic")

    rendered = widget.render("sample", "Hello World!")

    expected = ("""<textarea id="id_sample" name="sample" rows="10" cols="40">"""
                """Hello World!</textarea>""")

    assert assert_and_parse_html(rendered) == assert_and_parse_html(expected)


@pytest.mark.parametrize('name,expected', [
    (
        'basic',
        ("""<textarea id="id_sample" name="sample" rows="10" cols="40">"""
         """Hello World!</textarea>\n"""
         """<script>var id_sample_codemirror = """
         """CodeMirror.fromTextArea("""
         """document.getElementById("id_sample"),"""
         """{"mode": "rst"});</script>"""),
    ),
    (
        'with-options',
        ("""<textarea id="id_sample" name="sample" rows="10" cols="40">"""
         """Hello World!</textarea>\n"""
         """<script>var id_sample_codemirror = """
         """CodeMirror.fromTextArea("""
         """document.getElementById("id_sample"),"""
         """{"lineNumbers": true, "lineWrapping": true, "mode": "rst"});"""
         """</script>"""),
    ),
], ids=["basic", "with-options"])
def test_admin_widget(name, expected):
    """Admin widget usage"""
    widget = CodeMirrorAdminWidget(config_name=name)

    rendered = widget.render("sample", "Hello World!")

    assert assert_and_parse_html(rendered) == assert_and_parse_html(expected)


@pytest.mark.parametrize('name,expected', [
    (
        'basic',
        ("""<link href="/static/CodeMirror/lib/codemirror.css" type="text/css" media="all" rel="stylesheet">\n"""
         """<script type="text/javascript" src="/static/CodeMirror/lib/codemirror.js"></script>""")
    ),
    (
        'with-modes',
        ("""<link href="/static/CodeMirror/lib/codemirror.css" type="text/css" media="all" rel="stylesheet">\n"""
         """<script type="text/javascript" src="/static/CodeMirror/lib/codemirror.js"></script>\n"""
         """<script type="text/javascript" src="/static/CodeMirror/mode/rst/rst.js"></script>\n"""
         """<script type="text/javascript" src="/static/CodeMirror/mode/python/python.js"></script>""")
    ),
], ids=["basic", "with-modes"])
def test_widget_medias(name, expected):
    """Get widget medias"""
    widget = CodeMirrorWidget(config_name=name)
    rendered = str(widget.media)

    assert assert_and_parse_html(rendered) == assert_and_parse_html(expected)
