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

class FieldAssetsMixin(object):
    """
    Base mixin
    """
    _default_app_settings = {
        'codemirror_only': False,
        'themes': [item[1] for item in settings_local.CODEMIRROR_THEMES],
        'search_enabled': False,
        'modes': [],
        'translations': settings_local.DJANGOCODEMIRROR_TRANSLATIONS,
        'csrf': False,
        'cookies_lib': False,
        'codemirror_settings_name': 'default',
        'css_bundle_name': settings_local.BUNDLES_CSS_NAME.format(settings_name='default'),
        'js_bundle_name': settings_local.BUNDLES_JS_NAME.format(settings_name='default'),
    }
    
    def get_app_settings(self, app_settings, widget_instance):
        """
        Return the right app settings (a dict) for the given widget instance
        """
        if getattr(widget_instance, 'add_jquery'):
            app_settings['add_jquery'] = widget_instance.add_jquery
        if widget_instance.codemirror_only:
            app_settings['codemirror_only'] = True
        if widget_instance.opt_search_enabled:
            app_settings['search_enabled'] = True
        if widget_instance.opt_csrf_method_name:
            app_settings['csrf_enabled'] = True
        # This one is not "cumulative", the last one is allways used, need another solution
        if hasattr(widget_instance, 'codemirror_settings_name'):
            app_settings['codemirror_settings_name'] = getattr(widget_instance, 'codemirror_settings_name')
            app_settings['css_bundle_name'] = settings_local.BUNDLES_CSS_NAME.format(settings_name=app_settings['codemirror_settings_name'])
            app_settings['js_bundle_name'] = settings_local.BUNDLES_JS_NAME.format(settings_name=app_settings['codemirror_settings_name'])
        
        # Agregate modes
        if widget_instance.opt_mode_syntax:
            app_settings['modes'].append(widget_instance.opt_mode_syntax)
        
        return app_settings
    
    def find_assets(self, app_settings, widget_instance):
        """
        Return the right app settings (a dict) for the given widget instance
        """
        css, js = {"all": []}, []
        
        js.append("CodeMirror/lib/codemirror.js")
            
        if app_settings.get('search_enabled'):
            js.append("CodeMirror/lib/util/dialog.js")
            js.append("CodeMirror/lib/util/search.js")
            js.append("CodeMirror/lib/util/searchcursor.js")
        
        for item in app_settings.get('modes', []):
            js.append(item)
        
        if app_settings.get('codemirror_only'):
            css['all'].append("CodeMirror/lib/codemirror.css")
        else:
            if app_settings.get('add_jquery'):
                js.append(app_settings['add_jquery'])
                
            css['all'].append("css/djangocodemirror.css")
            css['all'].append("js/qtip/jquery.qtip.min.css")
            
            js.append("js/jquery/jquery.cookies.2.2.0.min.js")
            js.append("djangocodemirror/djangocodemirror.translation.js")
            
            for item in app_settings.get('translations', []):
                js.append(item)

            js.append("djangocodemirror/buttons.js")
            js.append("djangocodemirror/syntax_methods.js")
            js.append("djangocodemirror/djangocodemirror.js")

            if app_settings.get('csrf_enabled'):
                js.append("djangocodemirror/csrf.js")

            js.append("js/qtip/jquery.qtip.min.js")
            js.append("djangocodemirror/qtip_console.js")
        
        for item in app_settings.get('themes', []):
            css['all'].append(item)
        
        return css, js

class HtmlAssetsRender(FieldAssetsMixin, template.Node):
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
        :return: Le rendu généré pour le tag capturé.
        """
        template_path = self.default_template
        given_fields = self.resolve_items(self.args, context)
        
        # If the first item is a string, assume that it is a template path, pop it and 
        # use it
        if len(given_fields)>0 and isinstance(given_fields[0], basestring):
            template_path = given_fields.pop(0)
        
        app_settings = copy.deepcopy(self._default_app_settings)
        
        # Update a global context for all fields, so we save only actived option, this 
        # will load all needed assets for all given fields
        for field in given_fields:
            field_widget = field.field.widget
            
            app_settings = self.get_app_settings(app_settings, field_widget)
            
        context.update(app_settings)
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

