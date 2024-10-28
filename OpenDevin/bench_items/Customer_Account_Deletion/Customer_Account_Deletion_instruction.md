# Analyze and Modify a Customer Deletion Record

## Objective:

The goal of this exercise is to analyze and modify a JSON object representing a deleted customer record. You will be tasked with extracting information, updating existing fields, and adding new data points.

## Exercise Instructions:

You are provided with a JSON file containing details about a deleted customer account. Your tasks are as follows:

1. **Extract Information:**  Retrieve the customer's `id` and store it in a separate variable named `customerId`.
2. **Update Deletion Reason:** Change the `reason` for deletion to `"ACCOUNT_COMPROMISE"` within the `deletionDetails` object.
3. **Add Timestamp:** Add a new property called `deletionTimestamp` at the root level of the JSON object. Set its value to the current date and time in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ).
4. **Update Notes:** Append the following text to the existing `notes`:  " A full security audit was conducted on the affected system."



