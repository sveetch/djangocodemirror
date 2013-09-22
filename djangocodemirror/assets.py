"""
Compute some Bundles for webassets/django-assets

A bundle is computed for each avalaible settings item in 
"settings.CODEMIRROR_SETTINGS".

In the template you will have to load the bundle accordly to your field settings, there 
is a templatetag and an include template to do this automatically from your form field,
see the doc.
"""
try:
    from django_assets import Bundle, register
except ImportError:
    DJANGO_ASSETS_INSTALLED = False
else:
    DJANGO_ASSETS_INSTALLED = True

if DJANGO_ASSETS_INSTALLED:
    from djangocodemirror import settings_local
    #from djangocodemirror.templatetags.djangocodemirror_assets import FieldAssetsMixin
    
    #class DummyWidget(object):
        #"""
        #Dummy to fake a form widget instance
        #"""
        #codemirror_only = False
        #themes = False
        #opt_search_enabled = False
        #mode = False
        #csrf = False
        #translations = False

    #def agregate_bundles_contents(opts, themes=[], translations=[]):
        #"""
        #Agregate all needed assets files
        #"""
        #widget = DummyWidget()
        #widget.codemirror_only = opts.get('codemirror_only')
        #widget.opt_search_enabled = opts.get('search_enabled')
        #widget.opt_mode_syntax = opts.get('mode')
        #widget.opt_csrf_method_name = opts.get('csrf')
        #widget.themes = themes
        #widget.translations = translations
        ## Find assets
        #mix = FieldAssetsMixin()
        #opts = mix.get_app_settings(opts, widget)
        #css, js = mix.find_assets(opts, widget)
        
        #return css, js
    
    ## Build all Bundles from available editor settings
    #for settings_name,settings_values in settings_local.CODEMIRROR_SETTINGS.items():
        #css_name = settings_local.BUNDLES_CSS_NAME.format(settings_name=settings_name)
        #js_name = settings_local.BUNDLES_JS_NAME.format(settings_name=settings_name)
        
        #css_options = settings_local.BUNDLES_CSS_OPTIONS.copy()
        #css_options['output'] = css_options['output'].format(settings_name=settings_name)
        #js_options = settings_local.BUNDLES_JS_OPTIONS.copy()
        #js_options['output'] = js_options['output'].format(settings_name=settings_name)
        
        #css_contents, js_contents = agregate_bundles_contents(settings_values, themes=settings_local.CODEMIRROR_THEMES, translations=settings_local.DJANGOCODEMIRROR_TRANSLATIONS)
        
        #register(css_name, Bundle(*css_contents, **css_options))
        #register(js_name, Bundle(*js_contents, **js_options))
