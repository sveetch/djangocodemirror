"""
Sample forms
"""
from django import forms

from djangocodemirror.fields import CodeMirrorField


class SampleForm(forms.Form):
    """
    Just a very basic form for tests
    """
    foo = CodeMirrorField(label="Foo",
                          required=True,
                          config_name="rst-basic",
                          initial='Hello World!')
