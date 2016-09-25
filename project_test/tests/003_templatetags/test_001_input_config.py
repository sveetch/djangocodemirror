"""
Tests against template tags for Codemirror config
"""
import json
import pytest

from djangocodemirror.widgets import CodeMirrorWidget
from djangocodemirror.templatetags import djangocodemirror_tags

from project.forms import ManyFieldsSampleForm


@pytest.mark.parametrize('name,attempted', [
    (
        'foo',
        {
            "mode": "rst",
        }
    ),
    (
        'ping',
        {
            "mode": "rst",
            "lineNumbers": True,
            "lineWrapping": True,
            "theme": "neat",
        }
    ),
], ids=["foo-basic", "ping-with-all"])
def test_codemirror_parameters(name, attempted):
    """Test codemirror_parameters tag"""
    f = ManyFieldsSampleForm()

    f.as_p()

    p = djangocodemirror_tags.codemirror_parameters(f.fields[name])

    assert json.loads(p) == attempted
