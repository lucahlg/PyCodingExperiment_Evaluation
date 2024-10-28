# Modify and Restructure a Meeting JSON Object

## Objective:
The goal of this exercise is to modify and restructure a JSON object representing a meeting by adding new information, updating existing details, and changing the structure.

## Exercise Instructions:

You are provided with a JSON file describing an engineering team meeting. Your tasks are as follows:


1. **Add a New Attendee:** Include a new attendee named "David Brown" with the email address "david.brown@example.com" to the  "attendees" array.
2. **Update Meeting Description:** Change the meeting description to: "Review the progress on feature X and identify potential roadblocks for the next sprint." 
3. **Add Agenda Items:** Create a new property called "agenda" within the JSON object. This property should be an array containing three strings representing agenda items:

    -  "Progress Update on Feature X"
    -  "Sprint Planning Discussion"
    -  "Open Q&A" 
4. **Remove Email Reminders:** Delete the entire "reminders" array from the JSON object. 
5. **Restructure Location Information:** Move the "name" and "address" fields of the "location" object to the top level of the JSON object, directly under the "id". The restructured JSON should look like this:

 ```json
 {
    "id": "01234567-89ab-cdef-0123-456789abcdef",
    "name": "Conference Room A",
    "address": "123 Main Street, Anytown, CA 91234",
    "title": "Engineering Team Meeting",
    // ... (rest of the JSON object)

 }
 ```



