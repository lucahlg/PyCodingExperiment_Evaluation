# Modify a Firewall Rule

## Objective:

This exercise focuses on modifying a firewall rule represented in JSON format to refine network security configurations.


## Exercise Instructions:

You are provided with a JSON file representing an ingress firewall rule named "Allow-Web-Traffic-from-Trusted-Network". Your tasks are as follows:

1. **Expand IP Range:** Modify the `"ipRange"`  within the `"match"` object to allow traffic from a broader range of IP addresses within the trusted network. Change it to `10.0.0.0/22`.

2. **Add Protocol Support:**  Enable support for UDP traffic in addition to TCP. Update the `"protocol"` field within the `"match"` object to an array containing both "TCP" and "UDP".

3. **Restrict Port Range:** Limit the allowed ports for web traffic. Change the `"portRange"` within the `"match"` object to `80-443`.
4. **Disable Logging:** For performance reasons, disable logging for this rule. Set the `"log"` field within the `"action"` object to `false`.


