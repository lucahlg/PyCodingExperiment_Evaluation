# Modifying a Scrap Disposition Plan

## Objective:

This exercise focuses on manipulating and restructuring data within a JSON object representing a scrap disposition plan.  You will add new information, update existing details, and reorganize the structure for clarity and usability.

## Exercise Instructions:

1. **Add a New Material:** Include a new material type in the "materials" array. The new material should be named "Aluminum" with the description "A lightweight and recyclable metal." 
2. **Update Process Description:** Modify the description of the "Recycling" process within the "processes" array to include more detail:  "The process of transforming waste materials into reusable objects, reducing environmental impact by conserving resources."
3. **Add a New Responsible Party:** Introduce a new responsible party to handle specific aspects of the plan. Include:

    - Name: "XYZ Recycling"
    - Contact Information:
        - Name: "Sarah Jones"
        - Email: "sarah.jones@example.com"
        - Phone: "555-987-6543"
4. **Restructure Location:** Move the "location" data into a dedicated object named "facility".  The structure should be:

    ```json
    "facility": { 
      "name": "Anytown Facility",
      "address": {
          "streetAddress": "123 Main Street",
          "city": "Anytown",
          "state": "CA",
          "zipCode": "12345"
      }
    } 
    ```

5. **Remove Timestamps:** Delete the  "createdAt", "createdBy", "updatedAt", and "updatedBy" fields as they are not essential for the plan's core information.



