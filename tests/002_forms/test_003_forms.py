"""
Tests against field usage inside a form
"""
import pytest

from django import forms
from django import VERSION as django_versioning

from sandbox.forms import SampleForm

from tests.utils import assert_and_parse_html


def test_form_basic():
    """Basic field usage"""
    f = SampleForm({'foo': 'bar'})

    rendered = f.as_p()
    expected = ("""<p><label for="id_foo">Foo:</label> """
                """<textarea id="id_foo" name="foo" """
                """rows="10" cols="40" required>bar</textarea></p>""")

    assert assert_and_parse_html(rendered) == assert_and_parse_html(expected)

