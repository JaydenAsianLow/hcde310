# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:



Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*
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
            print(f"{title} — {artist} — {date}")

## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*
https://claude.ai/share/6dada27b-de1e-4988-b329-bb2d4447f832

## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*
it will contain whatever artwork in the format in which I printed

## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*
I knew what it would print because I created the code and told it exactly what to.

## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*
I just added my own comments talking about what each piece of code does.