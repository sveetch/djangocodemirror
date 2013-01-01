# -*- coding: utf-8 -*-
"""
DjangoCodeMirror template tags and filters for assets
"""
import json

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
    def __init__(self, *args):
        """
        :type page_var_name: string or object ``django.db.models.Model``
        :param page_var_name: Nom de variable de l'instance ou un string 
                                        pour le slug.
                                        
        :type template_path_varname: string
        :param template_path_varname: (optionnel) Chemin d'un template à utiliser pour 
                                      le rendu du menu à générer
                                        
        :type flat_mode: int
        :param flat_mode: (optionnel) Indique si on doit gérer un menu avec seulement les 
                          pages adjacentes (flat) à la page ciblée ou bien l'arborescence 
                          récursive de ses enfants (tree).
        """
        self.args = args
    
    def render(self, context):
        """
        Render the HTML
        
        :type context: object ``django.template.Context``
        :param context: Objet du contexte du tag.
        
        :rtype: string
        :return: Le rendu généré pour le tag capturé.
        """
        self.template_path = "djangocodemirror/include_field_assets.html"
        param_context = {
            'codemirror_only': False,
            'themes': [item[1] for item in settings_local.CODEMIRROR_THEMES],
            'search_enabled': False,
            'modes': [],
            'translations': settings_local.DJANGOCODEMIRROR_TRANSLATIONS,
            'csrf': False,
            'cookies_lib': False,
        }
        
        # Try to resolve all given arguments
        given_fields = []
        for item in self.args:
            fieldname = template.Variable(item)
            try:
                field = fieldname.resolve(context)
            except template.VariableDoesNotExist:
                # We should be explicit and throw an error ?
                pass
            else:
                given_fields.append(field)
        
        # If the first item is a string, assume that is a template path, pop it and 
        # use it
        if len(given_fields)>0 and isinstance(given_fields[0], basestring):
            self.template_path = given_fields.pop(0)
        
        # Update a global context for all fields, so we save only actived option, this 
        # will load all needed assets for all given fields
        for field in given_fields:
            field_widget = field.field.widget
            
            if field_widget.codemirror_only:
                param_context['codemirror_only'] = True
            if field_widget.opt_search_enabled:
                param_context['search_enabled'] = True
            if field_widget.opt_csrf_method_name:
                param_context['csrf_enabled'] = True
            
            # Agregate modes
            if field_widget.opt_mode_syntax:
                param_context['modes'].append(field_widget.opt_mode_syntax)
            
        context.update(param_context)
        html = template.loader.get_template(self.template_path).render(template.Context(context))
        
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
        return HtmlAssetsRender(*args[1:])

do_djangocodemirror_get_assets.is_safe = True

