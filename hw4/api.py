
import requests

FIELDS = "id,title,artist_title,artist_display,date_display"


def search_art(term):
    """Search the Art Institute API and return matching artworks."""

    url = "https://api.artic.edu/api/v1/artworks/search"

    params = {
        "q": term,
        "fields": FIELDS
    }

    headers = {
        "User-Agent": "HCDE310 student project"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=10
    )

    print("API URL:", response.url)
    print("Status code:", response.status_code)

    if response.status_code != 200:
        print("API request failed:", response.text)
        return None

    data = response.json()
import requests

FIELDS = "id,title,artist_title,artist_display,date_display"


def search_art(term):
    """Search the Art Institute API and return matching artworks."""

    url = "https://api.artic.edu/api/v1/artworks/search"

    params = {
        "q": term,
        "fields": FIELDS
    }

    headers = {
        "User-Agent": "HCDE310 student project"
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            print("API request failed:", response.status_code)
            return None

        data = response.json()
        artworks = data.get("data", [])

        # Keep only artworks whose title or artist matches the search
        matching_artworks = []

        for art in artworks:
            title = art.get("title") or ""
            artist = art.get("artist_title") or ""

            if term.lower() in title.lower() or term.lower() in artist.lower():
                matching_artworks.append(art)

        return matching_artworks

    except requests.RequestException as e:
        print("API connection error:", e)
        return None