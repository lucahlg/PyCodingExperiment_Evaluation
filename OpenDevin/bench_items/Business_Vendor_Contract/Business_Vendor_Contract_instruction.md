# Analyze and Modify a Contract JSON

## Objective:
The goal of this exercise is to analyze and modify a JSON object representing a contract. This will involve extracting information, updating values, and adding new details to the contract data.

## Exercise Instructions:

You are provided with a JSON file containing detailed information about a contract. Your tasks are as follows:

1. **Extract Contract Details:**
   - Identify and store the "contractNumber" and "contractDate" from the JSON object. 
2. **Update Product Information:**
    - Locate "Product B" within the "products" array. Change its "quantity" to 8.
3. **Add a New Product:**
  - Append a new product to the "products" array with the following details:
      - "name": "Product C"
      - "description": "A fantastic new addition!"
      - "unitPrice": {"amount": 15.0, "currency": "USD"}
      - "quantity": 3
4. **Calculate Updated Total Contract Value:**

   - After the product updates, recalculate and update the "totalContractValue" within the JSON object. Ensure you correctly sum the values of all products considering their updated quantities and unit prices.



