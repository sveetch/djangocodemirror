from djangocodemirror.templatetags.djangocodemirror_tags import codemirror_instance


def test_codemirror_instance_without_assets():
    html = codemirror_instance("basic", "foo_codemirror", "id_foo", assets=False)

    output = (
        """<script>var foo_codemirror = CodeMirror.fromTextArea("""
        """document.getElementById("id_foo"), """
        """{"mode": "rst"});"""
        """</script>"""
    )

    assert html == output


def test_codemirror_instance_varname_dash():
    html = codemirror_instance("basic", "foo_codemirror-0", "id_foo", assets=False)

    output = (
        """<script>var foo_codemirror_0 = CodeMirror.fromTextArea("""
        """document.getElementById("id_foo"), """
        """{"mode": "rst"});"""
        """</script>"""
    )

    assert html == output


def test_codemirror_instance_varname_messy():
    html = codemirror_instance("basic", "foo codemérror-0", "id_foo", assets=False)

    output = (
        """<script>var foo_codemerror_0 = CodeMirror.fromTextArea("""
        """document.getElementById("id_foo"), """
        """{"mode": "rst"});"""
        """</script>"""
    )

    assert html == output


def test_codemirror_instance_with_assets():
    html = codemirror_instance("basic", "foo_codemirror", "id_foo", assets=True)

    output = (
        """<link rel="stylesheet" href="/static/CodeMirror/lib/codemirror.css">"""
        """<script src="/static/CodeMirror/lib/codemirror.js"></script>"""
        """<script>var foo_codemirror = CodeMirror.fromTextArea("""
        """document.getElementById("id_foo"), {"mode": "rst"});"""
        """</script>"""
    )

    assert html == output
