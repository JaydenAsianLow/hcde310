# HW2 Part 6 – AI log (`ai_log.md`)

The tutor walks you through the routine (Try → Predict → Run → Explain → Log) as you chat, so your transcript shows most of it. In `ai_log.md`:

---

## 1. One prediction
*copy one prediction you made in a chat. Were you right? If not, what surprised you?*
I didn't use the Claude Tutor, but I copied Question #2 with my answer into it and it says I got a full attempt response. It is asking me to attempt now even though I uploaded my answer. Im surprised how strict it follows the tutor prompt: Try → Predict → Run → Explain → Log routine.

## 2. What clicked
*pick one thing you were stuck on or didn't know. Without looking at the transcript, explain it in your own words.*
I uploaded this: print(f"{art("title", "Unknown")} - {art.get("artist", "Unknown")} ({art("year", "Unknown")})")

I don't understand the question your trying to ask, but the Claude tutor was helpful in giving me a hint in saying to look at all 3 {...} and telling me which matches best with what I learned about .get().

## 3. Too much?
*Did the tutor ever give you too much? What did you do? (one line)*
Not really

## 4. Transcripts
*paste every tutor chat you used for HW2 (one is fine if that's all you had)*
 In `part2.py`, print each artwork as `Title - Artist (Year)`, for example `The Bedroom - Vincent van
 Gogh (1889)`. Use `.get()` so a missing artist or year prints `Unknown` instead of crashing.

from artworks import artworks

for art in artworks:
    print(f"{art.get("title", "Unknown")} - {art.get("artist", "Unknown")} ({art.get("year", "Unknown")})")
Reviewing the latest attempt before deciding the next step.

You’ve got a full attempt there, so we’re in the Try step. I’ll hold my earlier question about the curly braces and come back to it afterward.

Before you run part2.py, predict what it will print. Imagine one entry in artworks is {"title": "The Bedroom", "artist": "Vincent van Gogh"}, with no "year" key at all. What exact line do you expect to see for it, and why?

im confused on :     print(f"{art("title", "Unknown")} - {art.get("artist", "Unknown")} ({art("year", "Unknown")})") given 


artworks = [
    {"title": "The Bedroom", "artist": "Vincent van Gogh", "year": 1889, "medium": "Oil on canvas"},
    {"title": "Nighthawks", "artist": "Edward Hopper", "year": 1942},
    {"title": "American Gothic", "artist": "Grant Wood", "year": 1930, "medium": "Oil on beaver board"},
    {"title": "A Sunday on La Grande Jatte", "artist": "Georges Seurat", "year": 1884, "medium": "Oil on canvas"},
    {"title": "The Old Guitarist", "artist": "Pablo Picasso", "year": 1903},
    {"title": "Water Lilies", "artist": "Claude Monet", "year": 1906, "medium": "Oil on canvas"},
    {"title": "The Child's Bath", "artist": "Mary Cassatt"},
    {"title": "Sky above Clouds IV", "artist": "Georgia O'Keeffe", "year": 1965},
    {"title": "Stacks of Wheat (End of Summer)", "artist": "Claude Monet", "year": 1890},
    {"title": "Untitled (vase)"},
]
Spotting a code change in the reported snippet.

Thanks for pasting your data, it’s helpful to see the dictionaries, especially the ones with missing keys. I also see that this line looks different from the one you pasted earlier, and that may be where the confusion comes from.

Look at the three {...} pieces in the line you just pasted: the one for the title, the one for the artist, and the one for the year. Two of them are written one way and one is written another way.

What’s the difference between them, and which version do you think matches what you learned about .get()?