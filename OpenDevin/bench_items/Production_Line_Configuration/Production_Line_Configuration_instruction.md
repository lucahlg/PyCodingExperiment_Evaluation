# Automate Production Line Optimization

## Objective:

This exercise focuses on manipulating a JSON representation of a production line configuration to enhance efficiency and traceability. 

## Exercise Instructions:

1. **Add Material Tracking:**  Insert a new property called "materialTrackingId" into each station configuration object within the "stationConfigurations" array. Assign a unique identifier (e.g., a UUID) for each station's material tracking.


2. **Update Station Output:** Modify the outputMaterialId of the "Packaging Station 1".  Change it to "f45e9c3d-8a7b-4b60-9285-321a7b07fb3e".

3. **Rename Inspection Station:** Update the "name" property of the inspection station (station with id: "a84c534e-6b37-4756-a098-0629042562be") to "Quality Control Station 1".

4. **Document Input Materials:** For each station, add a new property named "inputMaterialNames" which is an array. This array should contain the names of the materials corresponding to each "inputMaterialId". You will need to reference external data (not provided in this JSON) to map material IDs to their names.

5. **Remove Unused IDs:** Delete the  "productionLineTypeId" field from the main object as it is not relevant for further processing.



