# Enhance a Blooper Compilation JSON

## Objective:

Practice manipulating and restructuring JSON data by adding new information, modifying existing values, and reorganizing the structure of a blooper compilation object.

## Exercise Instructions:

You are given a JSON file representing a collection of "The Office" bloopers. Your tasks are as follows:

1. **Add a New Clip:** Append a new blooper clip to the `clips` array. The new clip should have the following details:
    - `"url"`:  "https://www.youtube.com/watch?v=3"
    - `"source"`: "YouTube"
    - `"title"`: "Pam's Teapot Surprise"
    - `"description"`: "Pam pranks Jim with a hidden teapot filled with chili." 

2. **Update the Rating:** The blooper compilation received rave reviews. Update the `rating` to 4.8.

3. **Add a New Tag:** Include a new tag, "viral", in the `tags` array to reflect the popularity of the bloopers.

4. **Restructure Cast Information:** Instead of storing cast information as separate objects within an array, create a new object called `"characters"` within the main JSON object. This object will contain key-value pairs where the keys are character names (e.g., "Michael Scott") and the values are the actors' names (e.g., "Steve Carell").

5. **Remove View Count:** The view count is no longer relevant. Remove the `viewCount` property from the JSON object. 



