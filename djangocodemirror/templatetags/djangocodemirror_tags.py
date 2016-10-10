# -*- coding: utf-8 -*-
"""
Template tags
=============

"""
import io
import json
import os

from django import template
from django.utils.safestring import mark_safe
from django.conf import settings

from djangocodemirror.manifest import CodeMirrorManifest
from djangocodemirror.exceptions import CodeMirrorFieldBundleError


register = template.Library()


class CodemirrorAssetTagRender(CodeMirrorManifest):
    """
    A manifest extend to render Codemirror assets tags HTML.
    """
    def resolve_widget(self, field):
        """
        Given a Field or BoundField, return widget instance.

        Todo:
            Raise an exception if given field object does not have a
            widget.

        Arguments:
            field (Field or BoundField): A field instance.

        Returns:
            django.forms.widgets.Widget: Retrieved widget from given field.
        """
        # When filter is used within template we have to reach the field
        # instance through the BoundField.
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
                :class:`djangocodemirror.widget.CodeMirrorWidget`.

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
        output = io.StringIO()

        for item in self.css():
            output.write(
                self.render_asset_html(item, settings.CODEMIRROR_CSS_ASSET_TAG)
            )

        content = output.getvalue()
        output.close()

        return content

    def js_html(self):
        """
        Render HTML tags for Javascript assets.

        Returns:
            string: HTML for Javascript assets from every registered config.
        """
        output = io.StringIO()

        for item in self.js():
            output.write(
                self.render_asset_html(item, settings.CODEMIRROR_JS_ASSET_TAG)
            )

        content = output.getvalue()
        output.close()

        return content

    def codemirror_html(self, config_name, varname, element_id):
        """
        Render HTML for a CodeMirror instance.

        Since a CodeMirror instance have to be attached to a HTML element, this
        method requires a HTML element identifier with or without the ``#``
        prefix, it depends from template in
        ``settings.CODEMIRROR_FIELD_INIT_JS`` (default one require to not
        prefix with ``#``).

        Arguments:
            config_name (string): A registred config name.
            varname (string): A Javascript variable name.
            element_id (string): An HTML element identifier (without
                leading ``#``) to attach to a CodeMirror instance.

        Returns:
            string: HTML to instanciate CodeMirror for a field input.
        """
        parameters = json.dumps(self.get_codemirror_parameters(config_name),
                                sort_keys=True)
        return settings.CODEMIRROR_FIELD_INIT_JS.format(
            varname=varname,
            inputid=element_id,
            settings=parameters,
        )


@register.simple_tag
def codemirror_field_js_assets(*args):
    """
    Tag to render CodeMirror Javascript assets needed for all given fields.

    Example:
        ::

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
        ::

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
        ::

        {% load djangocodemirror_tags %}
        {{ form.myfield|codemirror_field_js_bundle }}

    Arguments:
        field (django.forms.fields.Field): A form field that contains a widget
            :class:`djangocodemirror.widget.CodeMirrorWidget`.

    Raises:
        CodeMirrorFieldBundleError: If Codemirror configuration form field
        does not have a bundle name.

    Returns:
        string: Bundle name to load with webassets.
    """
    manifesto = CodemirrorAssetTagRender()
    manifesto.register_from_fields(field)

    try:
        bundle_name = manifesto.js_bundle_names()[0]
    except IndexError:
        msg = ("Given field with configuration name '{}' does not have a "
               "Javascript bundle name")
        raise CodeMirrorFieldBundleError(msg.format(field.config_name))

    return bundle_name


@register.filter
def codemirror_field_css_bundle(field):
    """
    Filter to get CodeMirror CSS bundle name needed for a single field.

    Example:
        ::

        {% load djangocodemirror_tags %}
        {{ form.myfield|codemirror_field_css_bundle }}

    Arguments:
        field (djangocodemirror.fields.CodeMirrorField): A form field.

    Raises:
        CodeMirrorFieldBundleError: Raised if Codemirror configuration from
        field does not have a bundle name.

    Returns:
        string: Bundle name to load with webassets.
    """
    manifesto = CodemirrorAssetTagRender()
    manifesto.register_from_fields(field)

    try:
        bundle_name = manifesto.css_bundle_names()[0]
    except IndexError:
        msg = ("Given field with configuration name '{}' does not have a "
               "Javascript bundle name")
        raise CodeMirrorFieldBundleError(msg.format(field.config_name))

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
        ::

            {% load djangocodemirror_tags %}
            {{ form.myfield|codemirror_parameters }}

    Arguments:
        field (djangocodemirror.fields.CodeMirrorField): A form field.

    Returns:
        string: JSON object for parameters, marked safe for Django templates.
    """
    manifesto = CodemirrorAssetTagRender()
    names = manifesto.register_from_fields(field)

    config = manifesto.get_codemirror_parameters(names[0])

    return mark_safe(json.dumps(config))

codemirror_parameters.is_safe = True


@register.simple_tag
def codemirror_instance(config_name, varname, element_id, assets=True):
    """
    Return HTML to init a CodeMirror instance for an element.

    This will output the whole HTML needed to initialize a CodeMirror instance
    with needed assets loading. Assets can be omitted with the ``assets``
    option.

    Example:
        ::

            {% load djangocodemirror_tags %}
            {% codemirror_instance 'a-config-name' 'foo_codemirror' 'foo' %}

    Arguments:
        config_name (string): A registred config name.
        varname (string): A Javascript variable name.
        element_id (string): An HTML element identifier (without
            leading ``#``) to attach to a CodeMirror instance.

    Keyword Arguments:
        assets (Bool): Adds needed assets before the HTML if ``True``, else
            only CodeMirror instance will be outputed. Default value is
            ``True``.

    Returns:
        string: HTML.
    """
    output = io.StringIO()

    manifesto = CodemirrorAssetTagRender()
    manifesto.register(config_name)

    if assets:
        output.write(manifesto.css_html())
        output.write(manifesto.js_html())

    html = manifesto.codemirror_html(config_name, varname, element_id)
    output.write(html)

    content = output.getvalue()
    output.close()

    return mark_safe(content)
