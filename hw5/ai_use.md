## Usage of AI

I used AI throughout this assignment and other parts of the course to help me understand concepts I struggled with, debug code, and complete tasks when the assignment instructions specifically asked me to use AI.

For this assignment, I used AI to:

Review my Flask app for bugs, missing error handling, accessibility, and security issues.

Help me understand and fix an error-handling issue in the app.

Debug and write pytest tests to check the app's behavior.

Help draft and organize parts of my findings.md file.

I reviewed the suggestions, made changes to the code, and ran the tests to check that the changes worked. AI was helpful for explaining unfamiliar concepts and troubleshooting, but I still needed to understand the code and verify the results myself.



Selected AI Conversation Logs — HW5

1. Understanding the Flask code

My questions (paraphrased):

What does request.values.get("artist") do?

Why does the code use .strip() afterward?

Why does the /results route accept both GET and POST when the form uses POST?

AI assistance:
AI explained that request.values.get("artist") retrieves the artist search term from the request parameters. The .strip() method removes extra whitespace from the beginning and end of the input. The route accepts GET and POST because it was configured to handle both request methods, even though the form submits using POST.

2. AI code review — Step 4

Assignment-provided prompt:

"Review this Flask app for bugs, missing error handling, accessibility and security problems. For each one, point to the line."

AI findings (summary):

The exception handler displayed raw technical error details to users.

app.run(debug=True) should only be used during development.

The API response parsing assumes that the response contains valid JSON with a data field.

The API request already included a timeout and raise_for_status(), which are useful safeguards.

The HTML templates included labels, headings, language declarations, and image alt text. Adding a required attribute to the search input could improve form usability.

3. Debugging and testing

My work/questions (paraphrased):
I asked for help understanding how to test what happens when an API request fails and how to make sure technical error details aren't displayed to users.

AI assistance:
AI explained how to use a mock function in pytest to simulate an API error. The test checks that the application displays a friendly error message and does not expose the underlying technical exception.

4. Reflection on AI use

AI helped me understand unfamiliar Python and Flask concepts, interpret code review feedback, and troubleshoot errors. I used the suggestions to make changes and then ran pytest to verify the behavior. I learned that AI suggestions still need to be checked because not every finding necessarily represents a real problem.