from django.urls import reverse


def test_ping_index(client):
    """
    Just pinging dummy homepage
    """
    response = client.get(reverse("demo:home"))
    assert response.status_code == 200
