# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?
'artworks' is a list of dictionaries and not one big one because it has dictionaries within it. This was done to make it easier to look at when coding and formating through the artworks. If it were to become a big dictionary, it would probably be easier to lookup different art with their artist and their dates at the same time, but will be harder to look at and more complex if you want to grab specifics from each piece of art.

## 2. Which fields are sometimes missing? What should the app show when they are?
Nighthawks [title: 2], The Old Guitarist [title 5], The Child's Bath [title: 7], Sky Above Clouds IV [title: 8], Stacks of Wheat (End of Summer) [title: 9] are lines are missing their mediums
Untitles Vase [title: 10] is missing the artist, year, and medium
The app should display some sort of Unavailability print if the user were to try to search for the missing fields of a certain piece of art.
