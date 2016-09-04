"""
Tests against field usage inside a form
"""
import pytest

from django import forms

from project.forms import SampleForm


def test_form_basic():
    """Basic field usage"""
    f = SampleForm({'foo': 'bar'})

    assert f.as_p() == ("""<p><label for="id_foo">Foo:</label> """
                        """<textarea cols="40" id="id_foo" name="foo" """
                        """rows="10">\r\nbar</textarea></p>""")
