# Art Database Modification

## Objective:

This exercise aims to familiarize you with manipulating JSON data by adding, removing, and restructuring information within a JSON object representing a piece of art.


## Exercise Instructions:

You are provided with a JSON file describing a painting titled "The Last of Us Fan Art". Your tasks are as follows:

1. **Add a New Platform:**  Include a new social media platform for the artist. Add an entry to the `socialMediaLinks` array within the `artist` object representing a "Facebook" link with the URL "https://facebook.com/janedoeart".
2. **Update Release Information:** The PlayStation 5 release of "The Last of Us" occurred later. Modify the `releaseDate`  within the `videoGame` object to reflect the game's PlayStation 5 release date, which is "2020-09-02". 
3. **Remove Dimensions:** The dimensions are no longer relevant for this art piece listing. Remove the entire `"dimensions"` field from the JSON.
4. **Restructure Artist Information:** Extract the artist's `name` and `nationality`  from within the `artist` object and create a new top-level field called `artistInfo`. This `artistInfo` field should be an object containing these two properties:

    ```json
    "artistInfo": {
      "name": "Jane Doe",
      "nationality": "American"
    }
    ```



