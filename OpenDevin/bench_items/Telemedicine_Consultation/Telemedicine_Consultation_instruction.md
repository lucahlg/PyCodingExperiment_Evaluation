## Exercise: Medical Consultation Analysis and Update

**Objective:**

The goal of this exercise is to analyze, modify, and extend a JSON object representing a medical consultation record. You will be tasked with adding new information, updating existing data points, and restructuring parts of the JSON to reflect real-world scenarios in healthcare data management.

**Exercise Instructions:**


1. **Add Diagnostic Information:** Create a new property called "diagnosis" within the "consultation" object. This property should be an array that can hold multiple diagnoses related to the consultation. Add the following diagnosis:
    *  `{"code": "I10", "description": "Essential (primary) hypertension"}` 

2. **Update Prescription Details:** Modify the existing prescription information within the "prescription" array. Specifically, for the "Lisinopril" entry, update the "dosage" to "20 mg".
3. **Record Vital Signs:** Add a new property called "vitalSigns" within the "consultation" object. This property should be an object containing key-value pairs representing vital signs measured during the consultation:
    * `"bloodPressure": {"systolic": 125, "diastolic": 75}`,
    * `"heartRate": 72`,
    * `"temperature": 98.6`

4. **Create a Referral:** Add a new referral to the "referrals" array within the "consultation" object. The referral should be for a specialist in nephrology (kidney doctor) with the following details:

```json
{
  "specialty": "Nephrology",
  "providerName": "Dr. Robert Jones" 
}
```

5. **Mark Consultation for Review:** Change the status of the consultation from "completed" to "needsReview".



