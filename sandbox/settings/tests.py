"""
Django settings for tests
"""
import os, copy

from sandbox.settings.base import *

#
# DjangoCodemirror settings
#
from djangocodemirror.settings import *

# Install tests required settings
from sandbox.settings.djangocodemirror_app import *
