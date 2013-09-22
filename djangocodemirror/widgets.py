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

class CodeMirrorAttrsWidget(forms.Textarea):
    """
    Widget to add a CodeMirror or DjangoCodeMirror instance on a textarea
    
    Take the same arguments than ``forms.Textarea`` and accepts four suplementary 
    optionnal arguments :
      
    * ``codemirror_attrs`` receive a dict with settings for the instance (CodeMirror 
      or DjangoCodeMirror);
    * ``codemirror_only`` to disable DjangoCodeMirror and use directly CodeMirror. By 
      default DjangoCodeMirror is always used;
    * ``embed_settings`` a boolean to active the automatic embed of the needed 
      Javascript code to launch a CodeMirror instance for the field. This is ``False`` 
      by default because there is lots of possible scenarios to manage your assets and 
      Javascript code. So if you active this, DjangoCodeMirror assets must be loaded 
      BEFORE your field appear in the HTML code;
    * ``add_jquery`` an string to specify a path to the jQuery lib to add to 
      the used assets, it's not really usefull because generally your pages allready 
      embed it;
    """
    def __init__(self, attrs=None, codemirror_attrs=None, codemirror_only=False, embed_settings=False, add_jquery=False, codemirror_settings_name='default'):
        self.codemirror_settings_name = codemirror_settings_name
        self.codemirror_attrs = codemirror_attrs
        self.codemirror_only = codemirror_only
        self.embed_settings = embed_settings
        self.add_jquery = add_jquery
        self._field_settings_cache = None
        
        default_attrs = {'cols': '40', 'rows': '10'}
        if attrs:
            default_attrs.update(attrs)
            
        super(CodeMirrorAttrsWidget, self).__init__(default_attrs)

    def init_editor_config(self):
        return ConfigManager(
            codemirror_settings_name=self.codemirror_settings_name,
            codemirror_attrs=self.codemirror_attrs,
            codemirror_only=self.codemirror_only,
            embed_settings=self.embed_settings,
            add_jquery=self.add_jquery,
        )

    def render(self, name, value, attrs=None):
        self.editor_config_manager = self.init_editor_config()
        
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        assert 'id' in final_attrs, "CodeMirror widget attributes must contain 'id'"
        
        self.editor_config_manager.merge_config(**final_attrs)
        
        html = [u'<textarea%s>%s</textarea>' % (flatatt(final_attrs), escape(value))]
        # Append HTML for the Javascript settings just below the textarea
        if self.embed_settings:
            html.append(self._build_codemirror_settings(final_attrs, self.editor_config_manager.editor_config))
            
        return mark_safe(u'\n'.join(html))

    def _build_codemirror_settings(self, final_attrs, editor_config):
        """build HTML for the Javascript settings"""
        html = settings_local.DJANGOCODEMIRROR_FIELD_INIT_JS
        if self.codemirror_only:
            html = settings_local.CODEMIRROR_FIELD_INIT_JS
        return html.format(inputid=final_attrs['id'], settings=json.dumps(editor_config))
    
    def _media(self):
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
    media = property(_media)

class CodeMirrorWidget(CodeMirrorAttrsWidget):
    """
    Inherits from ``CodeMirrorAttrsWidget`` but does not accept the ``codemirror_attrs`` 
    argument, instead it require ``codemirror_settings_name`` named argument.
    
    * ``codemirror_settings_name`` name of the settings to use, a valid key name from 
      ``settings.CODEMIRROR_SETTINGS``;
    * ``codemirror_settings_extra`` an optional dict to override some settings;
    * ``codemirror_only`` to disable DjangoCodeMirror and use directly CodeMirror. By 
      default DjangoCodeMirror is always used;
    * ``embed_settings`` a boolean to active the automatic embed of the needed 
      Javascript code to launch a CodeMirror instance for the field. This is ``False`` 
      by default because there is lots of possible scenarios to manage your assets and 
      Javascript code. So if you active this, DjangoCodeMirror assets must be loaded 
      BEFORE your field appear in the HTML code;
    """
    def __init__(self, *args, **kwargs):
        if 'codemirror_attrs' in kwargs:
            raise TypeError("CodeMirrorWidget does not accept anymore the 'codemirror_attrs' named argument, for this see at CodeMirrorAttrsWidget")
        
        self.codemirror_settings_name = kwargs.pop('codemirror_settings_name', 'default')
        
        super(CodeMirrorWidget, self).__init__(*args, **kwargs)

class NewCodeMirrorWidget(forms.Textarea):
    """
    ...
    """
    def __init__(self, attrs=None):
        default_attrs = {'cols': '40', 'rows': '10'}
        if attrs:
            default_attrs.update(attrs)
            
        super(NewCodeMirrorWidget, self).__init__(default_attrs)

    def init_editor_config(self):
        return ConfigManager(
            codemirror_settings_name=self.codemirror_settings_name,
            codemirror_attrs=self.codemirror_attrs,
            codemirror_only=self.codemirror_only,
            embed_settings=self.embed_settings,
            add_jquery=self.add_jquery,
        )

    def render(self, name, value, attrs=None):
        self.editor_config_manager = self.init_editor_config()
        
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        assert 'id' in final_attrs, "CodeMirror widget attributes must contain 'id'"
        
        self.editor_config_manager.merge_config(**final_attrs)
        
        html = [u'<textarea%s>%s</textarea>' % (flatatt(final_attrs), escape(value))]
        # Append HTML for the Javascript settings just below the textarea
        if self.embed_settings:
            html.append(self._build_codemirror_settings(final_attrs, self.editor_config_manager.editor_config))
            
        return mark_safe(u'\n'.join(html))

    def _build_codemirror_settings(self, final_attrs, editor_config):
        """build HTML for the Javascript settings"""
        html = settings_local.DJANGOCODEMIRROR_FIELD_INIT_JS
        if self.codemirror_only:
            html = settings_local.CODEMIRROR_FIELD_INIT_JS
        return html.format(inputid=final_attrs['id'], settings=json.dumps(editor_config))
    
    def _media(self):
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
    media = property(_media)
