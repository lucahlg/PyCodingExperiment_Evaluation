# Modify a Poster Design Request

## Objective:

This exercise aims to familiarize you with manipulating JSON data structures. You'll modify a JSON object representing a poster design request, adding new information and refining existing details.

## Exercise Instructions:

You are provided with a JSON file outlining a poster design request. Complete the following tasks:

1. **Add Image Dimensions:** Within the "artworkFile" object, add two new properties: 
    - `"width"`: Set this to  `420`.
    - `"height"`: Set this to `594`, reflecting the dimensions of an A2 poster in millimeters.
2. **Specify Color Palette:** Add a new property called "colorPalette" at the top level of the JSON object. Set its value to an array containing three strings representing desired colors (e.g., ["#FF0000", "#00FF00", "#0000FF"]). Choose any color scheme you like!
3. **Update Design Request:** Modify the "designRequest" property. Instead of just stating "Please use a bold and eye-catching design...", provide more specific guidance. For example: "Please create a futuristic design featuring geometric shapes and vibrant colors. The poster should convey a sense of innovation and excitement."

4. **Remove Special Requests:** Remove the entire "specialRequests" property from the JSON object as it is already implied that high-quality printing is expected.



