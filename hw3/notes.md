# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?
data["data][0]["title"]

## 2. Find 3 more fields you'd want to show a user, and their paths
data["data][0]["artist_display"]
data["data][0]["id"]
data["data][0]["date_display"]


## 3. Which fields are `null` for some works?
data["data][2]["artist_title"]


## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*
There will be an error as nothing is filled out yet. There is no url, and no parameters set.

## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*
response doesn't have a url or parameter linked to it, it's empty, so my user input for 'cat' can't even be searched because there is no where for the code to search for it, which is why I get can error in lines 16, 87, 71, 635, 541, 439, and 514. 