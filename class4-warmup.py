#def label(year):
#   if year < 1900:
#        return "old"
#    return "modern"
#print(label(1889), label(1942))

#def works_ny(artist, artists, titles):
#    """Return the titles by one artust"""
#    found = []
#    for i in range(len(titles)):
#        if artists[i] == artist:
#            found.append(titles[i])
#    return found

titles = ["Nighthawks", "The Bedroom", "Sky above Clouds IV"]
for t in titles:
    if "the" in t.lower():
        print(t)