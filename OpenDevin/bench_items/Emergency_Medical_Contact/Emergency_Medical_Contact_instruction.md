# Normalize a Contact JSON Object

## Objective:
The goal of this exercise is to normalize the provided contact JSON object by splitting nested data into separate objects and creating consistent naming conventions.

## Exercise Instructions:

You are provided with a JSON file representing a contact. Your tasks are as follows:

1. **Separate Name Components:** Extract the "firstName", "lastName", "middleName", and "suffix" from the "name" object and create individual properties for each at the top level of the JSON object. Remove the original "name" object.
2. **Rename Properties:** Rename the following properties to be more descriptive: 
    - "relationship" to "familyRelationship"
3. **Split Contact Information:** Move the "phoneNumber", "emailAddress", and "address" data into separate objects named "phone", "email", and "address" respectively, at the same level as "familyRelationship".  
4. **Standardize Address:** Ensure all address fields are lowercase: "streetAddress", "city", "state", and "zipCode".



