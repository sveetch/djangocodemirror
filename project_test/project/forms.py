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
                          config_name="basic",
                          initial='Hello World!')


class ManyFieldsSampleForm(forms.Form):
    """
    Basic form for tests with multiple CodeMirrorField
    """
    foo = CodeMirrorField(label="Foo",
                          required=True,
                          config_name="basic",
                          initial='Hello World!')
    pika = CodeMirrorField(label="Pika",
                          required=True,
                          config_name="basic",
                          initial='Catch them all')
    ping = CodeMirrorField(label="Ping",
                          required=True,
                          config_name="with-all",
                          initial='Zouip')


class WrongForm(forms.Form):
    """
    Form with a field using an unknow config name
    """
    foo = CodeMirrorField(label="Foo",
                          required=True,
                          config_name="nope",
                          initial='Hello World!')
