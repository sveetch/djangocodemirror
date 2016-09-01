# -*- coding: utf-8 -*-
"""
Fields
"""
from django import forms

from djangocodemirror import settings_local
from djangocodemirror.widgets import CodeMirrorWidget

class DjangoCodeMirrorField(forms.CharField):
    """
    A CharField that comes with CodeMirrorWidget.

    Arguments:
        config_name (string): A Codemirror config name available in
            ``settings.CODEMIRROR_SETTINGS``. Default is ``empty``.
    """
    def __init__(self, config_name='empty', *args, **kwargs):
        self.config_name = config_name
        kwargs.update({'widget': CodeMirrorWidget})

        # Initialize widget with given config name if the field has been
        # bounded.
        widget = kwargs.get('widget', self.widget) or self.widget
        if isinstance(widget, type):
            kwargs['widget'] = widget(config_name=config_name)

        super(DjangoCodeMirrorField, self).__init__(*args, **kwargs)

