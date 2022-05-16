from django.urls import reverse


def test_home_page_view(client):
    response = client.get(reverse("blog:home"), secure=True)
    response.status_code == 200


def test_about_view(client):
    response = client.get(reverse("blog:about"), secure=True)
    assert response.status_code == 200


def test_contact_view(client):
    response = client.get(reverse("blog:contact"), secure=True)
    assert response.status_code == 200


def test_talks_view(client):
    response = client.get(reverse("blog:talks"), secure=True)
    assert response.status_code == 200


def test_past_events_view(client):
    response = client.get(reverse("blog:past_events"), secure=True)
    assert response.status_code == 200


def test_thank_you_view(client):
    response = client.get(reverse("blog:thank_you"), secure=True)
    assert response.status_code == 200


def test_search_view(client):
    response = client.get(reverse("blog:search"), secure=True)
    assert response.status_code == 200


def test_robots_txt_view(client):
    response = client.get(reverse("blog:robots"), secure=True)
    assert response.status_code == 200


def test_sitemap_xml_view(client):
    response = client.get(reverse("blog:sitemap"), secure=True)
    assert response.status_code == 200


def test_upcoming_events_view(client):
    response = client.get(reverse("blog:upcoming_events"), secure=True)
    assert response.status_code == 200


def test_talk_view(client, talk):
    response = client.get(reverse("blog:talk", args=(talk.pk,)), secure=True)
    assert response.status_code == 200


def test_post_view(client, post):
    response = client.get(reverse("blog:post", args=(post.pk,)), secure=True)
    assert response.status_code == 200


def test_category_view(client, category):
    response = client.get(reverse("blog:category", args=(category.pk,)), secure=True)
    assert response.status_code == 200
