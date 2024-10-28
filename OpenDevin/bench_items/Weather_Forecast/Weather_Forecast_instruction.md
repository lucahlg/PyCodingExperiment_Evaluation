# Weather Data Modification

## Objective:
This exercise aims to familiarize you with manipulating JSON data structures by modifying and adding information to a weather report.

## Exercise Instructions:

You are provided with a JSON file containing weather data for a specific location and date. Your tasks are as follows:

1. **Add a "feels_like" temperature:** 
   -  Insert a new property called `"feels_like"` within the main JSON object.
   -  This property should also be an object with the structure: `{"unit": "C", "value": integer}`. Set the "value" to 12 degrees Celsius.

2. **Update the wind direction:** Change the `"direction"` of the `"wind"` object to "N".

3. **Add a precipitation property:** 
   -  Insert a new property called `"precipitation"`.
   - Set its value to `"light rain"` (as a string).

4. **Remove the pressure reading:** Delete the entire `"pressure"` property from the JSON object.


