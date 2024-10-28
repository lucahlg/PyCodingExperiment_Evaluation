#  Product Presentation: Data Analysis and Modification

## Objective:

This exercise focuses on analyzing and modifying a JSON object representing data for a product launch event. You will be asked to extract information, add new entries, and restructure parts of the JSON data.


## Exercise Instructions:

You are provided with a JSON file containing details about a product launch event. Your tasks are as follows:

1. **Extract attendee information:** Create a new list called "attendeeEmails" that contains only the email addresses of all attendees from the "attendees" array.
2. **Add a new product:** Append a new product to the "products" array with the following details:
    - "name": "Product C"
    - "description": "An innovative solution for all your needs."
    - "price": {"amount": 49.99, "currency": "USD"}
3. **Modify revenue:** Update the "revenue" object within the "business" section to reflect a 10% increase in revenue. Calculate the new amount and store it in the "amount" field while keeping the "currency" as "USD".
4. **Restructure attendee information:** Move the "phoneNumber" field from each attendee object into a nested object called "contactInfo". The "contactInfo" object should contain both the "phoneNumber" and the "email" fields.



