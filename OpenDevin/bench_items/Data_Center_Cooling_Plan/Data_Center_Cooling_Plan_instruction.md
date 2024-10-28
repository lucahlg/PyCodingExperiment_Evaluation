# Data Center Information Update

## Objective:

The goal of this exercise is to modify and update a JSON object representing information about a data center. This will involve adding new properties, changing existing values, and restructuring some parts of the JSON. 

## Exercise Instructions:

You are provided with a JSON file containing information about a data center. Your tasks are as follows:

1. **Add Power Information:** Add a new property called "power" to the top level of the JSON object. This property should be an object containing the following key-value pairs:
    - `"source": "Grid"`
    - `"capacityWatts": 20000`
2. **Update Cooling System:** Change the "type" of the cooling system from "CRAC" to "Air Handler". Update the "capacity" to 150.
3. **Modify Airflow:**  Increase the "cfm" (cubic feet per minute) value in the "airflow" object to 1200.
4. **Restructure Equipment:** Move the "equipment" array into a new object called "infrastructure". This object should also include a new property called "networkDevices" with an initial value of an empty array (`[]`).

5. **Add Notes:** Append the following sentence to the existing "notes" string:  "Data center recently underwent maintenance."



