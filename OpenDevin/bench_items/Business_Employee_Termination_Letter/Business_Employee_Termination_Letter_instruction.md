# Analyzing and Modifying Employment Termination Data

## Objective:

This exercise focuses on analyzing and modifying a JSON object representing employee termination data. You will be tasked with updating information, restructuring the JSON, and adding new details to gain a better understanding of the termination process.

## Exercise Instructions:


1. **Update Employee Information:** Change Jane Doe's "position" from "Software Engineer" to "Senior Software Engineer."
2. **Restructure Termination Details:** Move the "terminationReason" field from its current location to within the "terminationDetails" object.
3. **Add Performance Review Data:** Create a new property called "performanceReviews" within the "employee" object. This property should be an array containing two objects, each representing a performance review:

    - **Review 1:**
        - "date": "2022-06-30"
        - "rating": "Needs Improvement"
        - "comments": "Areas for improvement in communication and collaboration."
    - **Review 2:**
        - "date": "2022-12-15"
        - "rating": "Below Expectations"
        - "comments": "Continued challenges in meeting project deadlines and quality standards."

4. **Add Termination Documentation:** Create a new property called "terminationDocumentation" within the main JSON object. This property should contain an array of strings representing file names of relevant termination documents (e.g., ["TerminationNotice.pdf", "PerformanceImprovementPlan.docx"]).


