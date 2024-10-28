#  Charger Database Management

## Objective:

The goal of this exercise is to modify and enhance a JSON database representing a collection of electronic chargers. You will be adding new chargers, updating existing information, and restructuring data for improved organization.


## Exercise Instructions:

You are provided with a JSON file containing a list of chargers. Your tasks are as follows:

1. **Add a New Charger:**  Introduce a new charger to the "chargers" array with the following specifications:
    - `"chargerType"`: "USB-C"
    - `"wattage"`: 45
    - `"numberOfPorts"`: 3
    - `"brand"`: "RavPower"
    - `"model"`: "RP-PC136"
    - `"weight"`: 0.25
    - `"dimensions"`:  
        - `"length"`: 7
        - `"width"`: 4
        - `"height"`: 2
    - `"inputVoltage"`: 110
    - `"outputVoltage"`: 5
    - `"outputCurrent"`: 9
    - `"supportedDevices"`: ["Android Phone", "Tablet"]
    - `"additionalFeatures"`: ["Quick Charge 3.0", "Foldable Prongs"]

2. **Update Charger Information:** Locate the charger with the model "PowerPort Atom III Slim" and update its "wattage" to 87.

3. **Restructure Data:** Create a new property called "chargingStandards" within each charger object. This property should be an array containing strings representing the supported charging standards (e.g., ["USB Power Delivery", "Quick Charge 3.0"]). Populate this array appropriately for all existing chargers based on their "additionalFeatures".

4. **Remove Redundant Information:** Delete the "inputVoltage" field from each charger object as it is generally not a key differentiator in charger selection.



