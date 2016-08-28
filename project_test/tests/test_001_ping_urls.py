"""
Some dummy pinging to ensure urls are consistent
"""
import pytest

from django.core.urlresolvers import reverse


def test_ping_index(client):
    """Just pinging dummy homepage"""
    response = client.get(reverse('home'))
    assert response.status_code == 200
