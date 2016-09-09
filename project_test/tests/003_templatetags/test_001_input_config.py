"""
Tests against template tags for Codemirror config
"""
import json
import pytest

from djangocodemirror.widgets import CodeMirrorWidget
from djangocodemirror.templatetags import djangocodemirror_tags

from project.forms import SampleForm


def test_resolve_widget():
    """
    Check widget resolving from a field

    Note:
        We should test also against BoundField but it seems to involve template
        resolving and i'm too lazy for that now.
    """
    f = SampleForm({'foo': 'bar'})

    w = djangocodemirror_tags.resolve_widget(f.fields['foo'])

    assert isinstance(w, CodeMirrorWidget) == True


def test_codemirror_parameters():
    """Test codemirror_parameters tag"""
    f = SampleForm({'foo': 'bar'})

    f.as_p()

    p = djangocodemirror_tags.codemirror_parameters(f.fields['foo'])

    assert json.loads(p) == {
        "lineNumbers": True,
        "lineWrapping": True,
        "mode": "rst"
    }
