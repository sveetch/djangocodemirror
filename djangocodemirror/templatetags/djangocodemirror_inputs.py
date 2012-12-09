# -*- coding: utf-8 -*-
"""
Parser template tags 
"""
import json

from django import template
from django.conf import settings
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

from djangocodemirror import settings_local

register = template.Library()

def djangocodemirror_input_settings(field):
    """
    Get the generated widget settings and return it as JSON
    """
    return mark_safe( json.dumps(field.field.widget._codemirror_final_settings_cache) )
djangocodemirror_input_settings.is_safe = True
register.filter(djangocodemirror_input_settings)

def djangocodemirror_init_input(field):
    """
    Return the HTML tag to embed the Javascript init for a djangocodemirror input field
    """
    html = settings_local.DJANGOCODEMIRROR_FIELD_INIT_JS
    settings = field.field.widget._codemirror_final_settings_cache
    return mark_safe( html.format(inputid=field.auto_id, settings=json.dumps(settings)) )
djangocodemirror_init_input.is_safe = True
register.filter(djangocodemirror_init_input)
