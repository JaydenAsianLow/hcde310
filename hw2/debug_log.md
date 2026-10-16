# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message
    print(f"{art("title", "Unknown")} - {art.get("artist", "Unknown")} ({art("year", "Unknown")})")
             ^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'dict' object is not callable


### 2. What I thought it meant
I thought it mean't that I was missing parenthesis somewhere because there was a whole lot of symbols going on.

### 3. What it actually meant
It actually mean't that I was trying to grab "title" out of the dictionary art with parenthesis () which I can't unless I did .get().

### 4. The fix
I changed all the parts that were art() to art.get()

## Entry 2

### 1. Error message
  File "c:\Users\lowjay00\Documents\hcde310\hw2\part4.py", line 16
    """TODO: Takes all the works by an artist and return the list of titles"""
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
IndentationError: expected an indented block after function definition on line 15

### 2. What I thought it meant
I thought it just assumed that """ didn't register it as a comment.

### 3. What it actually meant
It still needs an indent regardless and it would be recognized as a string.

### 4. The fix
I just fixed it to ### as that is what I usually do for comments.