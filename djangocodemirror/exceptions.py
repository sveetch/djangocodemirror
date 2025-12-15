"""
Specific application exceptions.
"""


class DjangocodemirrorBaseException(Exception):
    """
    Exception base.

    You should never use it directly except for test purpose. Instead make or
    use a dedicated exception related to the error context.
    """
    pass


class AppOperationError(DjangocodemirrorBaseException):
    """
    Sample exception to raise from your code.
    """
    pass


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
