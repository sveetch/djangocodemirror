# -*- coding: utf-8 -*-
"""
CodeMirror manifest
===================

Every assets paths should be relative path to your static directory. In fact it
depends how you will use them, but commonly it should be so.

"""
import copy, json

from django.conf import settings

class CodeMirrorManifest(object):
    """
    CodeMirror config and assets manifest

    Attributes:
        registry (dict): Configuration registry.
        default_internal_config (dict): Editor internal parameters, they
            won't be exposed in codemirror parameters until present in
            ``_internal_to_codemirror``.
        _internal_to_codemirror (dict): Name of internal parameters that will
            be passed into codemirror parameters.
    """
    # Default config base to extend for every registred config
    default_internal_config = {
        'mode': None, # Current mode, automatically added to 'modes'
        'modes': [], # Enabled modes
        'addons': [], # Addons filepaths to load
        'themes': [], # Themes filepaths to load
        'css_bundle_name': None, # CSS bundle name to fill
        'js_bundle_name': None, # Javascript bundle name to fill
    }

    _internal_to_codemirror = ['mode']

    def __init__(self):
        self.registry = {}

    def register(self, name):
        """
        Register configuration for an editor instance.

        Arguments:
            name (string): Config name from available ones in
                ``settings.CODEMIRROR_SETTINGS``.

        Returns:
            dict: Registred config dict.
        """
        parameters = copy.deepcopy(self.default_internal_config)
        parameters.update(copy.deepcopy(
            settings.CODEMIRROR_SETTINGS[name]
        ))

        # Add asset bundles name
        css_template_name = settings.CODEMIRROR_BUNDLES_CSS_NAME
        parameters['css_bundle_name'] = css_template_name.format(
            settings_name=name
        )
        js_template_name = settings.CODEMIRROR_BUNDLES_JS_NAME
        parameters['js_bundle_name']= js_template_name.format(
            settings_name=name
        )

        self.registry[name] = parameters

        return parameters

    def autoregister(self):
        """
        Register every configuration from ``settings.CODEMIRROR_SETTINGS``.
        """
        for name in settings.CODEMIRROR_SETTINGS:
            self.register(name)

    def resolve_mode(self, name):
        """
        From given mode name, return mode file path from
        ``settings.CODEMIRROR_MODES`` map.

        Raises:
            TODO: raise explicit error about unknowed mode name

        Returns:
            string: Mode file path.
        """
        return settings.CODEMIRROR_MODES.get(name)

    def resolve_theme(self, name):
        """
        From given theme name, return theme file path from
        ``settings.CODEMIRROR_THEMES`` map.

        Raises:
            TODO: raise explicit error about unknowed theme name

        Returns:
            string: Theme file path.
        """
        return settings.CODEMIRROR_THEMES.get(name)

    def get_config(self, name=None):
        """
        Returns configurations.

        * If ``name`` argument is not given, default behavior is to return
          every config from all registred config;
        * If ``name`` argument is given, just return its config and nothing
          else;

        Arguments:
            name (string): Specific configuration name to return.

        Returns:
            dict: Configurations.
        """
        if name:
            return {name: self.registry[name]}
        return self.registry

    def js(self, name=None):
        """
        Returns all needed Javascript filepaths for given config name (if
        given) or every registred config instead (if no name is given).

        Arguments:
            name (string): Specific config name to use instead of all.

        Returns:
            list: List of Javascript file paths.
        """
        filepaths = copy.copy(settings.CODEMIRROR_BASE_JS)

        configs = self.get_config(name)

        # Addons first
        for name,opts in configs.items():
            for item in opts.get('addons', []):
                # Uniqueness
                if item not in filepaths:
                    filepaths.append(item)

        # Then Modes
        for name,opts in configs.items():
            # 'mode' opts is for current mode, automatically add it to 'modes'
            # list
            if 'mode' in opts:
                if isinstance(opts['mode'], basestring):
                    opts['modes'] = [opts['mode']] + opts['modes']
            # Process modes
            for item in opts['modes']:
                # Uniqueness
                resolved = self.resolve_mode(item)
                if resolved not in filepaths:
                    filepaths.append(resolved)

        return filepaths

    def css(self, name=None):
        """
        Returns all needed CSS filepaths for given config name (if
        given) or every registred config instead (if no name is given).

        Arguments:
            name (string): Specific config name to use instead of all.

        Returns:
            list: List of CSS file paths.
        """
        filepaths = copy.copy(settings.CODEMIRROR_BASE_CSS)

        configs = self.get_config(name)

        # Process theme names
        for name,opts in configs.items():
            for item in opts.get('themes', []):
                # Uniqueness
                resolved = self.resolve_theme(item)
                if resolved not in filepaths:
                    filepaths.append(resolved)

        return filepaths

    def get_codemirror_config(self, name, json=False):
        """
        Return CodeMirror configuration for given config name.

        Arguments:
            name (string): Config name from available ones in
                ``settings.CODEMIRROR_SETTINGS``.

        Keyword Arguments:
            json (bool): If ``True`` will return config as a JSON string,
                default is ``False``.

        Returns:
            dict or string: Configuration as a Python dict or a JSON string
            depending on ``json`` argument.
        """
        return []
