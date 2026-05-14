# Author: Elle Chappelle
# GitHub Username: ellechappelle
# Date: 05/13/2026
# Description: World scramble game where user has 5 attempts to guess a randomly selected sectret word from the scrampbled letters in the word



import random

# ----------------------------------------------------
# PROVIDED HELPER FUNCTIONS (DO NOT MODIFY)
# ----------------------------------------------------

def load_words(filename="words.txt"):
    """
    Loads the word list from a file and returns a list of words.
    Each word is assumed to be in lowercase.
    """
    print("Loading word list from file...")
    with open(filename, 'r') as f:
        wordlist = f.read().split()
    print(f"{len(wordlist)} words loaded")
    return wordlist

def choose_word(wordlist):
    """
    wordlist: list of strings
    returns: string, a randomly chosen word from the list
    """
    return random.choice(wordlist)

def scramble_word(secret_word):
    """
    Scrambles the letters of the given secret word and prints the scrambled version.
    Does not return anything.
    """
    letters = list(secret_word)
    random.shuffle(letters)
    scrambled = ''.join(letters)
    print(f"Scrambled word: {scrambled}")

# ----------------------------------------------------
# FUNCTIONS TO IMPLEMENT
# ----------------------------------------------------

# Task 1.1 
def input_check(secret_word):
    """
    Prompts user to enter a guess and checks if it is valid.
    Removes all non-letter characters, converts all letters to lowercase.
    Compares letters in the guess to letters in secret word using sorted().
    Repeats until user enters a valid guess.

    secret_word: string
    returns: string, the cleaned valid guess
    """
    while True:
        user_guess = input("Your guess: ")

        guess_cleaned = ""
        for letter in user_guess:
            if letter.isalpha():
               guess_cleaned += letter.lower()

        sorted_guess = sorted(guess_cleaned)
        if sorted_guess == sorted(secret_word):
            return guess_cleaned
        else:
            print("Invalid input. Please use only the letters from the secret word.")

# Task 1.2
def has_player_won(secret_word, user_guess):
    """
    Checks if the user guessed the word correctly.

    secret_word: string
    user_guess: string
    returns: boolean, True if the guess is correct, False otherwise.
    """
    if user_guess == secret_word:
        return True
    else:
        return False

# Task 1.3 
def get_word_progress(secret_word, user_guess):
    """
    Compares each letter in the user's guess to the corresponding letter in the secret word.
    If the letters are the same, adds the letter to a new string called letter_positions.
    If the letters are not the same, adds '*' to the string called letter_positions.

    secret_word: string
    user_guess: string
    returns: string, showing correctly positioned letters and '*' in the place of incorrectly positioned letters.
    """
    letter_positions = ""
    for i in range(0, len(secret_word)):
        if user_guess[i] == secret_word[i]:
            letter_positions += user_guess[i]
        else:
            letter_positions += '*'

    return letter_positions

# Task 2.1, 2.2 
def word_scramble():
    """
    Runs the Word Scramble game.
    
    Loads a list of words, randomly selects one word, and scrambles the letters in the secret word.
    Allows user 5 attempts to correctly guess the secret word.
    """
    word_list = load_words()
    secret_word = choose_word(word_list)
    print("Welcome to Word Scramble!")
    scramble_word(secret_word)
    print("You have 5 attempts to guess the original word.")

    remaining_attempts = 5
    while remaining_attempts > 0:
        print()
        user_guess = input_check(secret_word)
        if has_player_won(secret_word, user_guess):
            print(f"Congratulations! You guessed the word: {user_guess}")
            return
        else:
            remaining_attempts -= 1
            print(f"Incorrect. Progress: {get_word_progress(secret_word, user_guess)}")
            print(f"Attempts left: {remaining_attempts}")

    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


if __name__ == "__main__":
    word_scramble()
