from sandbox.demo.forms import SampleForm

from tests.utils import assert_and_parse_html


def test_form_basic():
    """
    Basic form usage
    """
    f = SampleForm({"foo": "bar"})

    rendered = f.as_p()
    expected = (
        """<p><label for="id_foo">Foo:</label> """
        """<textarea id="id_foo" name="foo" """
        """rows="10" cols="40" required>bar</textarea></p>"""
    )

    assert assert_and_parse_html(rendered) == assert_and_parse_html(expected)
