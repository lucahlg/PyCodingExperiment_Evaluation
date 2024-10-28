# Modify a Customer Order JSON

## Objective:

The goal of this exercise is to modify and extend a JSON object representing a customer order. You will be adding new properties, updating existing values, and restructuring parts of the JSON.


## Exercise Instructions:

You are provided with a JSON file containing information about a customer's order. Your tasks are as follows:

1. **Add New Items:** The customer wants to add two more products to their order. Append the following product IDs to the "productIds" array:
    - "PROD9012"
    - "PROD3456"
2. **Change Delivery Frequency:** The customer has decided to receive their order every other week instead of weekly. Update the "deliveryPreference" property to reflect this change.
3. **Add Customer Name:** Add a new property called "customerName" to the JSON object and set its value to "Jane Doe".
4. **Separate Product IDs:** Extract the "productIds" array from the main JSON object and create a separate nested object called "orderDetails".  Move the "productIds" array into this new "orderDetails" object.



