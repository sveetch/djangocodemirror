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
from djangocodemirror.templatetags.djangocodemirror_assets import FieldAssetsMixin

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
    def __init__(self, attrs=None, codemirror_attrs=None, codemirror_only=False, embed_settings=False, add_jquery=False):
        self.codemirror_attrs = codemirror_attrs or {}
        self.codemirror_only = codemirror_only
        self.embed_settings = embed_settings
        self.add_jquery = add_jquery
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
            
        #test to remove, needed sometime because the property() catch exceptions
        #print self._media()
            
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
            if name in field_settings and field_settings.get(name, None) is not None and not isinstance(field_settings.get(name, None), basestring):
                args = []
                kwargs = {}
                urlname = field_settings[name][0]
                if len(field_settings[name])>1:
                    args = field_settings[name][1]
                    if len(field_settings[name])>2:
                        kwargs = field_settings[name][2]
                field_settings[name] = reverse(urlname, args=args, kwargs=kwargs)
        return field_settings
    
    def _media(self):
        """
        Adds necessary files (Js/CSS) to the widget's medias
        """
        mix = FieldAssetsMixin()
        app_settings = copy.deepcopy(mix._default_app_settings)
        app_settings = mix.get_app_settings(app_settings, self)
        css, js = mix.find_assets(app_settings, self)
        return forms.Media(
            css=css,
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
        self.codemirror_settings_extra = kwargs.pop('codemirror_settings_extra', {})
        kwargs['codemirror_attrs'] = settings_local.CODEMIRROR_SETTINGS[self.codemirror_settings_name]
        kwargs['codemirror_attrs'].update(self.codemirror_settings_extra)
        super(CodeMirrorWidget, self).__init__(*args, **kwargs)
