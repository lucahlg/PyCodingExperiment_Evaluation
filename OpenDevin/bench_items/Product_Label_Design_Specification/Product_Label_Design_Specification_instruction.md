# Designing a Brochure: JSON Manipulation

## Objective:

This exercise aims to enhance your understanding of JSON manipulation by modifying and restructuring a JSON object representing a product brochure.

## Exercise Instructions:

You are provided with a JSON file describing the design specifications for a product brochure. Your tasks are as follows:

1. **Add New Image:** Incorporate a new image into the "images" array. The new image should have the following properties:
    - `"url"`: `"https://example.com/image3.jpg"`
    - `"width"`: 150
    - `"height"`: 150

2. **Update Font Size:** Increase the font size of the welcome message ("Welcome to our company!") in the "texts" array to 20.

3. **Change Ink Type:** The design team decided to use a different ink type. Update the "ink" property to `"soy-based"`.

4. **Add a New Color:**  Include a new color, `"red"`, to the "colors" array.

5. **Restructure Text Information:** Create a nested object within each element of the "texts" array called "styling". This object should contain the properties:
    - `"font"` (existing font property)
    - `"size"` (existing size property)
    - `"color"` (existing color property)

This will restructure the text information to be more organized.



