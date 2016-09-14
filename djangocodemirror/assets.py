"""
Webassets bundles
=================

Compute some Bundles for ``webassets`` + ``django-assets``.

Bundles are computed from each avalaible settings item in
"settings.CODEMIRROR_SETTINGS".
"""
try:
    from django_assets import Bundle
    from django_assets import register as asset_register
except ImportError:
    DJANGO_ASSETS_INSTALLED = False
else:
    import copy

    DJANGO_ASSETS_INSTALLED = True

    from django.conf import settings
    from djangocodemirror.manifest import CodeMirrorManifest

    for name, opts in settings.CODEMIRROR_SETTINGS.items():
        manifesto = CodeMirrorManifest()

        manifesto.register(name)
        config = manifesto.registry[name]

        css_options = copy.deepcopy(settings.BUNDLES_CSS_OPTIONS)
        if 'output' in css_options:
            css_options['output'] = css_options['output'].format(
                settings_name=name
            )

        js_options = copy.deepcopy(settings.BUNDLES_JS_OPTIONS)
        if 'output' in js_options:
            js_options['output'] = js_options['output'].format(
                settings_name=name
            )

        css_bundle = Bundle(*manifesto.css(name), **css_options)
        js_bundle = Bundle(*manifesto.js(name), **js_options)

        asset_register(config.settings['css_bundle_name'], css_bundle)
        asset_register(config.settings['js_bundle_name'], js_bundle)
