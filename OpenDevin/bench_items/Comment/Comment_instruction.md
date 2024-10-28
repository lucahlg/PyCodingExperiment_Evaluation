# Manipulate a Blog Comment JSON

## Objective: 

This exercise aims to familiarize you with manipulating and restructuring nested JSON data. You'll be modifying a JSON object representing a blog comment and its associated information.

## Exercise Instructions:

You are provided with a JSON file containing data about a blog post comment. Your tasks are as follows:


1. **Extract User Information:** Create a new JSON object named "commenter" that contains only the following fields from the "likes" array:
    * `id`: The user ID of the commenter
    * `name`:  The name of the commenter
    * `email`: The email address of the commenter

2. **Update Comment Content:** Change the content of the comment to: "Great post, Aiden! I'm looking forward to reading more of your insights." 

3. **Remove Redundant Data:** Delete the entire "post" field from the JSON object.

4. **Add Timestamp:** Add a new property named "created_at" to the main JSON object and set its value to the current date and time in ISO 8601 format (YYYY-MM-DDTHH:mm:ss.sssZ).


