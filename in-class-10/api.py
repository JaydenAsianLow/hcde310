
# api.py: will call Open Library for books by an author.
# SKELETON: get_books() returns fake data for now, so the whole path works before the API does.

import requests

URL = "https://openlibrary.org/search.json"

# Fake data, same shape as the real API's "docs" list.
FAKE_BOOKS = [
    {"title": "Fake Book One", "first_publish_year": 2001},
    {"title": "Fake Book Two", "first_publish_year": 2002},
    {"title": "Fake Book Three", "first_publish_year": 2003},
]

FAKE_EMPTY = []

FAKE_MISSING_FIELDS = [
    {"title": "Fake Book One", "first_publish_year": 2001},
    {"title": "Fake Book Two"},
    {"title": None, "first_publish_year": 2003},
    {"first_publish_year": 2004},
]

FAKE_ERROR = None

# Change this line to test a different case:
FAKE_DATA = FAKE_BOOKS
# Other options: FAKE_EMPTY, FAKE_MISSING_FIELDS, FAKE_ERROR


def get_books(author):
    # Fake for now. When the path works, switch app.py to get_books_real().
    return FAKE_DATA


def get_books_real(author):
    try:
        r = requests.get(
            URL,
            params={"author": author},
            timeout=10,
            headers={"User-Agent": "HCDE310 books app"}
        )
    except requests.RequestException:
        print("API error: no answer")
        return None

    if r.status_code != 200:
        print("API error:", r.status_code, r.reason)
        return None

    return r.json()["docs"][:10]
