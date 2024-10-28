#  Art Auction Data Analysis

## Objective: 

This exercise focuses on manipulating and restructuring an auction data JSON file. You will be performing various tasks to gain a deeper understanding of how to work with nested JSON structures.

## Exercise Instructions:

You are provided with a JSON file representing art auction data. Your tasks are as follows:

1. **Add a New Artwork:**  Include a new artwork to the "artworks" array. The artwork details should be as follows:
    -  **title**: "The Scream" 
    -  **artist**: 
        - **name**: "Edvard Munch"
        - **nationality**: "Norwegian"
    -  **year**: 1893
    -  **medium**: "Tempera and crayon on cardboard"
    -  **dimensions**:
        - **height**: 91
        - **width**: 73.5
        - **unit**: "cm"

    -  **description**: "This iconic expressionist painting portrays a figure with an anguished facial expression against a swirling, fiery background."

    - **estimate**:
        - **low**: 80000000
        - **high**: 120000000
        - **currency**: "USD"

2. **Update Artist Information:** Change the nationality of Claude Monet to "French Impressionist".

3. **Remove Artwork Dimension:** Delete the "dimensions" object for Vincent van Gogh's "Starry Night" artwork.

4.  **Calculate Average Estimate:** Determine the average estimated value (using the midpoint between "low" and "high") for all artworks in the auction. Store this calculated value as a new property called "averageEstimate" within the main "auction" object.



