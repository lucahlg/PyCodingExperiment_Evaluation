# Analyze and Modify a Purchase Order JSON

## Objective:

This exercise aims to enhance your understanding of JSON data structures by analyzing and modifying a purchase order. You will perform various operations on the JSON object, including updating values, adding new fields, and restructuring information.

## Exercise Instructions:

You are provided with a JSON file representing a purchase order. Your tasks are as follows:

1. **Update Delivery Details:** Modify the "deliveryTerms" field to "CIF Destination".
2. **Add Warranty Information:** Add a new property called "warrantyPeriod" within the "material" object. Set its value to 2 years.
3. **Calculate Total Price:** Create a new property called "totalPrice" at the root level of the JSON. Calculate and store the total price by multiplying the "quantity" with the "amount" from the "unitPrice" object.
4. **Restructure Contact Information:** Move the contact information (name, email, phone) for both "supplier" and "buyer" into separate objects named "supplierContact" and "buyerContact" respectively within the main JSON structure. 

5. **Add Invoice Information:** Add a new object called "invoice" at the root level of the JSON. This object should contain:
    - "invoiceNumber": Set to a string "INV12345".
    - "invoiceDate": Set to a string representing the current date (YYYY-MM-DD).



