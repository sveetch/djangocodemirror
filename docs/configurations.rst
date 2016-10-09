.. _configurations-intro:

CodeMirror configurations
=========================

A CodeMirror configuration is a set of parameters for a CodeMirror instance.
Some of them are internal ones reserved to the manifest to control some
behaviors.

Every parameter in a configuration will be given to CodeMirror instance
excepted some internal ones:

themes
    List of theme names (from ``settings.CODEMIRROR_THEMES``) to load.
extra_css
    List of paths for extra CSS files to append after themes.
addons
    List of addons paths (relative to static directory) to load before modes.
modes
    List of mode names (from ``settings.CODEMIRROR_MODES``) to load.
    CodeMirror will assume to use the last loaded mode if you don't explicitely
    enable one using ``mode`` parameter.
css_bundle_name
    Bundle name for this configuration CSS assets, it will be used from
    :ref:`lib-assets-intro`. Automatically filled from configuration name if
    not defined.
js_bundle_name
    Bundle name for this configuration Javascript assets, it will be used from
    :ref:`lib-assets-intro`. Automatically filled from configuration name if
    not defined.

For available configuration parameters, see the
`CodeMirror documentation <http://codemirror.net/doc/manual.html#config>`_.

Create a new configuration
--------------------------

At the end of your settings (or just after default settings are loaded)
you could add:

.. sourcecode:: python

    CODEMIRROR_MODES.update({
        'css': {
            'modes': ['css'],
            'matchBrackets': True,
            'extraKeys': {"Ctrl-Space": "autocomplete"},
            'addons': [
                "CodeMirror/addon/edit/matchbrackets.js",
                "CodeMirror/addon/hint/show-hint.js",
                "CodeMirror/addon/hint/css-hint.js",
            ],
            'extra_css': [
                "CodeMirror/addon/hint/show-hint.css",
            ],
        },
    })

*This configuration is allready part of the default settings, copied here just
for sample*.

* This reproduces CodeMirror demo for ``css`` mode;
* You can see ``matchBrackets`` and ``extraKeys`` that are CodeMirror
  parameters, the other ones are internal parameters to define every required
  assets.
* ``modes`` define modes to load, here just ``css``;
* ``addons`` define useful CodeMirror addons to load. Addons may be required
  from some modes, some other ones are just for optional features;
* ``extra_css`` define some additional CSS stylesheets to load that are not
  themes. Here it's the ``show-hint`` addon CSS;

See ``djangocodemirror.settings`` file for more examples of configurations in
``CODEMIRROR_SETTINGS``.

If you plan to create a new configuration to use a mode that is not yet
implemented from default configurations, you should be aware how CodeMirror
and its modes work.
