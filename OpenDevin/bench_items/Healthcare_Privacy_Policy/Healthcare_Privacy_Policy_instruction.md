# Healthcare Policy Modification Exercise

## Objective: 
This exercise aims to familiarize you with manipulating and modifying complex JSON structures. You will update an existing healthcare privacy policy document represented in JSON format, adding new provisions and adjusting existing ones.

## Exercise Instructions:

1. **Add a New Provision:**  Within the "policies" array, locate the policy with the ID "policy-1". Add a new provision to this policy's "provisions" array with the following details:

   - **id**: "provision-3"
   - **name**: "Data Security"
   - **description**: "Acme Hospital will implement appropriate administrative, technical, and physical safeguards to protect patient protected health information (PHI)."
   - **type**: "Security"
   - **requirements**: 

     * "All PHI must be encrypted at rest and in transit."
     * "Access to PHI must be restricted to authorized personnel only."
     * "Regular security audits must be conducted to ensure compliance with data protection policies."

2.  **Update an Existing Requirement:** Modify the requirement list within "provision-2" (Consent) of the same policy ("policy-1"). Add a new requirement:

    * "Patients have the right to revoke their consent at any time."

3. **Remove an Exception:** Delete the "exceptions" array entirely from the policy with the ID "policy-1".



