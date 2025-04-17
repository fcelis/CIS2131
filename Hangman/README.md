Assignment: Hangman Game with Random Word Generator

#### Objective:

Create a hangman game in Python that includes the following features:

1. A loop that allows the user to play again once the game is done, if they want to.
2. A function to pick a random word from a predefined list.
3. The game should allow the user to guess a hidden word (shown as blanks) one letter at a time.
4. If the user guesses a correct letter, display that letter instead of a blank.
5. If the user guesses an incorrect letter, add to the number of body parts on the hanging man.
6. The game should end after 6 incorrect guesses or once all the letters in the hidden word have been guessed.

#### Requirements:

1. **Random Word Generator**:
    
    - Use a predefined list of words and create a function to select a random word from this list.
2. **Game Over Conditions**:
    
    - Implement a function `is_game_over(hidden_word, letters_guessed, number_of_incorrect_guesses)`to determine if the game is over (either by guessing the word correctly or making 6 incorrect guesses).
3. **User Input**:
    
    - Implement a function `ask_user_for_guess(letters_guessed)` that ensures the user can only guess a single character that hasn't been guessed already (use a validation loop).
4. **Display Hidden Word**:
    
    - Implement a function `print_hidden_word(hidden_word, letters_guessed)` to display the hidden word with guessed letters revealed and remaining letters as underscores.
5. **Display Gallows**:
    
    - Implement a function `print_gallows(number_of_body_parts)` to display the hangman gallows based on the number of incorrect guesses.
6. **Game Loop**:
    
    - The entire game should be in a loop that allows the user to play again once the game is done, if they want to.