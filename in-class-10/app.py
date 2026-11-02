
# app.py: the routes for the books app.
# The whole path works (form → /results → results page) with fake data.
# Next: replace one piece at a time, and commit each time something works.

from flask import Flask, render_template, request
from api import get_books_real
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results")
def results():
    # 1. Read the search term from the form
    author = request.args.get("author_search", "")

    # 2. Empty input? Return home page with a message.
    if not author.strip():
        return render_template(
            "home.html",
            message="Please enter an author's name."
        )

    # 3. Call the API (fake data for now)
    books = get_books_real(author)

    # 4. API error? get_books returned None.
    if books is None:
        return render_template(
            "home.html",
            message="Sorry, something went wrong while retrieving books. Please try again."
        )

    # 5. No results, or nothing useful to show?
    useful_books = []

    for book in books:
        if book.get("title") or book.get("first_publish_year"):
            useful_books.append(book)

    if not useful_books:
        return render_template(
            "home.html",
            message=f"No books found for {author}. Please try another author."
        )

    # 6. Otherwise, display the results page.
    return render_template(
        "results.html",
        books=useful_books,
        author=author
    )


if __name__ == "__main__":
    app.run(debug=True)
