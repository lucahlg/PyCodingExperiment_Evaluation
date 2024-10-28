# Analyzing Medical Equipment Calibration Records

## Objective:

This exercise focuses on manipulating and extracting information from a JSON file containing medical equipment calibration records. You will be tasked with modifying the data structure and adding new calibration entries.

## Exercise Instructions:

You are provided with a JSON file representing calibration records for various pieces of medical equipment. Your tasks are as follows:

1. **Add New Calibration Entry:** For the "X-Ray Machine" (equipmentId: "EQ1234"), add a new entry to the `equipmentCalibrationHistory` array representing a calibration performed on  "2023-10-26" by technician "Emily Chen". The calibration status should be "Calibration Complete", and the notes should state "Routine calibration performed successfully."

2. **Update Calibration Status:** Change the `calibrationStatus` of the MRI machine (equipmentId: "EQ5678")'s existing calibration entry to "Calibration Scheduled" instead of "Needs Calibration".

3. **Extract Data:** Write code that extracts and prints the following information for each piece of equipment in the JSON file:
    - Equipment Name
    - Calibration Interval
    - The date of the most recent successful calibration (Calibration Complete status)


