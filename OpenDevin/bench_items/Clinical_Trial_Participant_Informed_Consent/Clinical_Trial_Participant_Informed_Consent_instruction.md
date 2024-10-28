# Consent Form Modification Exercise

## Objective: 

This exercise focuses on modifying and restructuring information within a JSON object representing a consent form for a medical study. You will be asked to update participant details, add new study information, and restructure parts of the JSON for better organization.


## Exercise Instructions:

You are provided with a JSON file containing the consent form for a participant in a clinical trial. Your tasks are as follows:

1. **Update Participant Information:** Change the participant's name to "John Doe".  Ensure all other participant details remain accurate.
2. **Add Study Location:** Include a new location, "Small Town Clinic", to the list of study locations within the "study" object. 
3. **Refactor Contact Information:** Move the contact information (address, phoneNumber, emailAddress) for the participant from within the "participant" object into its own separate object called  "contact". This "contact" object should be at the same level as "participant" and "study" within the "consent" object.
4. **Append Additional Information:** Add a new paragraph to the "additionalInformation" field stating: *"The participant has been informed of the potential benefits of participating in this study."* 


