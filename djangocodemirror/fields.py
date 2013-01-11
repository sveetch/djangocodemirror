# -*- coding: utf-8 -*-
"""
Fields and widgets
"""
import json

from django import forms
from django.core.urlresolvers import reverse

from django.forms.widgets import flatatt
from django.utils.html import escape
from django.utils.safestring import mark_safe

from djangocodemirror import settings_local

class CodeMirrorAttrsWidget(forms.Textarea):
    """
    Widget to add a CodeMirror or DjangoCodeMirror instance on a textarea
    
    Take the same arguments than ``forms.Textarea`` and accepts three suplementary 
    optionnal arguments :
      
    NOTE: This is the old version of 'CodeMirrorWidget' it takes settings directly from 
          the ``codemirror_attrs`` argument but he is not aware of the settings name and 
          so is not available with the Bundles.
    
    * ``codemirror_attrs`` receive a dict with settings for the instance (CodeMirror 
      or DjangoCodeMirror);
    * ``codemirror_only`` to disable DjangoCodeMirror and use directly CodeMirror. By 
      default DjangoCodeMirror is always used;
    * ``embed_settings`` a boolean to active the automatic embed of the needed 
      Javascript code to launch a CodeMirror instance for the field. This is ``False`` 
      by default because there is lots of possible scenarios to manage your assets and 
      Javascript code. So if you active this, DjangoCodeMirror assets must be loaded 
      BEFORE your field appear in the HTML code;
    """
    def __init__(self, attrs=None, codemirror_attrs=None, codemirror_only=False, embed_settings=False):
        self.codemirror_attrs = codemirror_attrs or {}
        self.codemirror_only = codemirror_only
        self.embed_settings = embed_settings
        self._field_settings_cache = None
        
        default_attrs = {'cols': '40', 'rows': '10'}
        if attrs:
            default_attrs.update(attrs)
            
        super(CodeMirrorAttrsWidget, self).__init__(default_attrs)
        
        self.public_opts()

    def public_opts(self):
        """
        Agregate some settings and release them to instance attributes, so they can be 
        used by templatetags and others
        """
        self.opt_csrf_method_name = self.codemirror_attrs.get('csrf', False)
        self.opt_translations_plugins = settings_local.DJANGOCODEMIRROR_TRANSLATIONS
        self.opt_search_enabled = self.codemirror_attrs.get('search_enabled', False)
        self.opt_mode_syntax = None
        if 'mode' in self.codemirror_attrs:
            self.opt_mode_syntax = dict(settings_local.CODEMIRROR_MODES).get(self.codemirror_attrs['mode'], None)

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        assert 'id' in final_attrs, "CodeMirror widget attributes must contain 'id'"
        
        field_settings = self._get_codemirror_settings(final_attrs)
        
        html = [u'<textarea%s>%s</textarea>' % (flatatt(final_attrs), escape(value))]
        if self.embed_settings:
            html.append(self._build_codemirror_settings(final_attrs, field_settings))
        return mark_safe(u'\n'.join(html))

    def _get_codemirror_settings(self, final_attrs):
        if self._field_settings_cache is None:
            self._field_settings_cache = self._reverse_setting_urls( self.codemirror_attrs )
        return self._field_settings_cache

    def _build_codemirror_settings(self, final_attrs, field_settings):
        html = settings_local.DJANGOCODEMIRROR_FIELD_INIT_JS
        if self.codemirror_only:
            html = settings_local.CODEMIRROR_FIELD_INIT_JS
        return html.format(inputid=final_attrs['id'], settings=json.dumps(field_settings))

    def _reverse_setting_urls(self, field_settings):
        """
        Reverse urls with args and kwargs from a tuple ``(urlname, args, kwargs)``, 
        items than are strings are not reversed.
        
        This is only working on setting items : preview_url, help_link, quicksave_url
        """
        for name in ['preview_url', 'help_link', 'quicksave_url', 'settings_url']:
            if name in field_settings and not isinstance(field_settings.get(name, ''), basestring):
                args = []
                kwargs = {}
                urlname = field_settings[name][0]
                if len(field_settings[name])>1:
                    args = field_settings[name][1]
                    if len(field_settings[name])>2:
                        kwargs = field_settings[name][2]
                field_settings[name] = reverse(urlname, args=args, kwargs=kwargs)
        return field_settings
    
    #def _media(self):
        #"""
        #Adds necessary files (Js/CSS) to the widget's medias
        
        #NOTE: This has been deprecated in favor of a template tag, a more flexible solution
        #      But this method should be redone with the same technic that the template 
        #      tag, because without this the editor can not be used in the Admin anymore.
        #"""
        #css_items = [settings_local.CODEMIRROR_FILEPATH_CSS, settings_local.QTIP_FILEPATH_CSS]+[item[1] for item in settings_local.CODEMIRROR_THEMES]
        #js_items = [settings_local.CODEMIRROR_FILEPATH_LIB]
        
        #return forms.Media(
            #css={'all': tuple(css_items)},
            #js=tuple(js_items),
        #)
    #media = property(_media)

class CodeMirrorWidget(CodeMirrorAttrsWidget):
    """
    Inherits from ``CodeMirrorAttrsWidget`` but does not accept the ``codemirror_attrs`` 
    argument, instead it require ``codemirror_settings_name`` named argument.
    
    * ``codemirror_settings_name`` name of the settings to use, a valid key name from 
      ``settings.CODEMIRROR_SETTINGS``;
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
        kwargs['codemirror_attrs'] = settings_local.CODEMIRROR_SETTINGS[self.codemirror_settings_name]
        super(CodeMirrorWidget, self).__init__(*args, **kwargs)

class CodeMirrorField(forms.CharField):
    """
    CharField dedicated to CodeMirror
    
    Accept one suplementary arguments ``codemirror_attrs``
    (the same as for ``CodeMirrorWidget``)
    """
    widget = CodeMirrorWidget
    
    def __init__(self, max_length=None, min_length=None, codemirror_settings_name='default', *args, **kwargs):
        super(CodeMirrorField, self).__init__(max_length=max_length, min_length=min_length, *args, **kwargs)
        
        self.widget.codemirror_only = True
        self.widget.codemirror_settings_name = codemirror_settings_name
        self.widget.codemirror_attrs = settings_local.CODEMIRROR_SETTINGS[codemirror_settings_name]
        
        self.widget.public_opts()

class DjangoCodeMirrorField(forms.CharField):
    """
    CharField dedicated to DjangoCodeMirror
    
    Accept one suplementary arguments ``codemirror_attrs``
    (the same as for ``CodeMirrorWidget``).
    """
    widget = CodeMirrorWidget
    
    def __init__(self, max_length=None, min_length=None, codemirror_settings_name=settings_local.DJANGOCODEMIRROR_DEFAULT_SETTING, *args, **kwargs):
        super(DjangoCodeMirrorField, self).__init__(max_length=max_length, min_length=min_length, *args, **kwargs)
        
        self.widget.codemirror_only = False
        self.widget.codemirror_settings_name = codemirror_settings_name
        self.widget.codemirror_attrs = settings_local.CODEMIRROR_SETTINGS[codemirror_settings_name]
        
        self.widget.public_opts()
