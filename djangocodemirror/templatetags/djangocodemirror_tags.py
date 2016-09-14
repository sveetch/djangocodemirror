# -*- coding: utf-8 -*-
"""
DjangoCodeMirror template tags and filters for assets

TODO: Tags for bundles.
"""
import copy
import json
import os

from django import template
from django.utils.safestring import mark_safe
from django.conf import settings

from djangocodemirror.manifest import CodeMirrorFieldBundle, CodeMirrorManifest


register = template.Library()


class CodemirrorAssetTagRender(CodeMirrorManifest):
    """
    A manifest extend to render Codemirror assets tags HTML.

    Arguments:
        initial (CodeMirrorManifest): Optional initial manifest.
    """
    def resolve_widget(self, field):
        """
        Given a Field or BoundField, return widget instance.

        Arguments:
            field (Field or BoundField): A field instance.

        Returns:
            django.forms.widgets.Widget: Retrieved widget from given field.
        """
        # When filter is used within template we have to reach the field instance
        # through the BoundField.
        if hasattr(field, 'field'):
            widget = field.field.widget
        # When used out of template, we have a direct field instance
        else:
            widget = field.widget

        return widget

    def register_from_fields(self, *args):
        """
        Register config name from field widgets

        Arguments:
            *args: Fields that contains widget
                ``djangocodemirror.widget.CodeMirrorWidget``.

        Returns:
            list: List of registered config names from fields.
        """
        names = []
        for field in args:
            widget = self.resolve_widget(field)
            self.register(widget.config_name)
            if widget.config_name not in names:
                names.append(widget.config_name)

        return names

    def render_asset_html(self, path, tag_template):
        """
        Render HTML tag for a given path.

        Arguments:
            path (string): Relative path from static directory.
            tag_template (string): Template string for HTML tag.

        Returns:
            string: HTML tag with url from given path.
        """
        url = os.path.join(settings.STATIC_URL, path)

        return tag_template.format(url=url)

    def css_html(self):
        """
        Render HTML tags for Javascript assets.

        Returns:
            string: HTML for CSS assets from every registered config.
        """
        output = []
        for item in self.css():
            output.append(
                self.render_asset_html(item, settings.CODEMIRROR_CSS_ASSET_TAG)
            )

        return '\n'.join(output)

    def js_html(self):
        """
        Render HTML tags for Javascript assets.

        Returns:
            string: HTML for Javascript assets from every registered config.
        """
        output = []
        for item in self.js():
            output.append(
                self.render_asset_html(item, settings.CODEMIRROR_JS_ASSET_TAG)
            )

        return '\n'.join(output)


@register.simple_tag
def codemirror_field_js_assets(*args):
    """
    Tag to render CodeMirror Javascript assets needed for all given fields.

    Example:

        {% load djangocodemirror_tags %}
        {% codemirror_field_js_assets form.myfield1 form.myfield2 %}
    """
    manifesto = CodemirrorAssetTagRender()
    manifesto.register_from_fields(*args)

    return manifesto.js_html()


@register.simple_tag
def codemirror_field_css_assets(*args):
    """
    Tag to render CodeMirror CSS assets needed for all given fields.

    Example:

        {% load djangocodemirror_tags %}
        {% codemirror_field_css_assets form.myfield1 form.myfield2 %}
    """
    manifesto = CodemirrorAssetTagRender()
    manifesto.register_from_fields(*args)

    return manifesto.css_html()


@register.filter
def codemirror_field_js_bundle(field):
    """
    Filter to get CodeMirror Javascript bundle name needed for a single field.

    Example:

        {% load djangocodemirror_tags %}
        {{ form.myfield|codemirror_field_js_bundle }}

    Arguments:
        field (djangocodemirror.fields.CodeMirrorField): A form field

    Raises:
        CodeMirrorFieldBundle: Raised if Codemirror configuration from field
        does not have a bundle name.

    Returns:
        string: Bundle name to load with webassets.
    """
    manifesto = CodemirrorAssetTagRender()
    manifesto.register_from_fields(field)

    try:
        bundle_name = manifesto.js_bundle_names()[0]
    except IndexError:
        raise CodeMirrorFieldBundle(("Given field with configuration name '{}' "
                                     "does not have a Javascript bundle "
                                     "name").format(name))

    return bundle_name


@register.filter
def codemirror_field_css_bundle(field):
    """
    Filter to get CodeMirror CSS bundle name needed for a single field.

    Example:

        {% load djangocodemirror_tags %}
        {{ form.myfield|codemirror_field_css_bundle }}

    Arguments:
        field (djangocodemirror.fields.CodeMirrorField): A form field

    Raises:
        CodeMirrorFieldBundle: Raised if Codemirror configuration from field
        does not have a bundle name.

    Returns:
        string: Bundle name to load with webassets.
    """
    manifesto = CodemirrorAssetTagRender()
    manifesto.register_from_fields(field)

    try:
        bundle_name = manifesto.css_bundle_names()[0]
    except IndexError:
        raise CodeMirrorFieldBundle(("Given field with configuration name '{}' "
                                     "does not have a CSS bundle "
                                     "name").format(name))

    return bundle_name


@register.filter
def codemirror_parameters(field):
    """
    Filter to include CodeMirror parameters as a JSON string for a single
    field.

    This must be called only on an allready rendered field, meaning you must
    not use this filter on a field before a form. Else, the field widget won't
    be correctly initialized.

    Example:

        {% load djangocodemirror_tags %}
        {{ form.myfield|codemirror_parameters }}

    Arguments:
        field (djangocodemirror.fields.CodeMirrorField): A form field

    Returns:
        string: JSON object for parameters, marked safe for Django templates.
    """
    manifesto = CodemirrorAssetTagRender()
    names = manifesto.register_from_fields(field)

    config = manifesto.get_codemirror_config(names[0])

    return mark_safe(json.dumps(config))

codemirror_parameters.is_safe = True
