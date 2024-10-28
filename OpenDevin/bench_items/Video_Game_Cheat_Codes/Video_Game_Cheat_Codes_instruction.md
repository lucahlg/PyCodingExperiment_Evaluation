# Video Game Cheat Code Database Modification

## Objective: 
The goal of this exercise is to modify and restructure a JSON database containing information about video game cheat codes. You will add new entries, update existing information, and change the data structure for better organization.

## Exercise Instructions:

You are provided with a JSON file representing a database of cheat codes. Your tasks are as follows:

1. **Add a New Cheat Code:** Include the following cheat code for the game "Grand Theft Auto V":
    - `code`: "tank"
    - `description`: "Spawns a tank vehicle."
    - `platform`: ["PC", "PlayStation", "Xbox"]
    - `category`: "Vehicle Spawning"
    - `requirements`: [] 
    - `disclaimer`: "This cheat code may cause instability in online play."

2. **Update Existing Information:** Modify the `description` of the cheat code `"IDKFA"` to: "Gives the player all weapons with infinite ammunition".

3. **Change Platform Structure:**  Restructure the JSON to store platform information as objects instead of arrays. For example, the "platform" field for `"IDKFA"` should become:

```json
"platform": {
    "PC": true, 
    "PlayStation": true,
    "Xbox": true 
}
```
Apply this change to all cheat codes in the database.

4. **Add a Disclaimer:** Add a new field called `"availability"` to each cheat code object. This field should be a string indicating whether the cheat code is `"active"`, `"deprecated"`, or `"experimental"`. Set the `"availability"` of `"unlockall"` to `"deprecated"`.



