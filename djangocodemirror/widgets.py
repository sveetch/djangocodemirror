# -*- coding: utf-8 -*-
"""
Fields and widgets
"""
import json, copy

from django import forms
from django.core.urlresolvers import reverse

from django.forms.widgets import flatatt
from django.utils.html import escape
from django.utils.safestring import mark_safe

from djangocodemirror import settings_local
from djangocodemirror.config import ConfigManager

class CodeMirrorWidget(forms.Textarea):
    """
    Widget to add a CodeMirror or DjangoCodeMirror instance on a textarea
    Take the same arguments than ``forms.Textarea`` and accepts one suplementary
    optionnal arguments :
    
    * ``config_name`` name of the settings to use, a valid key name from
    ``settings.CODEMIRROR_SETTINGS``. Default to "default" that is the default config 
    with minimal options;
    """
    def __init__(self, attrs=None, config_name='default', **kwargs):
        super(CodeMirrorWidget, self).__init__(attrs=attrs, **kwargs)
        self.config_name = config_name
    
    def init_editor_config(self):
        return ConfigManager(
            config_name=self.config_name,
        )

    def render(self, name, value, attrs=None):
        if not hasattr(self, "editor_config_manager"):
            self.editor_config_manager = self.init_editor_config()
        
        final_attrs = self.build_attrs(attrs, name=name)
        
        html = [super(CodeMirrorWidget, self).render(name, value, attrs)]
        # Append HTML for the Javascript settings just below the textarea
        if self.editor_config_manager.settings['embed_settings']:
            html.append(self._build_codemirror_settings(final_attrs))
            
        return mark_safe(u'\n'.join(html))

    def _build_codemirror_settings(self, final_attrs):
        """build HTML for the Javascript settings"""
        html = settings_local.DJANGOCODEMIRROR_FIELD_INIT_JS
        if self.editor_config_manager.settings['codemirror_only']:
            html = settings_local.CODEMIRROR_FIELD_INIT_JS
        return html.format(inputid=final_attrs['id'], settings=json.dumps(self.editor_config_manager.editor_config))

    @property
    def media(self):
        """
        Adds necessary files (Js/CSS) to the widget's medias
        """
        if not hasattr(self, "editor_config_manager"):
            self.editor_config_manager = self.init_editor_config()
        css, js = self.editor_config_manager.find_assets()
        return forms.Media(
            css={"all": css},
            js=js
        )
