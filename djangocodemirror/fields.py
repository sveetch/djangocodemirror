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
    
    Accept three additional arguments ``codemirror_settings_name``, ``codemirror_settings_extra`` and ``embed_settings`` (the same as for ``CodeMirrorWidget``)
    """
    widget = CodeMirrorWidget
    
    def __init__(self, max_length=None, min_length=None, codemirror_settings_name='default', codemirror_settings_extra={}, embed_settings=False, *args, **kwargs):
        super(CodeMirrorField, self).__init__(max_length=max_length, min_length=min_length, *args, **kwargs)
        
        self.widget.codemirror_only = True
        self.widget.codemirror_settings_name = codemirror_settings_name
        self.widget.codemirror_settings_extra = codemirror_settings_extra
        self.widget.embed_settings = embed_settings
        
        self.widget.editor_config_manager = self.init_editor_config()

class DjangoCodeMirrorField(forms.CharField):
    """
    CharField dedicated to DjangoCodeMirror
    
    Accept four additional arguments ``codemirror_settings_name`` and 
    ``codemirror_settings_extra``, ``add_jquery`` and ``embed_settings`` (the same as for ``CodeMirrorWidget``)
    """
    widget = CodeMirrorWidget
    
    def __init__(self, max_length=None, min_length=None, codemirror_settings_name=settings_local.DJANGOCODEMIRROR_DEFAULT_SETTING, codemirror_settings_extra={}, embed_settings=False, add_jquery=False, *args, **kwargs):
        self.codemirror_only = False
        self.codemirror_settings_name = codemirror_settings_name
        self.codemirror_settings_extra = codemirror_settings_extra
        self.embed_settings = embed_settings
        self.add_jquery = add_jquery
        
        super(DjangoCodeMirrorField, self).__init__(max_length=max_length, min_length=min_length, *args, **kwargs)
        
        #self.codemirror_only = self.widget.codemirror_only = False
        #self.codemirror_settings_name = self.widget.codemirror_settings_name = codemirror_settings_name
        #self.embed_settings = self.widget.codemirror_settings_extra = codemirror_settings_extra
        #self.embed_settings = self.widget.embed_settings = embed_settings
        #self.add_jquery = self.widget.add_jquery = add_jquery
        
        self.widget.editor_config_manager = self.widget.init_editor_config()

    def widget_attrs(self, widget):
        """
        Given a Widget instance (*not* a Widget class), returns a dictionary of
        any HTML attributes that should be added to the Widget, based on this
        Field.
        """
        return {
            'codemirror_only': False,
            'codemirror_settings_name': self.codemirror_settings_name,
            'codemirror_settings_extra': self.codemirror_settings_extra,
            'embed_settings': self.embed_settings,
            'add_jquery': self.add_jquery,
        }
