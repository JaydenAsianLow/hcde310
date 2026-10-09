# HW1 Part 3: Decisions
# Run it:  python3 part3.py
# Your output must match expected/part3.txt exactly.

from artworks import titles, years

cutoff = 1900  # works made before this year are "old"
for i in range(len(titles)):
    if years[i] > cutoff:
        print(titles[i])

print()
for i in range(len(titles)):
    if years[i] < cutoff:
        print(f"{titles[i]}: old")
    else:
        print(f"{titles[i]}: modern")

print()
old = 0
modern = 0
for i in range(len(titles)):
    if years[i] < cutoff:
        old = old + 1
    else:
        modern = modern + 1
print(f"Old: {old}")
print(f"Modern: {modern}")
