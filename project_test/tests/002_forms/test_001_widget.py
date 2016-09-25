"""
Tests against field widgets
"""
import pytest

from djangocodemirror.widgets import CodeMirrorWidget, CodeMirrorAdminWidget


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

    assert rendered == ("""<textarea cols="40" name="sample" rows="10">\r\n"""
                        """Hello World!</textarea>""")


@pytest.mark.parametrize('name,html', [
    (
        'basic',
        ("""<textarea cols="40" name="sample" rows="10">\r\n"""
         """Hello World!</textarea>\n"""
         """<script>var id_sample_codemirror = """
         """CodeMirror.fromTextArea("""
         """document.getElementById("id_sample"),"""
         """{"mode": "rst"});</script>"""),
    ),
    (
        'with-options',
        ("""<textarea cols="40" name="sample" rows="10">\r\n"""
         """Hello World!</textarea>\n"""
         """<script>var id_sample_codemirror = """
         """CodeMirror.fromTextArea("""
         """document.getElementById("id_sample"),"""
         """{"lineNumbers": true, "lineWrapping": true, "mode": "rst"});"""
         """</script>"""),
    ),
], ids=["basic", "with-options"])
def test_admin_widget(name, html):
    """Admin widget usage"""
    widget = CodeMirrorAdminWidget(config_name=name)

    rendered = widget.render("sample", "Hello World!")

    assert rendered == html


@pytest.mark.parametrize('name,attempted', [
    (
        'basic',
        ("""<link href="/static/CodeMirror/lib/codemirror.css" type="text/css" media="all" rel="stylesheet" />\n"""
         """<script type="text/javascript" src="/static/CodeMirror/lib/codemirror.js"></script>""")
    ),
    (
        'with-modes',
        ("""<link href="/static/CodeMirror/lib/codemirror.css" type="text/css" media="all" rel="stylesheet" />\n"""
         """<script type="text/javascript" src="/static/CodeMirror/lib/codemirror.js"></script>\n"""
         """<script type="text/javascript" src="/static/CodeMirror/mode/rst/rst.js"></script>\n"""
         """<script type="text/javascript" src="/static/CodeMirror/mode/python/python.js"></script>""")
    ),
], ids=["basic", "with-modes"])
def test_widget_medias(name, attempted):
    """Get widget medias"""
    widget = CodeMirrorWidget(config_name=name)
    medias = str(widget.media)

    assert medias == attempted
