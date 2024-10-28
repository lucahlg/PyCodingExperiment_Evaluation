# Analyzing and Modifying a Benefits Package

## Objective:

This exercise focuses on manipulating JSON data to understand and modify a benefits package structure. You will add new benefits, adjust existing ones, and calculate the total cost of the package.


## Exercise Instructions:

You are provided with a JSON file representing a company's benefits package. Your tasks are as follows:

1. **Add a New Benefit:** Introduce a new benefit called "Flexible Spending Account (FSA)" to the "benefits" array.  
    - Set its `description` to "Allows pre-tax contributions for healthcare and dependent care expenses." 
    - Assign a `cost` of 20.
    - Set its `coverage` type to "FSA".

2. **Update an Existing Benefit:** The cost of Dental Insurance has increased. Update the `cost` of the "Dental Insurance" benefit to 60.

3. **Calculate Total Cost:** After the modifications in steps 1 and 2, calculate the new total cost of the benefits package and update the `"cost"` field accordingly.

4. **Remove a Benefit:** Remove the "Retirement Savings Plan" benefit from the "benefits" array as it is no longer being offered by the company.

5. **Update Coverage Description:** Modify the description for the "coverage" field outside the "benefits" array to:  "Comprehensive coverage including basic medical, dental, vision, and disability benefits."



