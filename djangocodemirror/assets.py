"""
.. _django-assets: http://pypi.python.org/pypi/django-assets

.. _lib-assets-intro:

django-assets bundles
=====================

If `django-assets`_ is installed, module ``djangocodemirror.assets`` will be
automatically loaded to enable asset bundles for available configurations
``settings.CODEMIRROR_SETTINGS``.

Also a variable ``djangocodemirror.assets.DJANGO_ASSETS_INSTALLED`` will be set
to ``True`` if `django-assets`_ is installed, else ``False``.

Be aware that every configurations will be bundled, you may disable
configurations you don't use to avoid too much time on bundle compress.

Configuration bundle name
-------------------------

Default behavior is to automatically fill bundle names using configuration
name within a template string (either ``settings.CODEMIRROR_BUNDLE_CSS_NAME``
or ``settings.CODEMIRROR_BUNDLE_JS_NAME``).

Optionnally you can define a custom name for each of bundle kind (css or js).

If you want to disable bundles for a configuration simply set bundle names
to ``None`` in parameters:

    .. sourcecode:: python

        {
            ...
            'mode': 'foo',
            'css_bundle_name': None,
            'js_bundle_name': None,
            ...
        }
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

        if config.get('css_bundle_name'):
            css_options = copy.deepcopy(settings.BUNDLES_CSS_OPTIONS)
            if 'output' in css_options:
                css_options['output'] = css_options['output'].format(
                    settings_name=name
                )
            css_bundle = Bundle(*manifesto.css(name), **css_options)
            asset_register(config['css_bundle_name'], css_bundle)

        if config.get('js_bundle_name'):
            js_options = copy.deepcopy(settings.BUNDLES_JS_OPTIONS)
            if 'output' in js_options:
                js_options['output'] = js_options['output'].format(
                    settings_name=name
                )
            js_bundle = Bundle(*manifesto.js(name), **js_options)
            asset_register(config['js_bundle_name'], js_bundle)
