# Analyze and Modify Machine Maintenance Data

## Objective:

The goal of this exercise is to analyze and modify a JSON object representing machine maintenance data. You will extract information, add new details, and restructure parts of the JSON. 

## Exercise Instructions:


1. **Extract Information:** Extract the "maintenanceDate" from the JSON object and store it in a separate variable.

2. **Add New Details:**  
    - Add a new property called "nextScheduledMaintenance" to the JSON object. Set its value to a date string representing the next scheduled maintenance date (e.g., "2023-06-15"). 
    - Append a new attachment to the "attachments" array with the following details:
        - "attachmentName": "Machine Performance Log"
        - "attachmentType": "CSV"
        - "attachmentUrl": "https://example.com/machine-performance-log.csv"

3. **Restructure Data:** Move the "performedBy" property into a nested object called "maintenancePersonnel". The "maintenancePersonnel" object should have the structure: 
    ```json
    "maintenancePersonnel": {
        "name": "John Smith"
    }
    ```

4. **Calculate Total Cost:** Calculate the total maintenance cost by adding the "maintenanceCost" to a hypothetical parts cost of $50. Store the result in a variable called "totalMaintenanceCost".



