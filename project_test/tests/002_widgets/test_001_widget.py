"""
Some dummy pinging to ensure urls are consistent
"""
import pytest

from django.core.urlresolvers import reverse

from djangocodemirror.widgets import CodeMirrorWidget, CodeMirrorAdminWidget


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
                        """<script>var id_sample_codemirror = CodeMirror.fromTextArea(document.getElementById("id_sample"),{"lineNumbers": true, "lineWrapping": true, "mode": "reStructuredText"});</script>""")
