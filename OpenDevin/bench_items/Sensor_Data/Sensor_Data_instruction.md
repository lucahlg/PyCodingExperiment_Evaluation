# Analyze and Modify Sensor Data

## Objective: 

The goal of this exercise is to analyze and modify a JSON object containing sensor data. You will extract specific information, perform calculations, and restructure the JSON for better representation.

## Exercise Instructions:


1. **Extract Timestamp Information:** Extract the date and time from the "timestamp" field and store them as separate properties called "date" and "time" within the JSON object.  
2. **Convert to Fahrenheit:** Add a new property called "valueFahrenheit" and calculate the temperature in Fahrenheit based on the existing "value" and "unit". Use the formula: `(value * 9/5) + 32`.
3. **Remove Unnecessary Fields:** Delete the "deviceId" field from the JSON object as it is not relevant for this analysis.

4. **Restructure Location Data:** Create a nested object called "locationData" within the JSON and move the "location" field inside this new object.  The structure should look like this:
    ```json
    "locationData": {
        "room": "Living Room" 
    }
    ```



