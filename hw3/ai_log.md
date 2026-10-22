# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I follow a routine: Try → Predict → Run → Explain → Log.
My attempt so far: [paste your code or plan, even if it doesn't work] Where I'm stuck: [one sentence] The function I need: [name]([inputs]) takes [what] and returns [what].
Rules: - Write only this one function, about 10 lines or fewer. No other code, and don't change mine. - Put # AI-written on the line above the function. - Start the function with a one-line docstring that says what it takes and returns. - Use only what a beginner would know: loops, if, lists, dictionaries, and the libraries I'm already using. If you need something new, tell me its name and what it does in one line. - Don't explain the code yet. Ask me to predict what it returns for [one real input]. Wait for my prediction. - After I've run it and told you the result, ask me to explain each line in my own words. Correct anything I got wrong, then ask me about one line I skipped. - Then suggest one small change I could make myself (don't write it). Wait until I tell you what I changed. - Then ask me: what's one thing that surprised you? Don't answer it for me. - For anything other than this one function, act as my tutor: hints and questions, no code.

Your message still has the template placeholders in it ([paste your code or plan...], [name]([inputs]), [one real input]), so I don’t have your actual attempt or the function you need yet.

I also need to flag a conflict: your saved rule is that I never write code for your assignment, even if asked. A full function from me would break that, so I won’t write it. If this is for an assignment, I can give you hints and questions instead. If it’s a practice exercise outside your coursework, tell me and we can talk about how you’d like to handle it.

Following your routine, the first step is Try, so let’s start there. Please send me:

Your attempt so far (code or a plain-English plan, even if it’s broken)
The function you’re trying to build: its name, what it takes in, and what it should return
One sentence on where you’re stuck

Once I see your attempt, I’ll ask you one guiding question to get us moving.

Write a new function, save_results(artworks, filename), that writes one line per artwork (title, artist, date) to a .txt file. Call it so every search saves its results. Then run fetch.py for real once, with a search you pick, and commit the .txt file it made: that's your proof the live call works.
You may have the AI write this function (about 10 lines) using the [Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt) (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in ai_log.md as you go:

Try: paste your own attempt or plan for the function, even if it doesn't work
Prompt (AI only): paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."
Predict: before you run the function, write what you think the file will contain for the sample data (check.py uses it) or for your search
Run and compare: paste what the file actually contains. Were you right? If not, what surprised you? (A wrong prediction gets full credit. Don't edit it after running.)
Explain: add a comment above every line of the function saying what it does, in your own words
Weighing a no-code preference against the assignment's own suggestion.

This is your assignment, and your rule is that I never write code for your assignment, even when the assignment allows AI help. So I won’t write save_results. I’ll give you a hint and a question instead.

Here’s a tiny example with different data and a different task:

python
with open("pets.txt", "w") as f:
    f.write("Rex, dog\n")

Also, I can’t run fetch.py or commit files for you. The live run and the commit have to come from you on your machine, which is the proof your instructor wants anyway.

Your routine starts with Try, and I haven’t seen your attempt yet. So here’s my one question: in plain English, what should save_results do for each artwork in the list? Write it as a rough plan, even if you’re not sure how to code it, and paste it here along with any code you’ve started.

Good, that output shows your formatting works: the em dashes, the “Unknown” fallback on the Baroque Pearl line, and the dates all came out the way you intended.

But that’s what showed up in your terminal. Your function never wrote anything to the file. So now your prediction can get sharper. Look at the last line of your function and compare it to my pets example from earlier, which used f.write(...). What’s the difference between what print(...) does and what file.write(...) does?

Based on that, what do you predict results.txt contains after this run: the ten lines, or something else? Write that in ai_log.md as your prediction, and then check the file itself to compare.

file.write puts it into the txt file while print just puts in terminal. so i changed it

Right: print goes to the terminal, file.write goes into the file. That’s the key idea in this function.

Before you run it again, one thing to check on your own: in my pets example, I wrote "Rex, dog\n". Look at the end of that string. What do you think \n does, and could leaving it out change what ends up in your file when you write ten artworks in a row?

Predict first, then run it and open results.txt. Paste what the file actually contains, and tell me whether your prediction matched.

Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*


## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*


## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*


## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*


## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*
