# HW4 Plan

Initial sketch is in the hw4 file under Sketch.png

## 1. Screen Sketches
Home page - search for artwork/artist name

Results page - displays artwork based on user input and helpful messages

## 2. Data Needed
Title - artwork title
Artist Title - artist's name
Date Display - date of artist creation
Artist Display - additional artist information
ID - unique/specific artist ID
Image ID - unique/specific image ID

## 3. Routes and Function Specs.
Home Page (/) - Displays user search form

Results page (/results) - recieves results of user search and displays images or messages depending on results

API search function (search_art) - sends a search message to Art Institute API matching artist titles/artists/, and returns the results

## 4. Checking Work
Search for Monet and verify results appear.

Submit an empty search and verify a helpful message appears.

Search for something with no matching artworks.

Test what happens if the API is unavailable.

Check missing artwork information.