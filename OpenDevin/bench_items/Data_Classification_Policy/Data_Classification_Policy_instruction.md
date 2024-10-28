# Data Classification Policy Enhancement

## Objective: 
The goal of this exercise is to enhance a JSON-based data classification policy by adding new rules and modifying existing ones.

## Exercise Instructions:
You are provided with a JSON file representing a basic data classification policy. Your tasks are as follows:

1. **Add a New Rule:** Create a new rule that classifies any data where the "field" is "location" and the "operator" is "EQUALS" with the "value" "US" as "RESTRICTED". This rule should be added to the existing "rules" array.
2. **Modify an Existing Condition:** Change the "operator" in the second rule (the one starting with `"dataset"`) from "STARTS_WITH" to "CONTAINS". 
3. **Update a Classification:** Modify the classification for the first rule (the one starting with `"project"`)  to "INTERNAL".


