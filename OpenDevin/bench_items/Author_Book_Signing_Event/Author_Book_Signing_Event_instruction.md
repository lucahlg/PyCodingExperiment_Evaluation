#  Book Club Meeting JSON Manipulation

## Objective:
This exercise aims to familiarize you with manipulating and restructuring data within a complex JSON object. You will be adding, modifying, and rearranging information related to a book club meeting.

## Exercise Instructions:

You are provided with a JSON file detailing a Book Club meeting. Your tasks are as follows:

1. **Add Discussion Points:** Create a new property called "discussionPoints" within the main JSON object. This property should be an array containing three strings representing potential discussion topics for "The Great Gatsby". For example:
    -  "Gatsby's portrayal of the American Dream"
    - "The significance of symbolism in the novel"
    - "Character analysis of Daisy Buchanan"

2. **Update Meeting Details:** The meeting has been rescheduled. Change the "startDate" to "2023-03-15" and the "endDate" to "2023-03-15".  

3. **Refactor Author Information:** Move the author information for F. Scott Fitzgerald from within the "book" object into a new top-level property called "authorBiography". This property should contain the same data as the existing "author" object inside the "book". Remove the original "author" object within "book".

4. **Add Venue Contact Information:** Create a new property called "venueContact" within the "venue" object. This property should be an object with the following fields:
    - "phoneNumber": "555-123-4567"
    - "email": "centrallibrary@example.com" 



