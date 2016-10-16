# -*- coding: utf-8 -*-
"""
Form field widget
=================

"""
import json

from django import forms

from django.conf import settings
from django.utils.safestring import mark_safe

from djangocodemirror.manifest import CodeMirrorManifest


class CodeMirrorWidget(forms.Textarea):
    """
    Widget to add a CodeMirror or DjangoCodeMirror instance on a textarea
    Take the same arguments than ``forms.Textarea`` and accepts one
    suplementary optionnal arguments :

    Arguments:
        config_name (string): A Codemirror config name available in
            ``settings.CODEMIRROR_SETTINGS``. Default is ``empty``.
        embed_config (bool): If ``True`` will add Codemirror Javascript config
            just below the input. Default is ``False``.

    Attributes:
        config_name (string): For given config name.
    """
    codemirror_field_js = settings.CODEMIRROR_FIELD_INIT_JS

    def __init__(self, *args, **kwargs):
        self.config_name = kwargs.pop('config_name', 'empty')
        self.embed_config = kwargs.pop('embed_config', False)

        super(CodeMirrorWidget, self).__init__(*args, **kwargs)

    def init_manifest(self, name):
        """
        Initialize a manifest instance

        Arguments:
            name (string): Config name to register.

        Returns:
            CodeMirrorManifest: A manifest instance where config (from
            ``config_name`` attribute) is registred.
        """
        manifesto = CodeMirrorManifest()
        manifesto.register(name)
        return manifesto

    def get_codemirror_field_js(self):
        """
        Return CodeMirror HTML template from
        ``CodeMirrorWidget.codemirror_field_js``.

        Returns:
            string: HTML template string.
        """
        return self.codemirror_field_js

    def codemirror_config(self):
        """
        Shortcut to get Codemirror parameters.

        Returns:
            dict: CodeMirror parameters.
        """
        return self.editor_manifest.get_codemirror_parameters(self.config_name)

    def codemirror_script(self, final_attrs):
        """
        Build CodeMirror HTML script tag which contains CodeMirror init.

        Arguments:
            final_attrs (dict): Widget attributes that must contains the ``id``
                attribute.

        Returns:
            string: HTML for field CodeMirror instance.
        """
        inputid = final_attrs['id']
        varname = "{}_codemirror".format(inputid)
        html = self.get_codemirror_field_js()
        opts = self.codemirror_config()

        return html.format(varname=varname, inputid=inputid,
                           settings=json.dumps(opts, sort_keys=True))

    def render(self, name, value, attrs=None):
        """
        Render widget HTML

        Arguments:
            name (string): Field input name.
            value (string): Field input value.

        Keyword Arguments:
            attrs (dict): Optional field widget attributes. Default to
                ``None``.

        Returns:
            string: Widget HTML representation.
        """
        if not hasattr(self, "editor_manifest"):
            self.editor_manifest = self.init_manifest(self.config_name)

        config = self.editor_manifest.get_config(self.config_name)

        final_attrs = self.build_attrs(attrs, name=name)

        # Widget allways need an id to be able to set CodeMirror Javascript
        # config
        if 'id' not in final_attrs:
            final_attrs['id'] = 'id_{}'.format(name)

        html = [super(CodeMirrorWidget, self).render(name, value, attrs)]

        # Append HTML for CodeMirror Javascript config just below the textarea
        if self.embed_config or config.get('embed_config'):
            html.append(self.codemirror_script(final_attrs))

        return mark_safe(u'\n'.join(html))

    @property
    def media(self):
        """
        Adds necessary files (Js/CSS) to the widget's medias.

        Returns:
            django.forms.Media: Media object with all assets from registered
            config.
        """
        if not hasattr(self, "editor_manifest"):
            self.editor_manifest = self.init_manifest(self.config_name)

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
