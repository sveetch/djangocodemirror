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
    from djangocodemirror.config import ConfigManager
    
    # Build all Bundles from available editor settings
    for settings_name,settings_values in settings_local.CODEMIRROR_SETTINGS.items():
        config = ConfigManager(config_name=settings_name)
        
        css_options = settings_local.BUNDLES_CSS_OPTIONS.copy()
        css_options['output'] = css_options['output'].format(settings_name=settings_name)
        js_options = settings_local.BUNDLES_JS_OPTIONS.copy()
        js_options['output'] = js_options['output'].format(settings_name=settings_name)
        
        css_contents, js_contents = config.find_assets()
        
        register(config.settings['css_bundle_name'], Bundle(*css_contents, **css_options))
        register(config.settings['js_bundle_name'], Bundle(*js_contents, **js_options))
