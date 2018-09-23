"""
Django settings for project demonstration (will not work for unittests)

Actually inherits from settings for Django 1.6. Intended to be used with
``make server``.
"""
import os, copy

from sandbox.settings.base import *

#
# DjangoCodemirror settings
#
from djangocodemirror.settings import *

# Keep default shipped configs
old = copy.deepcopy(CODEMIRROR_SETTINGS)

# Install tests required settings
from sandbox.settings.djangocodemirror_app import *

# Restore default shipped configs additionaly to the tests ones
CODEMIRROR_SETTINGS.update(old)
