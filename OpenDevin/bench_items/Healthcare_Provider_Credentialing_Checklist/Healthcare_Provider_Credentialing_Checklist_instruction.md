# Modify and Update a Credentialing Checklist

## Objective:
This exercise aims to familiarize you with manipulating JSON data structures by updating an existing healthcare provider credentialing checklist. You will be adding new requirements, modifying existing sections, and restructuring information within the checklist.

## Exercise Instructions:

You are provided with a JSON file representing a healthcare provider credentialing checklist.  Your tasks are as follows:

1. **Add New Requirement:** Within the "Licenses and Certifications" section ("SEC-3"), insert a new item after "DEA Registration" with the following details:
    - `itemId`: "ITEM-10"
    - `itemName`: "State Medical Board Certification"
    - `description`: "Confirmation of current certification status from the state medical board."
    - `type`: "Document"
    - `required`: true

2. **Modify Existing Section:** Rename the section "Education and Training" ("SEC-2") to "Professional Qualifications". 

3. **Restructure Information:** Move the "Social Security Number" item ("ITEM-3") from the "Personal Information" section ("SEC-1") into a new top-level field within the main checklist object. Name this field "ssn". Ensure that the "required" status for this field remains "true".

4. **Update Description:** Change the description of the checklist to:  "This checklist is used to ensure that all necessary information and documentation are collected from healthcare providers prior to granting them access to [Hospital/Facility Name] ". Replace "[Hospital/Facility Name]" with the name of your choice.



