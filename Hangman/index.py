# *****************************************************
# Developer: Fernando Celis
# Date: 02/23/2025
# Class: CIS2131 / Python Programming
# Project: Hang Man
"""
Project Description: This script implements a classic game of Hangman.
The game randomly selects a word, and the player must guess the word one letter at a time.
The player has a total of six attempts to guess the correct word before the stick figure is fully drawn
and the game is lost. Each incorrect guess brings the player closer to defeat, while correct guesses
reveal letters in the word. The game continues until the player either successfully guesses
the word or runs out of attempts.
"""
# *****************************************************
import random

# List of words for the game
WORD_LIST = ["python", "developer", "hangman", "programming","fernando", "lego"]


def random_word():
    # Select a random word from the list.
    return random.choice(WORD_LIST)

def display(word, guessed_letters):
    # Display the word with correctly guessed letters and underscores for missing ones.
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def get_user_guess(guessed_letters):
   # Prompt user for a guess and validate input.
    while True:
        guess = input("\nEnter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha() :
            print("Invalid input! Please enter a single letter.")
        elif guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        else:
            return guess


def print_hangman(attempts):
   # Prints the hangman figure based on incorrect attempts.
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(stages[attempts])


def play_game():
    # Main function to play the game.
    word = random_word()
    guessed_letters = set()
    attempts = 0
    max_attempts = 6

    print("\n🎉 Welcome to Hangman! Try to guess the word. 🎉")

    while attempts < max_attempts:
        print_hangman(attempts)
        print("\nWord: ", display(word, guessed_letters))
        print(f"Incorrect attempts left: {max_attempts - attempts}")

        guess = get_user_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess not in word:
            attempts += 1
            print(f"Incorrect! '{guess}' is not in the word.")
        else:
            print(f"Good guess! '{guess}' is in the word.")

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word.upper())
            break
    else:
        print_hangman(attempts)
        print("\n😞 Game Over! The word was:", word.upper())


def main():
    # Main game loop with replay option.
    while True:
        play_game()
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye! 👋")
            break


if __name__ == "__main__":
    main()
