import app as app_module
from app import app


def test_home_shows_search_form():
    client = app.test_client()
    page = client.get("/")

    assert page.status_code == 200
    assert b"Artist name" in page.data


def test_search_displays_artwork(monkeypatch):
    def fake_get_artworks(artist):
        return [{
            "title": "Water Lilies",
            "date_display": "1906",
            "image_id": "example123"
        }]

    monkeypatch.setattr(app_module, "get_artworks", fake_get_artworks)

    client = app.test_client()
    page = client.post("/results", data={"artist": "Monet"})

    assert page.status_code == 200
    assert b"Results for" in page.data
    assert b"Monet" in page.data
    assert b"Water Lilies" in page.data


def test_search_shows_friendly_message_on_error(monkeypatch):
    def fake_get_artworks(artist):
        raise Exception("Sensitive technical error")

    monkeypatch.setattr(app_module, "get_artworks", fake_get_artworks)

    client = app.test_client()
    page = client.post("/results", data={"artist": "Monet"})

    assert page.status_code == 200
    assert b"Sorry, we couldn&#39;t retrieve the artwork." in page.data
    assert b"Sensitive technical error" not in page.data