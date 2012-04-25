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

from djangocodemirror import (CODEMIRROR_SETTINGS, DJANGOCODEMIRROR_DEFAULT_SETTING, 
                                CODEMIRROR_FIELD_INIT_JS, 
                                DJANGOCODEMIRROR_FIELD_INIT_JS, CODEMIRROR_MODES,
                                CODEMIRROR_FILEPATH_LIB, CODEMIRROR_FILEPATH_CSS, CODEMIRROR_THEMES,
                                DJANGOCODEMIRROR_FILEPATH_LIB, DJANGOCODEMIRROR_FILEPATH_CSS,
                                DJANGOCODEMIRROR_FILEPATH_TRANSLATION, DJANGOCODEMIRROR_TRANSLATIONS,
                                DJANGOCODEMIRROR_FILEPATH_BUTTONS, DJANGOCODEMIRROR_FILEPATH_METHODS,
                                DJANGOCODEMIRROR_FILEPATH_CONSOLE,
                                DJANGOCODEMIRROR_FILEPATH_COOKIES, DJANGOCODEMIRROR_FILEPATH_CSRF,
                                QTIP_FILEPATH_LIB, QTIP_FILEPATH_CSS)

class CodeMirrorWidget(forms.Textarea):
    """
    Widget to add a CodeMirror or DjangoCodeMirror instance on a textarea
    
    Accept two suplementary optionnal arguments :
    
    * ``codemirror_attrs`` receive a dict with settings for the instance (CodeMirror 
      or DjangoCodeMirror);
    * ``codemirror_only`` to disable DjangoCodeMirror and use directly CodeMirror. By 
      default DjangoCodeMirror is always used.
    
    Recoit le même argument optionnel ``attr`` que le widget ``forms.Textarea`` plus un 
    autre argument optionnel ``codemirror_attrs`` qui est un dictionnaire des options 
    de l'instance CodeMirror
    """
    def __init__(self, attrs=None, codemirror_attrs=None, codemirror_only=False):
        self.codemirror_attrs = codemirror_attrs or {}
        self.codemirror_only = codemirror_only
        default_attrs = {'cols': '40', 'rows': '10'}
        if attrs:
            default_attrs.update(attrs)
        super(CodeMirrorWidget, self).__init__(default_attrs)

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        assert 'id' in final_attrs, "CodeMirror widget attributes must contain 'id'"
        
        html = [u'<textarea%s>%s</textarea>' % (flatatt(final_attrs), escape(value))]
        html.append(self._get_codemirror_settings(final_attrs))
        return mark_safe(u'\n'.join(html))

    def _get_codemirror_settings(self, final_attrs):
        settings = self._reverse_setting_urls( self.codemirror_attrs )
        html = DJANGOCODEMIRROR_FIELD_INIT_JS
        if self.codemirror_only:
            html = CODEMIRROR_FIELD_INIT_JS
        return html.format(inputid=final_attrs['id'], settings=json.dumps(settings))

    def _reverse_setting_urls(self, settings):
        """
        Reverse urls with args and kwargs from a tuple ``(urlname, args, kwargs)``, 
        items than are strings are not reversed.
        
        This is only working on setting items : preview_url, help_link, quicksave_url
        """
        for name in ['preview_url', 'help_link', 'quicksave_url']:
            if name in settings and not isinstance(settings.get(name, ''), basestring):
                args = []
                kwargs = {}
                urlname = settings[name][0]
                if len(settings[name])>1:
                    args = settings[name][1]
                    if len(settings[name])>2:
                        kwargs = settings[name][2]
                settings[name] = reverse(urlname, args=args, kwargs=kwargs)
        return settings
    
    def _media(self):
        """
        Adds necessary files (Js/CSS) to the widget's medias
        """
        css_items = [CODEMIRROR_FILEPATH_CSS, QTIP_FILEPATH_CSS]+[item[1] for item in CODEMIRROR_THEMES]
        js_items = [CODEMIRROR_FILEPATH_LIB]
        # Set CodeMirror 'mode' js media only if 'mode' has been defined
        # Use the 'mode' name as a key in the settings registry
        if 'mode' in self.codemirror_attrs:
            mode = dict(CODEMIRROR_MODES).get(self.codemirror_attrs['mode'], None)
            if mode:
                js_items.append(mode)
        # DjangoCodeMirror files if enabled
        # DJANGOCODEMIRROR_FILEPATH_TRANSLATION, DJANGOCODEMIRROR_TRANSLATIONS,
        if not self.codemirror_only:
            css_items.append(DJANGOCODEMIRROR_FILEPATH_CSS)
            # DjangoCodeMirror must be instanciated AFTER CodeMirror
            js_items.append(DJANGOCODEMIRROR_FILEPATH_TRANSLATION)
            for lang in DJANGOCODEMIRROR_TRANSLATIONS:
                js_items.append(lang)
            js_items.append(DJANGOCODEMIRROR_FILEPATH_BUTTONS)
            js_items.append(DJANGOCODEMIRROR_FILEPATH_METHODS)
            js_items.append(DJANGOCODEMIRROR_FILEPATH_LIB)
            js_items.append(QTIP_FILEPATH_LIB)
            js_items.append(DJANGOCODEMIRROR_FILEPATH_CONSOLE)
            # Use CSRF lib only if setted and used
            if DJANGOCODEMIRROR_FILEPATH_CSRF and self.codemirror_attrs.get('csrf', False):
                js_items.append(DJANGOCODEMIRROR_FILEPATH_CSRF)
            # Adds Jquery Cookies plugin only if setted
            if DJANGOCODEMIRROR_FILEPATH_COOKIES:
                js_items.append(DJANGOCODEMIRROR_FILEPATH_COOKIES)
        
        return forms.Media(
            css={'all': tuple(css_items)},
            js=tuple(js_items),
        )
    media = property(_media)

class CodeMirrorField(forms.CharField):
    """
    CharField dedicated to CodeMirror
    
    Accept one suplementary arguments ``codemirror_attrs``
    (the same as for ``CodeMirrorWidget``)
    """
    widget = CodeMirrorWidget
    
    def __init__(self, max_length=None, min_length=None, codemirror_attrs=CODEMIRROR_SETTINGS['default'], *args, **kwargs):
        super(CodeMirrorField, self).__init__(max_length=max_length, min_length=min_length, *args, **kwargs)
        
        self.widget.codemirror_attrs.update(codemirror_attrs or {})
        self.widget.codemirror_only = True

class DjangoCodeMirrorField(forms.CharField):
    """
    CharField dedicated to DjangoCodeMirror
    
    Accept one suplementary arguments ``codemirror_attrs``
    (the same as for ``CodeMirrorWidget``).
    """
    widget = CodeMirrorWidget
    
    def __init__(self, max_length=None, min_length=None, codemirror_attrs=CODEMIRROR_SETTINGS[DJANGOCODEMIRROR_DEFAULT_SETTING], *args, **kwargs):
        super(DjangoCodeMirrorField, self).__init__(max_length=max_length, min_length=min_length, *args, **kwargs)
        
        self.widget.codemirror_attrs.update(codemirror_attrs or {})
        self.widget.codemirror_only = False
