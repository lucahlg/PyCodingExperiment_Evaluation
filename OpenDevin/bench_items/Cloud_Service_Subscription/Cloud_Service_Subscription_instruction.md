# Modify and Analyze a GKE Hub Subscription JSON

## Objective:

This exercise focuses on manipulating and understanding the configuration details of a Google Kubernetes Engine (GKE) Hub subscription represented as a JSON object. You will modify existing properties, add new information, and analyze the structure to gain insights into how GKE Hub subscriptions are managed.


## Exercise Instructions:

You are provided with a JSON file representing a GKE Hub subscription. Your tasks are as follows:

1. **Update Subscription Status:** Change the "status" of the subscription to "SUSPENDED".
2. **Add Billing Information:** Create a new property called "billingInfo" within the main object. This property should be another object containing the following fields:

    - "accountNumber": "1234567890"
    - "billingCycle": "Monthly"

3. **Modify Workload Identity Configuration:** Within the "authConfig" object, update the "issuerUrl" field to a new URL: "https://updated-issuer-url.com".

4. **Add Tags:** Create a new array property called "tags" within the main object. Populate this array with two string values representing tags for the subscription: "production" and "critical".
5. **Analyze Cloud State Data:** The "cloudStateData" is currently an empty object. Describe what type of information you would expect to find in this object based on your understanding of GKE Hub subscriptions.



