# -*- coding: utf-8 -*-
"""
Fields
"""
from django import forms

from djangocodemirror import settings_local
from djangocodemirror.widgets import CodeMirrorWidget

class DjangoCodeMirrorField(forms.CharField):
    def __init__(self, config_name='default', *args, **kwargs):
        self.config_name = config_name
        kwargs.update({'widget': CodeMirrorWidget})
        
        widget = kwargs.get('widget', self.widget) or self.widget
        if isinstance(widget, type):
            kwargs['widget'] = widget(config_name=config_name)        
        
        super(DjangoCodeMirrorField, self).__init__(*args, **kwargs)

