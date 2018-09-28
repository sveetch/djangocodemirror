"""
Test utilities
"""
from django.test.html import HTMLParseError, parse_html


def assert_and_parse_html(html):
    """
    Shortand to use Django HTML parsing as object to use in assert
    """
    dom = parse_html(html)
    return dom
