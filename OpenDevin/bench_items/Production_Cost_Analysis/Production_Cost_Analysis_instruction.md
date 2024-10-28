# Analyzing Production Costs

## Objective:
The goal of this exercise is to gain insights into the production costs associated with a specific product by manipulating and analyzing data within a JSON object.

## Exercise Instructions:

You are provided with a JSON file containing detailed information about the production of a product. Your tasks are as follows:

1. **Calculate Total Direct Costs:** Add a new property called "totalDirectCosts" to the JSON object. This property should store the sum of all direct cost components ("materialCosts", "laborCosts", and "otherDirectCosts").
2. **Determine Indirect Cost Per Unit:** Calculate the indirect cost per unit produced by dividing the total indirect costs ("rentAndUtilities", "depreciation", "otherIndirectCosts") by the "productionQuantity".  Add this value as a new property called "indirectCostPerUnit" to the JSON object.

3. **Assess Production Profitability:** Add a new property called "profitMargin" to the JSON object. Calculate this by subtracting the total direct costs and the total indirect costs from the "totalProductionCost". Divide this result by the "totalProductionCost" and multiply by 100 to express it as a percentage.



