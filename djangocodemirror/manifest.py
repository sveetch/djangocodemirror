# -*- coding: utf-8 -*-
"""
CodeMirror manifest
===================

From its registred Codemirror configs, manifest is able to:

* Return needed js files, either for all registred configs or a single one;
* Return needed css files, either for all registred configs or a single one;
* Return Codemirror configuration options as a dict for a registred config;

A Codemirror config is selected from its name in
``settings.CODEMIRROR_SETTINGS``.
"""
import copy

from django.conf import settings


class NotRegistered(KeyError):
    pass


class UnknowConfig(KeyError):
    pass


class UnknowMode(KeyError):
    pass


class UnknowTheme(KeyError):
    pass


class CodeMirrorFieldBundle(KeyError):
    pass


class CodeMirrorManifest(object):
    """
    CodeMirror configurations and assets manifest.

    A configuration contains every parameters and assets to use with a
    CodeMirror instance.

    Attributes:
        registry (dict): Configuration registry.
        default_internal_config (dict): Default internal parameters.
        _internal_only (list): Names of internal parameters only that will be
            exluded from CodeMirror parameters.
    """
    default_internal_config = {
        'modes': [], # Enabled modes
        'addons': [], # Addons filepaths to load
        'themes': [], # Themes filepaths to load
        'css_bundle_name': None, # CSS bundle name to fill
        'js_bundle_name': None, # Javascript bundle name to fill
    }

    _internal_only = ['modes', 'addons', 'themes', 'css_bundle_name',
                      'js_bundle_name']

    def __init__(self):
        self.registry = {}

    def register(self, name):
        """
        Register configuration for an editor instance.

        Arguments:
            name (string): Config name from available ones in
                ``settings.CODEMIRROR_SETTINGS``.

        Raises:
            UnknowConfig: If given config name does not exist in
                ``settings.CODEMIRROR_SETTINGS``.

        Returns:
            dict: Registred config dict.
        """
        if name not in settings.CODEMIRROR_SETTINGS:
            raise UnknowConfig(("Given config name '{}' does not exists in "
                                 "'settings.CODEMIRROR_SETTINGS'.").format(
                                     name
                                ))

        parameters = copy.deepcopy(self.default_internal_config)
        parameters.update(copy.deepcopy(
            settings.CODEMIRROR_SETTINGS[name]
        ))

        # Add asset bundles name
        css_template_name = settings.CODEMIRROR_BUNDLE_CSS_NAME
        parameters['css_bundle_name'] = css_template_name.format(
            settings_name=name
        )
        js_template_name = settings.CODEMIRROR_BUNDLE_JS_NAME
        parameters['js_bundle_name']= js_template_name.format(
            settings_name=name
        )

        self.registry[name] = parameters

        return parameters

    def register_many(self, *args):
        """
        Register many configuration names.

        Arguments:
            *args: Config names as strings.

        Returns:
            list: List of registered configs.
        """
        params = []
        for name in args:
            params.append(self.register(name))

        return params

    def autoregister(self):
        """
        Register every available configuration from
        ``settings.CODEMIRROR_SETTINGS``.
        """
        for name in settings.CODEMIRROR_SETTINGS:
            self.register(name)

    def resolve_mode(self, name):
        """
        From given mode name, return mode file path from
        ``settings.CODEMIRROR_MODES`` map.

        Arguments:
            name (string): Mode name.

        Raises:
            KeyError: When given name does not exist in
                ``settings.CODEMIRROR_MODES``.

        Returns:
            string: Mode file path.
        """
        if name not in settings.CODEMIRROR_MODES:
            raise UnknowMode(("Given config name '{}' does not exists in "
                              "'settings.CODEMIRROR_MODES'.").format(name))

        return settings.CODEMIRROR_MODES.get(name)

    def resolve_theme(self, name):
        """
        From given theme name, return theme file path from
        ``settings.CODEMIRROR_THEMES`` map.

        Arguments:
            name (string): Theme name.

        Raises:
            KeyError: When given name does not exist in
                ``settings.CODEMIRROR_THEMES``.

        Returns:
            string: Theme file path.
        """
        if name not in settings.CODEMIRROR_THEMES:
            raise UnknowTheme(("Given theme name '{}' does not exists in "
                               "'settings.CODEMIRROR_THEMES'.").format(name))

        return settings.CODEMIRROR_THEMES.get(name)

    def get_configs(self, name=None):
        """
        Returns registred configurations.

        * If ``name`` argument is not given, default behavior is to return
          every config from all registred config;
        * If ``name`` argument is given, just return its config and nothing
          else;

        Arguments:
            name (string): Specific configuration name to return.

        Raises:
            NotRegistered: If given config name does not exist in registry.

        Returns:
            dict: Configurations.
        """
        if name:
            if name not in self.registry:
                raise NotRegistered(("Given config name '{}' "
                                    "is not registered.").format(name))

            return {name: self.registry[name]}
        return self.registry

    def get_config(self, name):
        """
        Return a registred configuration for given config name.

        Arguments:
            name (string): A registred config name.

        Raises:
            NotRegistered: If given config name does not exist in registry.

        Returns:
            dict: Configuration.
        """
        if name not in self.registry:
            raise NotRegistered(("Given config name '{}' "
                                 "is not registered.").format(name))

        return copy.deepcopy(self.registry[name])

    def get_codemirror_parameters(self, name):
        """
        Return CodeMirror parameters for given configuration name.

        This is a reduced configuration from internal parameters.

        Arguments:
            name (string): Config name from available ones in
                ``settings.CODEMIRROR_SETTINGS``.

        Returns:
            dict: Parameters.
        """
        config = self.get_config(name)

        for k,v in config.items():
            if k in self._internal_only:
                del config[k]

        return config

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

        configs = self.get_configs(name)

        # Addons first
        for name,opts in configs.items():
            for item in opts.get('addons', []):
                if item not in filepaths:
                    filepaths.append(item)

        # Process modes
        for name,opts in configs.items():
            for item in opts['modes']:
                resolved = self.resolve_mode(item)
                if resolved not in filepaths:
                    filepaths.append(resolved)

        return filepaths

    def js_bundle_names(self, name=None):
        """
        Returns all needed Javascript Bundle names for given config name (if
        given) or every registred config instead (if no name is given).

        Arguments:
            name (string): Specific config name to use instead of all.

        Returns:
            list: List of webasset bundle names.
        """
        configs = self.get_configs(name)

        # Addons first
        return sorted([opts['js_bundle_name'] for name, opts in configs.items()
                if 'js_bundle_name' in opts])

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

        configs = self.get_configs(name)

        # Process theme names
        for name,opts in configs.items():
            for item in opts.get('themes', []):
                resolved = self.resolve_theme(item)
                if resolved not in filepaths:
                    filepaths.append(resolved)

        return filepaths

    def css_bundle_names(self, name=None):
        """
        Returns all needed CSS Bundle names for given config name (if
        given) or every registred config instead (if no name is given).

        Arguments:
            name (string): Specific config name to use instead of all.

        Returns:
            list: List of webasset bundle names.
        """
        configs = self.get_configs(name)

        # Addons first
        return sorted([opts['css_bundle_name'] for name, opts in configs.items()
                if 'css_bundle_name' in opts])
