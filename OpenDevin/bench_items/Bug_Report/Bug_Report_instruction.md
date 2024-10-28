# Analyze and Modify a Bug Report JSON

## Objective:

The goal of this exercise is to analyze a bug report represented in JSON format and make modifications to update its status and add new information.

## Exercise Instructions:

You are provided with a JSON file describing a bug report. Your tasks are as follows:

1. **Update the Status:** Change the "status" of the bug report from "New" to "In Progress". 
2. **Add a Comment:**  Append a new comment to the "comments" array. The new comment should be from "Jane Doe" (the assigned developer), and it should say: "Looking into the issue. Will update soon." Include the current date and time in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ) for the "date" field of this new comment.
3. **Add a New Attachment:** Add a new attachment to the "attachments" array with the following details:
    - "fileName": "ErrorLog.txt"
    - "mimeType": "text/plain"
    - "size": 54321

Remember to maintain the proper JSON structure while making these modifications. 