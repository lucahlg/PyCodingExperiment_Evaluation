# Server Room Inventory Management

## Objective:

The goal of this exercise is to modify and extend a JSON object representing a server room inventory. You will be adding new servers, updating existing server details, and restructuring information for clarity.


## Exercise Instructions:

You are provided with a JSON file containing the inventory of "Server Room 1". Your tasks are as follows:

1. **Add a New Server:**  Include information about a new server named "Server 3" in the "devices" array. Specify the following details for "Server 3":
    - Manufacturer: "IBM"
    - Model: "System x3650 M6"
    - Serial Number: "5551212345"
    - Location: 
        - Room: "Server Room 1"
        - Row: 1
        - Rack: 1
        - Unit: 3
        - Position: "Front"

    - Connected Ports: ["Ethernet1", "Ethernet2"]
    - Custom Properties:
        - Operating System:  "Ubuntu Server 20.04"
        - CPU: "Intel Xeon Silver 4214"
        - Memory: "64GB DDR4"

2. **Update Existing Server:** Modify the "customProperties" of "Server 1" to reflect a memory upgrade to "256GB DDR4".

3. **Restructure Cabling Information:** Move the "cabling" information from the main object into a new nested object called "network".

   The "network" object should contain the following structure:
    ```json
    "network": {
        "type": "Ethernet",
        "cableType": "Cat6",
        "description": "All devices are connected using Cat6 Ethernet cables."
    }
    ``` 


