# Insurance Policy JSON Modification Exercise

## Objective:

This exercise focuses on manipulating a JSON object representing an insurance policy. You will add new information, modify existing values, and restructure parts of the JSON to gain familiarity with working with complex data structures.

## Exercise Instructions:

You are provided with a JSON file describing an insurance policy. Your tasks are as follows:


1. **Add a New Dependent:** Add a new dependent to the "dependents" array. This new dependent should have the following information:
    - id: "b37f920a-c5d4-468e-b721-f8b05342d1c9" 
    - name: "Ethan Smith"
    - email: "ethan.smith@example.com"
    - phoneNumber: "555-345-6789"

    Ensure the address for Ethan Smith is identical to Aiden Smith's address.

2. **Update Coverage:** Modify the "deductible" of the "Dental" coverage to 400.

3. **Remove Coverage:** Delete the "Vision" coverage from the "coverages" array.


4. **Restructure Policyholder Data:** Move the "phoneNumber", "email", and "address" fields from within the "policyholder" object into a new nested object called "contactInfo" within the "policyholder" object. 

 This should result in a structure like:
 ```json
 "policyholder": {
    "id": "...",
    "name": "...",
    "contactInfo": {
        "phoneNumber": "...",
        "email": "...",
         "address": { ... }
     } 
 }
 ```

5. **Add Policy Notes:**  Create a new property called "notes" at the top level of the JSON object. Set its value to an empty string (`""`). This will be used for storing future policy-related notes.



