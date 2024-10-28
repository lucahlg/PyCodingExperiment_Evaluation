# Modify and Restructure a Medical Appointment JSON

## Objective:
The goal of this exercise is to modify and restructure a JSON object representing a medical appointment by adding, updating, and removing fields, and reorganizing the structure.


## Exercise Instructions:

You are provided with a JSON file describing a medical appointment. Your tasks are as follows:

1. **Add patient information:**  Within the "patient" object, add a new field called "address". This field should contain a nested object with the following fields:
    - "street": "123 Main St"
    - "city": "Anytown"
    - "state": "CA" 

2. **Update appointment details:** Change the "appointmentType" to "Consultation". Update the "startTime" to "2023-03-15T14:00:00Z" and the "endTime" to "2023-03-15T15:00:00Z".

3. **Remove contact information:** Remove the entire "contactInfo" object from both the "patient" and "provider" objects.

4. **Restructure notes:** Move the "notes" field into a new object called "appointmentDetails". This object should also include two additional fields:
    - "reasonForVisit": "Follow up on chest pain"
    - "diagnosis": "" (Leave this field empty for now) 


