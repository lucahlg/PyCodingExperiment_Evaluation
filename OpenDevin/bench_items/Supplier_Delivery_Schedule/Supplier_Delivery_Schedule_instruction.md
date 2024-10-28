#  Modify and Analyze a Supplier Delivery Schedule

## Objective: 
This exercise aims to familiarize you with manipulating JSON data representing a supplier delivery schedule. You will add new items, update existing information, and restructure the JSON for better readability.

## Exercise Instructions:

1. **Add a New Item:**  Introduce a new item to the "items" array with the following details:
    - "itemNumber": "ITEM-003"
    - "quantity": 50
    - "unitOfMeasure": "CS"
    - "deliveryDate": "2023-03-29"

2. **Update Delivery Date:** The delivery date for "ITEM-002" has been changed to "2023-03-18". Update the corresponding "deliveryDate" field in the JSON.

3. **Separate Supplier Information:** Extract the "supplierAddress" object from its current location and place it as a new top-level property within the JSON structure, alongside "scheduleId", "supplierId", etc. This will create a more organized representation of supplier information.
4. **Calculate Total Quantity:** Add a new property called "totalQuantity" to the main JSON object. Calculate and store the sum of all item quantities in this property. 



