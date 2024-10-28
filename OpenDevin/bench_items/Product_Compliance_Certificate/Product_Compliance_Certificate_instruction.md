#  Product Certification Data Manipulation

## Objective:
This exercise focuses on modifying and restructuring a JSON object representing product certification data. You will add, update, and remove properties, as well as restructure parts of the JSON to reflect changes in information.

## Exercise Instructions:

You are provided with a JSON file detailing a product certificate. Your tasks are as follows:

1. **Add a new Attachment:**  Include a link to a supplementary document explaining the testing procedures used for certification: `"https://example.com/testing-procedures.pdf"` under the "attachments" array. 
2. **Update Certificate Status:** The certificate has been renewed. Update the "status" to "renewed".
3. **Modify Expiration Date:**  Extend the certificate's validity by one year. Change the "expirationDate" accordingly.
4. **Remove Notes:** Delete the "notes" property as it is considered outdated and unnecessary for this version of the certificate.
5. **Restructure Product Information:**  Instead of listing products within a string in the "notes" field, create a new array called `"certifiedProducts"` directly under the main object. Populate this array with individual strings representing each certified product:

    ```json
    "certifiedProducts": [
        "Product A",
        "Product B",
        "Product C"
    ]
    ``` 



