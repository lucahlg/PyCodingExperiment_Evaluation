# Process an Order JSON Object

## Objective:

The goal of this exercise is to process and modify an order JSON object, simulating real-world e-commerce actions like adding items and updating payment information.

## Exercise Instructions:

You are provided with a JSON file representing a customer's online order. Your tasks are as follows:


1. **Add a New Item:**  Add a new item to the "items" array within the "order" object. The new item should have the following structure:
    ```json
    {
      "productId": "PROD-3", 
      "quantity": 1
    }
    ```

2. **Update Quantity:**  Increase the quantity of the product with "productId": "PROD-2" by 2.

3. **Modify Payment Information:** Change the "payment" object's "amount" to 25.50.

4. **Extract Customer Name:** Create two new variables, one for the customer's "firstName" and another for the "lastName".



