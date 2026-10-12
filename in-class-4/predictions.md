# Class 4: Five broken snippets

Your name: Jayden Low
Collaborator: Reid Schmidt

# Part 1: Predict

**Don't run anything yet.** Read each snippet in `exercise.py` and write your guesses. A wrong guess is fine: the point is to compare.

## Snippet 1
- Which line breaks?
line 8 breaks, as there isn't specification on capitatlization.
- What error will Python show? (the kind and the message)
Name Error
- What's the fix?
print("Find it in room " + exhibit["room"])


## Snippet 2
- Which line breaks?
Line 2
- What error will Python show? (the kind and the message)
Type Error
- What's the fix?
print(f"Find it in room {exhibit["room"]}")


## Snippet 3
- Which line breaks?
line 2 and 3
- What error will Python show? (the kind and the message)
Index Error
- What's the fix?
for i in range(len(exhibits)):
    print(i, exhibits[i])

## Snippet 4
- Which line breaks?
Line 10
- What error will Python show? (the kind and the message)
Key Error
- What's the fix?
print(count_visits(visits, 243))


## Snippet 5
- Which line breaks?
Line 7
- What error will Python show? (the kind and the message)
Not sure what kind of error
- What's the fix?
return(longest)

# Part 2: Run

Run `python3 exercise.py`. Python stops at the first error, so fix that snippet in `exercise.py`, run again, and see the next one. Fill in what actually happened.

## Snippet 1
- Which line broke?
line 8
- What error did Python show?
Key Error
- What's the fix?
print(f"Find it in room {exhibit["room"]}")

## Snippet 2
- Which line broke?
line 12
- What error did Python show?
Type Error
- What's the fix?
print(f"Find it in room {exhibit["room"]}")

## Snippet 3
- Which line broke?
line 17
- What error did Python show?
Index Error
- What's the fix?
for i in range(len(exhibits)):

## Snippet 4
- Which line broke?
line 29
- What error did Python show?
Name Error
- What's the fix?
print(count_visits(visits, 243))

## Snippet 5
- Which line broke?
line 38
- What error did Python show?
Attribute Error
- What's the fix?
      return(longest)

When all five are fixed, run `python3 check.py` until it says ✓.

Bonus: Snippet 5 prints something *before* it crashes. What, and why does it still crash?

Not sure, didn't check it before the change

# Part 3: Tutor practice (one snippet)

Pick one snippet. Write your guess first, then ask your tutor. Paste the chat (or a share link) below.

https://claude.ai/share/bdc38f6d-520f-48c2-a2f9-819d2afd0f1a

- Snippet #: 1
- Our guess before asking:
Will give me: Find it in room 243
- Chat:
exhibit = {"title": "Water Lilies", "room": 243, "year": 1906}
print(f"Find it in room {exhibit["room"]}")
Helping with a coding question using a guided approach.
Helping with a coding question using a guided approach.
Thanks for sharing your attempt. Before you run it, take a moment to predict.

Read the code line by line and tell me exactly what you think it will print when you run it. If you think it might not print anything, tell me what you expect to happen instead.

Will produce Find it in the room: 243
Comparing the predicted wording against the actual room text.
Comparing the predicted wording against the actual room text.
You got the key idea: the 243 comes from looking up "room" in the dictionary and putting it into the sentence. Take another look at the text around it, though. Compare your prediction word for word with the string inside the print. Is there a “the” or a colon in the code?

The next step in your routine is Run. Run the code exactly as you pasted it, then paste back everything Python shows you, whether that’s the output or an error message. Then we’ll compare it to your prediction.

Find it in the room 243

Checking the room number formatting in the output text.
Checking the room number formatting in the output text.
Let’s check that against the code. Look at the text inside the quotes in your print line, just before the {. Does the word “the” appear there?

If it doesn’t, your output may have been typed from memory rather than copied from the terminal. Run it again and copy-paste exactly what Python shows you, including any error message if there is one.

"Find it in the room 243"

Debugging the exhibit text for a stray quoting error.
Debugging the exhibit text for a stray quoting error.
Thanks for retyping it, but that output still doesn’t match the code you pasted. The string in your print line reads Find it in room, with no “the” anywhere, so that code can’t produce the sentence you’re showing me.

That usually means one of two things: the file you ran has slightly different text than what you pasted, or the output was typed in rather than copied from the terminal.

Could you run the file once more and copy-paste exactly what appears in your terminal, with no retyping? If an error message shows up instead of a sentence, paste that too.

Find it in room 243

Debugging quote nesting inside an f-string expression.
Debugging quote nesting inside an f-string expression.
That matches the code, and it’s the output the program really produces. Your prediction was close: you correctly saw that the number 243 gets pulled out of the dictionary and placed inside the sentence. What you missed was the exact wording of the text around it (“the” and the colon weren’t in the code), so with small details like that, reading the string character by character is a good habit.

Now the Explain step. In your own words, what do you think happens inside the curly braces, {exhibit["room"]}, to turn that piece of code into 243?


- Did it give you too much? What did you do?
It gave less that I thought. It didn't give me answer but was more verifying for me and making sure if I am sure about the answer and that my answer didn't match the code if I input a different ans
