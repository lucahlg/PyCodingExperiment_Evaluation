#  Managing Software Updates:

## Objective:

The goal of this exercise is to practice manipulating a JSON object representing software updates by adding, updating, and restructuring data.

## Exercise Instructions:

You are provided with a JSON file containing information about two software updates. Your tasks are as follows:

1. **Add a New Update:** Add a new update to the "softwareUpdates" array. The new update should have the following properties:
    -  `id`: "SU003"
    -  `title`: "Bug Fix for Package C"
    -  `description`: "This update fixes a bug that was causing crashes in Package C."
    -  `status`: "published"
    -  `releaseDate`: "2023-04-26"
    -  `softwarePackage`: 
        - `name`: "Package C"
        - `description`: "Package C is a graphics editing tool"
        - `version`: "1.2.0"
        - `publisher`: "Open Source Graphics"

2. **Change Update Status:** Update the status of the update with the ID "SU002" to "published".

3. **Extract Package Information:** Create a new array called "packageInformation" at the top level of the JSON object. This array should contain objects representing information about each software package mentioned in the updates. Each object should have the following structure:
    - `name`:  (The name of the software package)
    - `description`: (The description of the software package)
    - `version`: (The version of the software package)

4. **Remove Release Date:** Remove the "releaseDate" property from all update objects in the "softwareUpdates" array. 



