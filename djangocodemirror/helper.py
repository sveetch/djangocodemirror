"""

.. _helper-intro:

Configuration helper
====================

Usually you will want to just use included configurations from default settings
and just add some parameters on them.

``codemirror_settings_update`` function will help you to easily apply these
parameters on many configuration in a single act.

Obviously, this is something to use from your settings.

Examples:

    Sample usage to apply some parameters only every configuration from default
    settings:

    .. sourcecode:: python

        from djangocodemirror.settings import *
        from djangocodemirror.helper import codemirror_settings_update

        CODEMIRROR_SETTINGS = codemirror_settings_update(CODEMIRROR_SETTINGS, {
            'lineNumber': False,
            'indent': 4
        })

    Sample usage to apply some parameters only on configuration ``python`` and
    keeping only two configurations from default settings:

    .. sourcecode:: python

        from djangocodemirror.settings import *
        from djangocodemirror.helper import codemirror_settings_update

        CODEMIRROR_SETTINGS = codemirror_settings_update(CODEMIRROR_SETTINGS, {
            'lineNumber': False,
            'indent': 4
        }, on=['python'], names=['css', 'python'])


.. Note::
    This helper is not able to delete parameters.

"""
import copy


def codemirror_settings_update(configs, parameters, on=None, names=None):
    """
    Return a new dictionnary of configs updated with given parameters.

    You may use ``on`` and ``names`` arguments to select config or filter out
    some configs from returned dict.

    Arguments:
        configs (dict): Dictionnary of configurations to update.
        parameters (dict): Dictionnary of parameters to apply on selected
            configurations.

    Keyword Arguments:
        on (list): List of configuration names to select for update. If empty,
            all given configurations will be updated.
        names (list): List of configuration names to keep. If not empty, only
            those configurations will be in returned dict. Else every
            configs from original dict will be present.

    Returns:
        dict: Dict of configurations with updated parameters.
    """
    # Deep copy of given config
    output = copy.deepcopy(configs)

    # Optionnaly filtering config from given names
    if names:
        output = {k: output[k] for k in names}

    # Select every config if selectors is empty
    if not on:
        on = output.keys()

    for k in on:
        output[k].update(parameters)

    return output
