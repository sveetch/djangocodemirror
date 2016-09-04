"""
Tests against template filter for Codemirror config
"""
import pytest

from django.core.urlresolvers import reverse

from djangocodemirror.templatetags.djangocodemirror import codemirror_config

from project.forms import SampleForm


def test_filter_basic():
    """Just pinging dummy homepage"""
    f = SampleForm({'foo': 'bar'})

    f.as_p()

    codemirror_config(f.fields['foo'])

    assert 1 == 1
