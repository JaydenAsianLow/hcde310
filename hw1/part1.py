# HW1 Part 1: Strings
# Run it:  python3 part1.py
# Your output must match expected/part1.txt exactly.
from artworks import titles, artists, years

print(f"{titles[0]} ({years[0]}) by {artists[0]}")
print(titles[0].upper(), len(titles[0]))
print("Bed" in titles[0])