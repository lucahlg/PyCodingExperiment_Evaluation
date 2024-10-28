# TV Show Data Manipulation

## Objective:

This exercise focuses on manipulating and restructuring data within a JSON array representing information about TV shows. You will add new properties, update existing values, and modify the structure of the JSON to gain experience with common data manipulation tasks.

## Exercise Instructions:

You are provided with a JSON file containing an array of TV show objects. Your tasks are as follows:

1. **Add 'Premiere Date':** Add a new property called "premiereDate" to each TV show object. The value for this property should be a string representing the year the show premiered (e.g., "2005", "2011").  
    - For "The Office": premiereDate = "2005"
    - For "Game of Thrones": premiereDate = "2011" 
    - For "Breaking Bad": premiereDate = "2008"

2. **Update 'numberOfSeasons':** Increase the "numberOfSeasons" for "Game of Thrones" by 1 (it had a spin-off series).

3. **Add 'Lead Actors':** Create a new property called "leadActors" in each TV show object. This property should be an array of strings, listing the names of the main actors.
    - For "The Office": leadActors = ["Steve Carell", "Rainn Wilson", "John Krasinski"] 
    - For "Game of Thrones": leadActors = ["Emilia Clarke", "Peter Dinklage", "Kit Harington"]
    - For "Breaking Bad": leadActors = ["Bryan Cranston", "Aaron Paul"]

4. **Remove 'ratings':** Delete the entire "ratings" property from each TV show object.



