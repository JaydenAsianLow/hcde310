# HW1 Part 2: Lists and loops
# Run it:  python3 part2.py
# Your output must match expected/part2.txt exactly.

from artworks import titles
for i in range(len(titles)):
    print(f"{i+1}. {titles[i]}")
print(f"Titles: {len(titles)}")

count = 0
for j in titles:
    if "a" in j:
        count = count + 1
print(f'Titles with an "a": {count}')

for k in titles:
    if len(k) > len(titles[0]):
        longest = k
        
print(f"Longest: {longest}")