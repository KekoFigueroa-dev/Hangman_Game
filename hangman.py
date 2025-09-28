# Hangman Game - Guess the word before the hangman is complete

import random

# Hangman images for each incorrect guess
hangman_images = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Welcome message
print("Welcome to my Hangman Game!")

# Expanded word list for more variety
word_list = [
    "python", "hangman", "challenge", "programming", "developer", "function", "variable", "iteration", "condition", "loop",
    "algorithm", "syntax", "exception", "inheritance", "object", "class", "method", "parameter", "argument", "recursion",
    "dictionary", "string", "integer", "boolean", "float", "list", "tuple", "set", "module", "package", "import",
    "lambda", "comprehension", "debugging", "statement", "operator", "expression", "index", "slice", "mutable", "immutable"
]

is_running = True

while is_running:
    # Select a random word and initialize game state
    correct_answer = list(random.choice(word_list))
    correct_letters = ["_"] * len(correct_answer)
    guessed_letters = []

    # Uncomment for debugging:
    # print(f"Correct Answer: {''.join(correct_answer)}")

    guess_count = 0
    is_playing = True

    while is_playing:
        # Show hangman image and current word progress
        print(hangman_images[guess_count])
        print(" ".join(correct_letters))
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Get a valid letter guess from user
        guessed_letter = input("\nGuess a letter: ").lower()
        while not (guessed_letter.isalpha() and len(guessed_letter) == 1) or guessed_letter in guessed_letters:
            if guessed_letter in guessed_letters:
                print("You've already guessed that letter!")
            else:
                print("Please enter a single alphabetic character.")
            guessed_letter = input("Guess a letter: ").lower()
        guessed_letters.append(guessed_letter)

        # Update state if guess is correct
        if guessed_letter in correct_answer:
            print(f"\nCorrect! The letter {guessed_letter} is in the word!")
            for i in range(len(correct_answer)):
                if guessed_letter == correct_answer[i]:
                    correct_letters[i] = guessed_letter
        # Update state if guess is incorrect
        else:
            print(f"\nOuch! The letter {guessed_letter} is not in the word!")
            guess_count += 1

        # Win condition: all letters guessed
        if correct_letters == correct_answer:
            print("Congratulations! You win!")
            print(f"The word was {''.join(correct_answer)}")
            print(r"""
      \O/
       |
      / \
   The hangman walks free!
    """)
            is_playing = False
        # Lose condition: hangman complete
        elif guess_count == len(hangman_images) - 1:
            print(hangman_images[guess_count])
            print("YOU LOSE!")
            print(f"The word was {''.join(correct_answer)}")
            is_playing = False

    # Prompt to play again
    choice = input("\nWould you like to run the program again (y/n): ").lower()
    if choice.startswith("n"):
        is_running = False

print("\nThank you for playing HANGMAN.")