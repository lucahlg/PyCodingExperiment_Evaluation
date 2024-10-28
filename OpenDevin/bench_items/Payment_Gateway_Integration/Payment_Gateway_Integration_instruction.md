# Secure Payment Configuration Modification

## Objective:

This exercise focuses on manipulating a JSON object representing secure payment credentials and configuration settings. 

You will practice updating sensitive information, adding new security parameters, and restructuring data within the JSON structure.


## Exercise Instructions:

1. **Update Credentials:** Replace the existing "key" and "secret" values in the "credentials" section with new placeholder values. Use "KEY_PLACEHOLDER" for the key and "SECRET_PLACEHOLDER" for the secret. 
2. **Add Two-Factor Authentication:**  Introduce a new property called "twoFactorAuth" to the root level of the JSON object. Set its value to `true`.
3. **Modify Currency:** Change the currency in the "config" section from "USD" to "EUR".
4. **Enhance Descriptor:** Within the "config" section, add a new property named "statementDescriptor" and set its value to "Acme Corp Services".
5. **Remove Provider:**  Delete the entire "provider" property from the JSON object.

