from django.test.html import parse_html


def assert_and_parse_html(html):
    """
    Shortand to use Django HTML parsing as object to use in assert
    """
    return parse_html(html)
