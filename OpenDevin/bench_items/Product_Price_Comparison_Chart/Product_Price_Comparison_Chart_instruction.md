# Extract and Structure Product Information

## Objective:

The goal of this exercise is to extract product information from a JSON file representing a price comparison, restructure it into a new format, and save it as a separate JSON file.

## Exercise Instructions:

You are provided with a JSON file containing product details, retailers, prices, and the overall title and description for a price comparison.

Your tasks are as follows:

1. **Extract Product Data:** From the "products" array in the input JSON, extract information for each product: name, description, image URL, and link.
2. **Create New JSON Structure:** Create a new JSON object with the following structure: 
   ```json
   {
     "products": [
       {
         "name": "Product Name", 
         "description": "Product Description",
         "image": "Image URL",
         "link": "Product Link",
         "prices": [
           {
             "retailer": "Retailer Name",
             "price": Product Price
           },
           // ... additional prices for different retailers
         ]
       },
       // ... additional products
     ]
   }
   ```
3. **Populate the New Structure:** Populate the new JSON structure with the extracted product information from step 1. Match each product with its corresponding prices found in the "prices" array of the input JSON.


4. **Save as a Separate File:** Save the newly created JSON object into a separate file named "product_data.json".