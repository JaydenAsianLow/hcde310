# HW1 notes

## Part 4: Predict, run, explain
from artworks import titles, years

###for i in range(3):
    print(i, titles[i], years[i] + 100)
print(len(titles))
print(len(titles[0]))

**My prediction for `predict.py` (written BEFORE running it):**

My prediction for 'predict.py' is that it will print out:
0 "The Bedroom" Vincent van Gogh 1999
1 "Nighthawks" Edward Hopper 2042
2 "American Gothic" Grant Wood 2030
3 "A Sunday on La Grande Jatte" Georges Seurat 1984
10
11

**What it actually printed:**
0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11

**Explain:** If I was off, which line surprised me and why? If I was right, why do the last two lines print different numbers?

I was off regarding that range doesn't grab 3, but only 0, 1, 2.
I was also off that it doesn't grab the "..." for the titles.
The last two lines print different numbers because the 10 is from how many titles there are while the 11 is how many characters are in the string for "The Bedroom".

## Part 5: Reflection (about 100 words)

Look back at your Day 1 app: its code if you can still open it, or your screenshots of it running. Is there anything you can now recognize (a loop, an `if`, a list)? Where? If you only have screenshots, what do you think the code had to do to make the app behave that way?

There are many instances throughout the code where I can now recognize the for and if statements and sort of understand whats going on.
Even though the code is still advanced, I can get a general idea of what's going on.
I also can make out the prints now with print(f"") as I did not know how to use f strings.
The code had many if statements and lists because the code had to be able to loop through all the different artworks and find it depending on the title or artist, and if not, produce a statement telling the user it didn't find anything.