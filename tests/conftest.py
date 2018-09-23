"""
Some fixture methods
"""
import pytest

from django.conf import settings

from djangocodemirror.manifest import CodeMirrorManifest


@pytest.fixture(scope="function")
def manifesto():
    """Return a CodeMirrorManifest instance"""
    return CodeMirrorManifest()
