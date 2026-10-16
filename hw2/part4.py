# HW2 Part 4 – Your first functions
#
# In `part4.py`, turn code you already wrote into functions:
#
# 1. `works_by(artist, artworks)` → returns a list of titles by that artist, from the list you pass in
#    (an empty list if there are none)
# 2. `count_by_artist(artworks)` → returns your counting dictionary from Part 3
# 3. Replace each `TODO` docstring with one line saying what the function takes and what it returns
#
# Don't change the `print` lines at the bottom of `part4.py`. `check.py` uses them.

from artworks import artworks


def works_by(artist, artworks):
###TODO: Takes all the works by an artist and return the list of titles###
    result = []

    for art in artworks:
        if art.get("artist") == artist:
            result.append(art.get("title", "Unknown"))
    return result


def count_by_artist(artworks):
###TODO: Takes all the artworks and returns the counts of the # of art created by each artist.###
    counts = {}
    for art in artworks:
        artist = art.get("artist", "Unknown")
        if artist in counts:
            counts[artist] = counts[artist] + 1
        else:
            counts[artist] = 1
    return counts

print(works_by("Claude Monet", artworks))
print(works_by("Nobody", artworks))
print(count_by_artist(artworks))
