"""
Some dummy pinging to ensure urls are consistent
"""
import pytest

from django.core.urlresolvers import reverse

from djangocodemirror.widgets import CodeMirrorWidget, CodeMirrorAdminWidget


def test_widget_init_manifest():
    """Check registered config"""
    widget = CodeMirrorWidget(config_name="empty")

    config = widget.init_manifest("empty")

    assert config.get_configs() == {
            'empty': {
            'mode': None,
            'modes': [],
            'addons': [],
            'themes': [],
            'css_bundle_name': 'dcm-empty_css',
            'js_bundle_name': 'dcm-empty_js',
        }
    }


def test_widget_basic():
    """Basic widget usage"""
    widget = CodeMirrorWidget(config_name="rst-basic")

    rendered = widget.render("sample", "Hello World!")

    assert rendered == ("""<textarea cols="40" name="sample" rows="10">\r\n"""
                        """Hello World!</textarea>""")


def test_adminwidget_basic():
    """Basic admin widget usage"""
    widget = CodeMirrorAdminWidget(config_name="rst-basic")

    rendered = widget.render("sample", "Hello World!")

    assert rendered == ("""<textarea cols="40" name="sample" rows="10">\r\n"""
                        """Hello World!</textarea>\n"""
                        """<script>var id_sample_codemirror = """
                        """CodeMirror.fromTextArea("""
                        """document.getElementById("id_sample"),"""
                        """{"lineNumbers": true, "lineWrapping": true"""
                        """, "mode": "rst"});</script>""")


def test_widget_medias():
    """Get widget medias"""
    widget = CodeMirrorWidget(config_name="rst-basic")

    assert str(widget.media) == ("""<link href="/static/CodeMirror/lib/codemirror.css" type="text/css" media="all" rel="stylesheet" />\n"""
                                 """<script type="text/javascript" src="/static/CodeMirror/lib/codemirror.js"></script>\n"""
                                 """<script type="text/javascript" src="/static/CodeMirror/mode/restructuredtext/restructuredtext.js"></script>""")
