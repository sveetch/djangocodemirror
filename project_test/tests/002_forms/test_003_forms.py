"""
Some dummy pinging to ensure urls are consistent
"""
import pytest

from django.core.urlresolvers import reverse
from django import forms

from djangocodemirror.fields import DjangoCodeMirrorField


class SampleForm(forms.Form):
    foo = DjangoCodeMirrorField(label="Foo", required=True,
                                config_name="rst-basic",
                                initial='Hello World!')


def test_form_basic():
    """Basic field usage"""
    f = SampleForm({'foo': 'bar'})

    assert f.as_p() == ("""<p><label for="id_foo">Foo:</label> """
                        """<textarea cols="40" id="id_foo" name="foo" """
                        """rows="10">\r\nbar</textarea></p>""")
