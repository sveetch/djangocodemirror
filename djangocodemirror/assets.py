"""
Compute some Bundles for webassets/django-assets

A bundle is computed for each avalaible settings item in 
"settings.CODEMIRROR_SETTINGS".

In the template you will have to load the bundle accordly to your field settings, there 
is a templatetag and an include template to do this automatically from your form field.
"""
from django_assets import Bundle, register

from djangocodemirror import settings_local

def agregate_bundles_contents(opts, themes=[], translations=[]):
    """
    Agregate all needed assets files
    """
    css = []
    js = []
    
    if not opts.get('codemirror_only'):
        css.append("css/djangocodemirror.css")
    else:
        css.append("CodeMirror/lib/codemirror.css")

    css.append("js/qtip/jquery.qtip.min.css")

    for k,v in themes:
        css.append(v)

    js.append("CodeMirror/lib/codemirror.js")
    if opts.get('search_enabled'):
        js.append("CodeMirror/lib/util/dialog.js")
        js.append("CodeMirror/lib/util/search.js")
        js.append("CodeMirror/lib/util/searchcursor.js")

    if opts.get('mode'):
        js.append(dict(settings_local.CODEMIRROR_MODES)[opts.get('mode')])

    if not opts.get('codemirror_only'):
        js.append("js/jquery/jquery.cookies.2.2.0.js") # TODO: This should be optional, as 
                                                       # some other things like Foundation embed it
        js.append("djangocodemirror/djangocodemirror.translation.js")
        for item in translations:
            js.append(item)

        js.append("djangocodemirror/buttons.js")
        js.append("djangocodemirror/syntax_methods.js")
        js.append("djangocodemirror/djangocodemirror.js")

        if opts.get('csrf'):
            js.append("djangocodemirror/csrf.js")

        js.append("js/qtip/jquery.qtip.js")
        js.append("djangocodemirror/qtip_console.js")
    
    #print css
    #print js
    #print
    return css, js

# Build all Bundles from available editor settings
for settings_name,settings_values in settings_local.CODEMIRROR_SETTINGS.items():
    #print settings_name
    css_name = settings_local.BUNDLES_CSS_NAME.format(settings_name=settings_name)
    js_name = settings_local.BUNDLES_JS_NAME.format(settings_name=settings_name)
    
    css_options = settings_local.BUNDLES_CSS_OPTIONS.copy()
    css_options['output'] = css_options['output'].format(settings_name=settings_name)
    js_options = settings_local.BUNDLES_JS_OPTIONS.copy()
    js_options['output'] = js_options['output'].format(settings_name=settings_name)
    
    css_contents, js_contents = agregate_bundles_contents(settings_values, themes=settings_local.CODEMIRROR_THEMES, translations=settings_local.DJANGOCODEMIRROR_TRANSLATIONS)
    
    register(css_name, Bundle(*css_contents, **css_options))
    register(js_name, Bundle(*js_contents, **js_options))
