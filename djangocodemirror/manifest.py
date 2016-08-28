# -*- coding: utf-8 -*-
"""
DjangoCodeMirror config object
"""
import copy, json

from django.conf import settings

class CodeMirrorManifest(object):
    """
    CodeMirror config and assets manifest

    Attributes:
        default_internal_config (dict): Editor internal parameters, they
            won't be exposed in codemirror parameters until present in
            ``_internal_to_codemirror``.
        _internal_to_codemirror (dict): Name of internal parameters that will
            be passed into codemirror parameters.
    """
    js = []
    css = []

    registry = {}

    default_internal_config = {
        'mode': None,
        'modes': [],
        'addons': [],
        'themes': [item[1] for item in settings.CODEMIRROR_THEMES],
        'css_bundle_name': settings.BUNDLES_CSS_NAME.format(settings_name='default'),
        'js_bundle_name': settings.BUNDLES_JS_NAME.format(settings_name='default'),
    }

    _internal_to_codemirror = ['mode']

    def __init__(self):
        pass

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

        self.registry[name] = parameters

        return parameters

    def autoregister(self):
        """
        Register every configuration from ``settings.CODEMIRROR_SETTINGS``.
        """
        for name in settings.CODEMIRROR_SETTINGS:
            self.register(name)

    def get_codemirror_config(self, name):
        """
        Return CodeMirror configuration for given config name.

        Arguments:
            name (string): Config name from available ones in
                ``settings.CODEMIRROR_SETTINGS``.
        """
        return []

    def resolve_mode(self, name):
        """
        From given mode name, return mode file path from
        ``settings.CODEMIRROR_MODES`` map.
        """
        return dict(settings.CODEMIRROR_MODES).get(name)

    def js(self, name=None):
        """
        Returns all needed Javascript filepaths for given config name or every registred config.

        If ``name`` argument is not given, default behavior is to make a
        complete pack of every ressources for all registred config.

        TODO: Have to be a read only Class attribute

        Arguments:
            name (string): Specific config name to use instead of all.

        Returns:
            list: List of Javascript file paths.
        """
        filepaths = ["CodeMirror/lib/codemirror.js"]

        if name:
            configs = {name: self.registry[name]}
        else:
            configs = self.registry

        # Addons first
        for name,opts in configs.items():
            if opts.get('addons', None):
                for item in opts['addons']:
                    # Uniqueness
                    if item not in filepaths:
                        filepaths.append(item)

        # Then Modes
        for name,opts in configs.items():
            # 'mode' opts is for current mode, add it to 'modes' list if not
            # allready in
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

    def css(self):
        """
        Returns all needed CSS filepaths for every registred config.

        Have to be Class attribute

        Arguments:
            name (string): Config name from available ones in
                ``settings.CODEMIRROR_SETTINGS``.
        """
        return []
