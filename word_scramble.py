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
    # Remove 'pass', fill in your code here
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
    # Remove 'pass', fill in your code here
    if user_guess == secret_word:
        return True
    else:
        return False

# Task 1.3 
def get_word_progress(secret_word, user_guess):
    # Remove 'pass', fill in your code here
    letter_positions = ""
    for i in range(0, len(secret_word)):
        if user_guess[i] == secret_word[i]:
            letter_positions += user_guess[i]
        else:
            letter_positions += '*'

    return letter_positions

# Task 2.1, 2.2 
def word_scramble():
    word_list = load_words()
    # Remove 'pass', fill in your code here
    secret_word = choose_word(word_list)
    print("Welcome to Word Scramble!")
    scramble_word(secret_word)
    print("You have 5 attempts to guess the original word.")

    remaining_attempts = 5
    while remaining_attempts > 0:
        print()
        user_guess = input_check(secret_word)
        if has_player_won(secret_word, user_guess) is True:
            print(f"Congratulations! You guess the word: {user_guess}")
            return
        else:
            remaining_attempts -= 1
            print(f"Incorrect. Progress: {get_word_progress(secret_word, user_guess)}")
            print(f"Attempts left: {remaining_attempts}")

    print(f"Sorry, you ran out of guesses. The word was {secret_word}")


if __name__ == "__main__":
    word_scramble()
