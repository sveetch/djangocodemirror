# -*- coding: utf-8 -*-
"""
Form field
==========

"""
from django import forms

from djangocodemirror.widgets import CodeMirrorWidget


class CodeMirrorField(forms.CharField):
    """
    A CharField that comes with CodeMirrorWidget.

    Arguments:
        config_name (string): A Codemirror config name available in
            ``settings.CODEMIRROR_SETTINGS``. Default is ``empty``.
    """
    def __init__(self, *args, **kwargs):
        self.config_name = kwargs.pop('config_name', 'empty')
        # Add Codemirror widget to the field
        kwargs.update({'widget': CodeMirrorWidget})

        # Initialize widget with given config name if the field has been
        # bounded.
        widget = kwargs.get('widget', None) or self.widget
        if isinstance(widget, type):
            kwargs['widget'] = widget(config_name=self.config_name)

        super(CodeMirrorField, self).__init__(*args, **kwargs)
