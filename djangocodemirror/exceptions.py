# -*- coding: utf-8 -*-
"""
Internal exceptions
===================

"""


class NotRegisteredError(KeyError):
    pass


class UnknowConfigError(KeyError):
    pass


class UnknowModeError(KeyError):
    pass


class UnknowThemeError(KeyError):
    pass


class CodeMirrorFieldBundleError(KeyError):
    pass
