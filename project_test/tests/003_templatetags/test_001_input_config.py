"""
Tests against template tags for Codemirror config
"""
import json
import pytest

from djangocodemirror.widgets import CodeMirrorWidget
from djangocodemirror.templatetags import djangocodemirror_tags

from project.forms import SampleForm


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
