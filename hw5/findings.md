# HW5 findings

## 1. Drawing: one search for "Monet"
Uploaded into hw5 as photo called Drawing.png

## 2. Two questions about the code
1. What does request.values.get("artist") do and what is the .strip() that follows it?
2. Why does the /results route use methods=["GET", "POST"] when the search form uses POST?

## 3. Checks (4 or more, at least 2 as pytest tests)
| # | Check | Pass or fail |
|---|---|---|
| 1 | Homepage displays artist search form | Pytest | Pass |
| 2 | Searching an artist displays the artist name and their artworks| Pytest | Pass |
| 3 | Submitting an empty search displays a helpful message | Manuel Test | Pass |
| 4 | Searching an artist with no artworks displays a no-results message | Manual Test | Fail |

(4) Search with no matching results: FAIL — Searching for something random displayed actual artwork results instead of a no-results message. The API may be returning broad or unexpected search matches.

## 4. AI review
What it found that I missed: - The exception handler displays the raw error message to the user, which could expose technical details.
- Debug mode is enabled in app.py.
- The API results are not checked to confirm that the artist name matches the search.
What it got wrong: - AI suggested that the API may return broad search matches. This is a possible explanation for the random-name search issue, but I have not confirmed the exact API behavior.
- AI could not fully evaluate accessibility because it did not review the HTML templates.
- Accepting both GET and POST is not necessarily a bug, although POST alone may be more appropriate for this form.
Answers to my two questions, in my own words:
- It grabs the artist value that was sumbitted through the request. The .strip() code removes the whitespace from the beginning/end, so that an empty string or spaces can be handled properly.
- Putting both GET/POST isn't necessarily a bug, but POST may be more appropriate for the form that is being used.

## 5. My fix
What was wrong: 
What I changed:
How I checked it works:
Commit before: (hash)  Commit after: (hash)

## 6. Can we ship it? (100–150 words)
Yes or no, and why:

One thing my HW4 does better:
One thing the AI's app does better:

AI use goes in `ai_use.md` (the five points on the AI Use Card).
