# Analyze and Modify a Travel Reservation

## Objective:

The goal of this exercise is to analyze and modify a travel reservation JSON object. You will extract specific information, update existing details, and add new information based on the provided structure.

## Exercise Instructions:


1. **Extract Traveler Details:** Extract the following traveler details from the JSON object:
    - Full name: Combine "customerName" from the "customer" object with the reservation confirmation number ("reservationConfirmation").  Store these values as a single string in a variable called `travelerName`.

2. **Update Activity Price:** The price of the Grand Canyon Helicopter Tour has increased. Update the `"activityPrice"` within the `"travelActivity"` object to 219.99.

3. **Add Payment Information:** Add a new property called `"paymentMethod"` to the top level of the JSON object. Assign it a string value of "Credit Card".

4. **Modify Availability:** The tour operator has decided to stop offering tours on Sundays. Remove "Sunday" from the `"activityAvailability"` list within the `"travelActivity"` object.
5. **Extract Location Details:** Extract the following location details from the `"travelActivity"` object and store them in separate variables:

    - `locationName`: The name of the location.
    - `addressLine1`: The first line of the address for the location.



