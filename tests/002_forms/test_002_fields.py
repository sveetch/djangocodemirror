"""
Tests against form fields
"""
import pytest

from djangocodemirror.fields import CodeMirrorField

from tests.utils import assert_and_parse_html


def test_field_basic():
    """Basic field usage"""
    field = CodeMirrorField(label="Foo", required=True,
                                  config_name="basic",
                                  initial='Hello World!')

    rendered = field.widget.render("foo", "bar")

    expected = ("""<textarea id="id_foo" name="foo" rows="10" cols="40">"""
                """bar</textarea>""")

    assert assert_and_parse_html(rendered) == assert_and_parse_html(expected)
