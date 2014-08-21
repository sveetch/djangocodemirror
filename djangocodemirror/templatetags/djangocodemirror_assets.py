# -*- coding: utf-8 -*-
"""
DjangoCodeMirror template tags and filters for assets
"""
import copy, json

from django import template
from django.conf import settings
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

from djangocodemirror import settings_local

register = template.Library()

class HtmlAssetsRender(template.Node):
    """
    Generate HTML of the node *HtmlMediaRender*
    """
    def __init__(self, default_template, *args):
        """
        :type default_template: string
        :param default_template: Default template name to use if not given in the tag args
        """
        self.args = args
        self.default_template = default_template
    
    def resolve_items(self, args, context):
        # Try to resolve all given arguments
        given_fields = []
        for item in args:
            fieldname = template.Variable(item)
            try:
                field = fieldname.resolve(context)
            except template.VariableDoesNotExist:
                # We should be explicit and throw an error ?
                pass
            else:
                given_fields.append(field)
        
        return given_fields
    
    def render(self, context):
        """
        Render the HTML
        
        :type context: object ``django.template.Context``
        :param context: Objet du contexte du tag.
        
        :rtype: string
        :return: Generated HTML to load needed assets (CSS, JS)
        
        TODO: 'mode' setting will not be accumulated, so for multiple fields with 
              different mode, only one will have its right mode.
              We should go for another solution wich merge assets list.
        """
        template_path = self.default_template
        given_fields = self.resolve_items(self.args, context)
        
        # If the first item is a string, assume that it is a template path, pop it and 
        # use it
        if len(given_fields)>0 and isinstance(given_fields[0], basestring):
            template_path = given_fields.pop(0)
        
        first_field = given_fields.pop(0)
        
        # We need to trigger Widget's media attribute to have the 'editor_config_manager' attribute
        first_field.field.widget.media
        
        app_settings = first_field.field.widget.editor_config_manager.editor_config
        
        css, js = first_field.field.widget.editor_config_manager.find_assets()
        # Update a global context for all fields, so we save only actived option, this 
        # will load all needed assets for all given fields
        for field in given_fields:
            field_widget = field.field.widget
            
            app_settings = self.editor_config_manager.editor_config
            app_settings.update(self.editor_config_manager.editor_config)
            css_sup, js_sup = first_field.field.widget.editor_config_manager.find_assets()
            css = css + css_sup
            js = js + js_sup
            
        context.update({
            'djangocodemirror_css': css,
            'djangocodemirror_js': js,
            'css_bundle_name': first_field.field.widget.editor_config_manager.settings['css_bundle_name'],
            'js_bundle_name': first_field.field.widget.editor_config_manager.settings['js_bundle_name'],
        })
        html = template.loader.get_template(template_path).render(template.Context(context))
        
        return mark_safe(html)

@register.tag(name="djangocodemirror_get_assets")
def do_djangocodemirror_get_assets(parser, token):
    """
    Return the html to load all needed assets for all given djangocodemirror fields
    
    This can only be used on a field that have allready been rendered.
    
    Usage : ::
    
        {% load djangocodemirror_assets %}
        
        <html>
            <head>
            ...
            {% djangocodemirror_get_assets form.myfield1 form.myfield2 %}
            </head>
        ...
        </html>
        
    Warning, the tag does not throw explicit template errors for invalid fields.
        
    :type parser: object ``django.template.Parser``
    :param parser: Objet du parser de template.
    
    :type token: object ``django.template.Token``
    :param token: Objet de la chaîne découpée du tag capturé dans le template.
    
    :rtype: object ``PageMenuTagRender``
    :return: L'objet du générateur de rendu du tag.
    """
    args = token.split_contents()
    if len(args) < 2:
        raise template.TemplateSyntaxError, "You need to specify at less one form field"
    else:
        return HtmlAssetsRender("djangocodemirror/include_field_assets.html", *args[1:])

do_djangocodemirror_get_assets.is_safe = True


@register.tag(name="djangocodemirror_get_bundles")
def do_djangocodemirror_get_bundles(parser, token):
    """
    It works exactly like the "djangocodemirror_get_assets" except it use django-assets 
    bundles in place of direct assets. You should not use this if you don't have 'django-assets' 
    installed.
    """
    args = token.split_contents()
    if len(args) < 2:
        raise template.TemplateSyntaxError, "You need to specify at less one form field"
    else:
        return HtmlAssetsRender("djangocodemirror/include_field_bundles.html", *args[1:])

do_djangocodemirror_get_bundles.is_safe = True
