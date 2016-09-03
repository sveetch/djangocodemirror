"""
Some dummy pinging to ensure urls are consistent
"""
import pytest

from django.core.urlresolvers import reverse

from djangocodemirror.fields import DjangoCodeMirrorField


def test_field_basic():
    """Basic field usage"""
    field = DjangoCodeMirrorField(label="Foo", required=True,
                                  config_name="rst-basic",
                                  initial='Hello World!')

    rendered = field.widget.render("foo", "bar")

    assert rendered == ("""<textarea cols="40" name="foo" rows="10">\r\n"""
                        """bar</textarea>""")
