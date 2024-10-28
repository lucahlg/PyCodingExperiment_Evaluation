# Wish List Management

## Objective:

This exercise focuses on manipulating a JSON object representing a wish list to reflect changes in priorities and add new items collaboratively.

## Exercise Instructions:

You are provided with a JSON file containing a wish list. Your tasks are as follows:

1. **Update Item Priority:** Change the "priority" of the "Gaming PC" item to "high".
2. **Add New Wish List Item:** Add a new item to the "items" array with the following details:
    -  "name": "Noise-Cancelling Headphones"
    -  "description": "Wireless headphones for focusing and travel."
    -  "price": 350
    -  "image": "https://example.com/headphones.jpg"
    -  "url": "https://example.com/headphones"
    -  "priority": "medium"
    -  "notes": "Need these for studying and long flights."
    -  "tags": [ "electronics", "audio"] 
3. **Remove Collaborator:** Remove "bob@example.com" from the list of "collaborators".

4. **Add Timestamps:** Add a new property called "lastEditedAt" to the main object and set its value to the current date and time in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ). This will track when the wish list was last modified.


Remember to save your changes to the JSON file after completing each step.