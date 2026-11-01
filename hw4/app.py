# PSEUDOCODE w/ Code

from api import search_art

# 1. Flask:
# Import the Flask tools learned in class in order to create the website, received HTML tempaltes, and use user input
from flask import Flask, render_template, request

app = Flask(__name__)

# 2. Home route (/):
# When a user visits the website, display home.html.
# Show a search form where the user can enter an artwork or artist name.
@app.route("/")
def home():
    return render_template("home.html")

# 4. Results route (/results):
# Recieve user input
# Check if the search term is empty.
# If it is empty, display a helpful message.
# If not empty, send user input into the API search
# Receive the list of matching artworks and see if any match the search term
# If no artworks were found, display a helpful message.
# If artworks were found, send the artwork information to results.html to render.

@app.route("/results")
def results():
    term = request.args.get("artwork_search", "")

    if not term.strip():
        artworks = []
    else:
        artworks = search_art(term)

    return render_template(
        "results.html",
        artworks=artworks,
        term=term
    )

# 5. Start the Flask application so the user can open the website in their browser.
if __name__ == "__main__":
    app.run(debug=True)
