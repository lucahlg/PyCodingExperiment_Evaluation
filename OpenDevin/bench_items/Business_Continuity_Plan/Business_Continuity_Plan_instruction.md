# Modify a Business Continuity Plan JSON

## Objective:

The goal of this exercise is to modify and restructure parts of a JSON object representing a Business Continuity Plan. You will add new components, update existing information, and restructure data within the plan. 

## Exercise Instructions:

You are provided with a JSON file describing a Business Continuity Plan. Your tasks are as follows:


1. **Add a New Component:** Insert a new component called "Recovery"  after the existing "Detection" component. This new component should have:
    * `componentId`: "00000000-0000-0000-0000-000000000007"
    * `componentName`: "Recovery"
    * `componentDescription`:  "This component focuses on restoring business operations following a disruption." 
    * `componentType`: "Recovery"
    * `componentObjectives`: An array containing the following objectives:
        * "Restore critical business functions within a defined timeframe."
        * "Minimize data loss and downtime."
        * "Communicate effectively with stakeholders during the recovery process."

2. **Update Action Status:** Find the action with `actionId` "00000000-0000-0000-0000-000000000003" (Implement security controls) and change its `actionStatus` to "Completed".

3. **Restructure Plan Objectives:** Move the objective "Protect the company's reputation and brand." from the `planObjectives` array to a new field called `reputationalObjective` within the main JSON object.



