# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display"

# Functions go here (above the code that runs)
def count_by_artist(artworks):
    artist_counts = {}

    for art in artworks:
        artist = art.get("artist_title") or "Unknown"

        if artist in artist_counts:
            artist_counts[artist] += 1
        else:
            artist_counts[artist] = 1

    return artist_counts

def save_results(artworks, filename):
    # Opens file
    with open(filename, "w", encoding="utf-8") as file:
        # Go through each artwork in the list.
        for art in artworks:
            # Get the title or replace with Unknown
            title = art.get("title") or "Unknown"
            # Get the artist or replace with Unknown
            artist = art.get("artist_title") or "Unknown"
            # Get the date or replace with Unknown
            date = art.get("date_display") or "Unknown"
            # Formats the title, artist, and date in the .txt file
            file.write(f"{title} — {artist} — {date}\n")

term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"      # TODO: the search URL from step 2
params = {"q": term, "fields": FIELDS}   # TODO: q (the search term) and fields (FIELDS)
response = requests.get(url, params=params, headers={"AIC-User-Agent": "HCDE310 student project"})

# TODO step 3: check response.status_code before you use the data
if response.status_code != 200:
    print(f"Request failed: {response.status_code} {response.reason}")
else:
    data = response.json()
    results = data.get("data", [])
    save_results(results, "artworks.txt")
# TODO steps 4-5: loop over the results and print each one (reuse your HW2 printing code),
#                 print a default for null fields, and print a helpful message if there are no results

    if len(results) == 0:
        print(f"No artworks found for '{term}'.")
    else:
        for art in results:
            print(f'Title: {art.get("title") or "Unknown"}')
            print(f'Artist: {art.get("artist_title") or "Unknown"}')
            print(f'Artist details: {art.get("artist_display") or "Unknown"}')
            print(f'ID: {art.get("id") or "Unknown"}')
            print(f'Date: {art.get("date_display") or "Unknown"}')