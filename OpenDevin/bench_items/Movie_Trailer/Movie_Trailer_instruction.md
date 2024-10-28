# Analyze and Modify a Movie JSON Object

## Objective:

The goal of this exercise is to analyze and modify information about a movie stored in a JSON object. You will add new data points, update existing ones, and restructure parts of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a movie. Your tasks are as follows:

1. **Add Director Information:**  Add a new property called "director" to the JSON object. The director should be represented as an object with two properties:
    - "name": "Peter Jackson"
    - "awardsWon": 3

2. **Update Trailer Quality:** Update the "trailerQuality" property to "Excellent".
3. **Add a New Genre:** Add the genre "Epic" to the "genres" array.
4. **Restructure Cast Information:** Create a new property called "mainCharacters" which will hold an array of objects, each representing a main character.  Each object should have:
    - "actor": The name of the actor (taken from the existing "castMembers")
    - "character": The name of the character they play (taken from the existing "castMembers").

5. **Remove Trailer Format:** Remove the "trailerFormat" property.


