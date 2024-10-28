# Software Release Note Modification

## Objective: 
This exercise focuses on modifying and restructuring JSON data representing software release notes. You will add, update, remove, and reorganize information within the provided JSON object.

## Exercise Instructions:

1. **Update Version:** Increment the "patch" version number by 1.  

2. **Add New Feature:** Include a new feature in the "features" array with the following details:
    - "name": "Enhanced User Interface"
    - "description": "A redesigned user interface for improved usability and aesthetics."

3. **Bug Fix Details:** For each bug fix in the "bugFixes" array, add a new property called "fixedInVersion". Set this property to the current software version (after the patch increment in step 1).  

4. **Known Issue Resolution:** Remove the first item from the "knownIssues" array as it has been resolved.
5. **Add Release Notes:** Add a new key-value pair at the top level of the JSON object called "releaseNotes". Set the value to a string describing any significant changes in this release, such as: "This release includes bug fixes and a new feature for an enhanced user interface experience." 



