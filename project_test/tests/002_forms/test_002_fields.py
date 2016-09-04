"""
Tests against form fields
"""
import pytest

from djangocodemirror.fields import CodeMirrorField


def test_field_basic():
    """Basic field usage"""
    field = CodeMirrorField(label="Foo", required=True,
                                  config_name="rst-basic",
                                  initial='Hello World!')

    rendered = field.widget.render("foo", "bar")

    assert rendered == ("""<textarea cols="40" name="foo" rows="10">\r\n"""
                        """bar</textarea>""")
