Instructions

**Creating a Tabletop Role-Playing Game Character**

In this assignment, you will write a Python program that guides the user through creating a character for a Tabletop Role-Playing Game (RPG) and performing basic actions inspired by D&D 5e mechanics.

1. **Function `get_name()`:** Write a function named `get_name()` that asks the user to enter their character's name and returns the result.
    
2. **Function `sum_of_four_six_sided_dice_with_lowest_dropped()`:** Write a function named `sum_of_four_six_sided_dice_with_lowest_dropped()` that generates 4 random numbers between 1 and 6, and returns the sum of the largest 3 of them. Use this function to assign values to the following 6 variables: `strength`, `dexterity`, `constitution`, `intelligence`, `wisdom`, and `charisma`.
    
3. **Function `get_ability_modifier()`:** Write a function named `get_ability_modifier` that accepts a value for an ability score and returns the correct modifier according to the table provided [here](https://roll20.net/compendium/dnd5e/Ability%20Scores#content). Note that the values will range from 3 to 18.
    
4. **Function `menu()`:** Write a function named `menu()` that prompts the user to enter an action from a predefined list (`Attack`, `Negotiate`, `Search`, and `Eat`) and returns their choice.
    
5. **Action Functions:**
    
    - If the user chooses `Attack`, roll a 20-sided die and add their better ability modifier score from strength or dexterity. If the total is greater than or equal to 12, tell them they hit. Otherwise, they miss. If they hit, roll a 6-sided die and add their ability modifier to calculate the total damage and display the result. Do not go below 0 for damage.
    - If the user chooses `Negotiate`, roll a 20-sided die and add their charisma modifier score. If the total is greater than or equal to 15, tell them they successfully negotiated a truce.
    - If the user chooses `Search`, roll a 20-sided die and add their better ability modifier score from intelligence or wisdom. If the total is greater than or equal to 12, tell them they found treasure; otherwise, they find nothing. If they find treasure, use a function that returns the name of some random treasure i.e. treasures = ["gems", "gold", "jade figurine", "other type"] 
    - If the user chooses `Eat`, tell them their food was rancid. Roll a 20-sided die and add their constitution ability modifier. If the total is greater than or equal to 10, tell them they were able to handle the rancid food without getting sick; otherwise, tell them they got sick and need to stay in bed.
6. **Perform Actions:** Allow the user to choose an action from the menu 4 times, displaying the results each time.