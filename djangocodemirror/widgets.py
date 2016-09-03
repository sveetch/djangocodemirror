# -*- coding: utf-8 -*-
"""
Form field widgets
==================

"""
import json, copy

from django import forms

from django.conf import settings
from django.utils.safestring import mark_safe

from djangocodemirror.manifest import CodeMirrorManifest
#from djangocodemirror import settings_local
#from djangocodemirror.config import ConfigManager


class CodeMirrorWidget(forms.Textarea):
    """
    Widget to add a CodeMirror or DjangoCodeMirror instance on a textarea
    Take the same arguments than ``forms.Textarea`` and accepts one suplementary
    optionnal arguments :

    Arguments:
        config_name (string): A Codemirror config name available in
            ``settings.CODEMIRROR_SETTINGS``. Default is ``empty``.
        embed_config (bool): If ``True`` will add Codemirror Javascript config
            just below the input. Default is ``False``.

    Attributes:
        config_name (string): For given config name.
    """
    codemirror_field_js = settings.CODEMIRROR_FIELD_INIT_JS

    def __init__(self, attrs=None, config_name='empty', embed_config=False, **kwargs):
        super(CodeMirrorWidget, self).__init__(attrs=attrs, **kwargs)
        self.config_name = config_name
        self.embed_config = embed_config

    def init_manifest(self):
        """
        Initialize a manifest instance

        Returns:
            CodeMirrorManifest: A manifest instance where config (from
            ``config_name`` attribute) is registred.
        """
        manifesto = CodeMirrorManifest()
        manifesto.register(self.config_name)
        return manifesto

    def get_codemirror_field_js(self):
        """
        Return CodeMirror HTML template string from
        ``CodeMirrorWidget.codemirror_field_js``.

        Returns:
            string: HTML template string.
        """
        return self.codemirror_field_js

    def build_codemirror_settings(self, final_attrs):
        """
        Build CodeMirror HTML for Javascript config

        Returns:
            string: HTML for field CodeMirror instance.
        """
        inputid = final_attrs['id']
        html = self.get_codemirror_field_js()
        opts = self.editor_manifest.get_codemirror_config(self.config_name)

        return html.format(inputid=inputid, settings=json.dumps(opts))

    def render(self, name, value, attrs=None):
        """
        Render widget HTML
        """
        if not hasattr(self, "editor_manifest"):
            self.editor_manifest = self.init_manifest()

        config = self.editor_manifest.get_config(self.config_name)

        final_attrs = self.build_attrs(attrs, name=name)

        # Widget allways need an id to be able to set CodeMirror Javascript config
        if 'id' not in final_attrs:
            final_attrs['id'] = 'id_{}'.format(name)

        html = [super(CodeMirrorWidget, self).render(name, value, attrs)]

        # Append HTML for CodeMirror Javascript config just below the textarea
        if self.embed_config or config.get('embed_config'):
            html.append(self.build_codemirror_settings(final_attrs))

        return mark_safe(u'\n'.join(html))

    @property
    def media(self):
        """
        Adds necessary files (Js/CSS) to the widget's medias
        """
        if not hasattr(self, "editor_manifest"):
            self.editor_manifest = self.init_manifest()

        return forms.Media(
            css={"all": self.editor_manifest.css()},
            js=self.editor_manifest.js()
        )


class CodeMirrorAdminWidget(CodeMirrorWidget):
    """
    CodeMirror widget suited for usage in models admins.

    Act like CodeMirrorWidget but allways embed Codemirror Javascript config.
    """
    def __init__(self, *args, **kwargs):
        kwargs['embed_config'] = True
        super(CodeMirrorAdminWidget, self).__init__(*args, **kwargs)
