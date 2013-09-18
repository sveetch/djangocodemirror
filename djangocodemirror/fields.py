# -*- coding: utf-8 -*-
"""
Fields
"""
from django import forms

from djangocodemirror import settings_local
from djangocodemirror.widgets import CodeMirrorWidget

class CodeMirrorField(forms.CharField):
    """
    CharField dedicated to CodeMirror
    
    Accept two additional arguments ``codemirror_settings_name`` and 
    ``codemirror_settings_extra`` (the same as for ``CodeMirrorWidget``)
    """
    widget = CodeMirrorWidget
    
    def __init__(self, max_length=None, min_length=None, codemirror_settings_name='default', codemirror_settings_extra={}, *args, **kwargs):
        super(CodeMirrorField, self).__init__(max_length=max_length, min_length=min_length, *args, **kwargs)
        
        self.widget.codemirror_only = True
        self.widget.codemirror_settings_name = codemirror_settings_name
        self.widget.codemirror_settings_extra = codemirror_settings_extra
        self.widget.codemirror_attrs = settings_local.CODEMIRROR_SETTINGS[codemirror_settings_name]
        self.widget.codemirror_attrs.update(codemirror_settings_extra)
        
        self.widget.public_opts()

class DjangoCodeMirrorField(forms.CharField):
    """
    CharField dedicated to DjangoCodeMirror
    
    Accept two additional arguments ``codemirror_settings_name`` and 
    ``codemirror_settings_extra`` (the same as for ``CodeMirrorWidget``)
    """
    widget = CodeMirrorWidget
    
    def __init__(self, max_length=None, min_length=None, codemirror_settings_name=settings_local.DJANGOCODEMIRROR_DEFAULT_SETTING, codemirror_settings_extra={}, *args, **kwargs):
        super(DjangoCodeMirrorField, self).__init__(max_length=max_length, min_length=min_length, *args, **kwargs)
        
        self.widget.codemirror_only = False
        self.widget.codemirror_settings_name = codemirror_settings_name
        self.widget.codemirror_settings_extra = codemirror_settings_extra
        self.widget.codemirror_attrs = settings_local.CODEMIRROR_SETTINGS[codemirror_settings_name]
        self.widget.codemirror_attrs.update(codemirror_settings_extra)
        
        self.widget.public_opts()
