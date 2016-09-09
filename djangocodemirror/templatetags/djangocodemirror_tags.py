# -*- coding: utf-8 -*-
"""
DjangoCodeMirror template tags and filters for assets
"""
import copy, json

from django import template
from django.utils.safestring import mark_safe
from django.conf import settings

from djangocodemirror.manifest import CodeMirrorManifest

register = template.Library()


@register.simple_tag
def toast(*args):
    """
    Toast simple_tag
    """
    output = '<ul>\n'
    for name in args:
        output += '<li>{}</li>'.format(name)
    output += '</ul>'
    return output


def resolve_widget(field):
    """
    Given a Field or BoundField, return widget instance.

    Todo:
        Should be able to figure if instance value is a string which will be
        assumed to be a config name ?
    """
    # When filter is used within template we have to reach the field instance
    # through the BoundField.
    if hasattr(field, 'field'):
        widget = field.field.widget
    # When used out of template, we have a direct field instance
    else:
        widget = field.widget

    return widget


@register.simple_tag
def codemirror_field_js_assets(*args):
    """
    Tag to render CodeMirror Javascript assets needed for all given fields.

    Example:

        {% load djangocodemirror_tags %}
        {% codemirror_field_js_assets form.myfield1 form.myfield2 %}
    """
    output = []

    manifesto = CodeMirrorManifest()
    for field in args:
        widget = resolve_widget(field)
        manifesto.register(widget.config_name)

    for item in manifesto.css():
        output.append(settings.CODEMIRROR_CSS_ASSET_TAG.format(url=item))

    return '\n'.join(output)


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
    widget = resolve_widget(field)

    # Get Codemirror config from widget
    config = widget.codemirror_config()

    return mark_safe(json.dumps(config))

codemirror_parameters.is_safe = True
