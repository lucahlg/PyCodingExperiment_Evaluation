# Analyze and Modify a Purchase Order JSON

## Objective:
This exercise focuses on analyzing and modifying data within a purchase order JSON object. You will be tasked with calculating new values, updating existing information, and adding new details to the structure.


## Exercise Instructions:

You are provided with a JSON file representing a purchase order. Your tasks are as follows:

1. **Calculate Item Totals:** Add a "total" field within each item object in the "items" array. This field should store the product of "quantity" and "unitPrice".
2. **Update Delivery Date:** Change the "deliveryDate" to "2023-03-20T12:00:00Z".

3. **Add Shipping Information:** Create a new object named "shipping" within the main JSON object. This object should contain the following fields:
    - "method": "Ground"
    - "cost": 15.0

4. **Calculate Final Cost:** Add a new field called "finalCost" to the main JSON object.  This field should store the sum of "totalCost" and the "shipping"."cost".

