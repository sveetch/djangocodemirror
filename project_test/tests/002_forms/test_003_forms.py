"""
Tests against field usage inside a form
"""
import pytest

from django import forms
from django import VERSION as django_versioning

from project.forms import SampleForm


def test_form_basic():
    """Basic field usage"""
    f = SampleForm({'foo': 'bar'})

    if django_versioning[1] < 10:
        assert f.as_p() == ("""<p><label for="id_foo">Foo:</label> """
                            """<textarea cols="40" id="id_foo" name="foo" """
                            """rows="10">\r\nbar</textarea></p>""")
    else:
        # Since Django 1.10, required form fields set the required HTML
        assert f.as_p() == ("""<p><label for="id_foo">Foo:</label> """
                            """<textarea cols="40" id="id_foo" name="foo" """
                            """rows="10" required>\r\nbar</textarea></p>""")

