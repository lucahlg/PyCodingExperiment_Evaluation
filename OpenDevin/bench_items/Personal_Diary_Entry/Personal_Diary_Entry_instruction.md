# Enhance Your Day Diary

## Objective:

The goal of this exercise is to modify and extend a JSON object representing a diary entry. You will be adding new information, updating existing entries, and restructuring some data.

## Exercise Instructions:

You are provided with a JSON file representing a diary entry for a particular day. 
Your tasks are as follows:

1. **Add an Emotion:**  Include the emotion "Excitement" in the "emotions" array.
2. **Update Event Description:** Change the description of the "Went to the zoo" event to: "Saw giraffes, elephants, and monkeys up close! It was incredible." 
3. **New Event:** Add a new event to the "events" array with the following details:

    -  `name`: "Watched a movie"
    - `description`: "Enjoyed a funny comedy with friends."
    - `location`: "Home Theater"
    - `date`: "2023-03-08"
4. **Restructure People:** Move the "people" array into a new object called "companions". The structure should be:

```json
"companions": {
  "friends": [
    {"name": "Sarah", "relationship": "Friend"},
    {"name": "John", "relationship": "Friend"}
  ]
} 
``` 



