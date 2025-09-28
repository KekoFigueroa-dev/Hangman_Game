# Hangman Game
import random

hangman_images =[
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

#Print welcome message
print("Welcome to my Hangman Game!")
# Set up a list of possible words
word_list = ["python", "hangman", "challenge", "programming", "developer", "function", "variable", "iteration", "condition", "loop"]
is_running = True
#Randomly select a word for the player to guess
chosen_word = random.choice(word_list)
while is_running:
    correct_answer = list(random.choice(word_list))
    correct_letters = []
    guessed_letters = []
    for letter in correct_answer:
        correct_letters.append("_")
    #Debug
    print(f"Correct Answer: {correct_answer}")
    print(f"Current Correct Letters: {correct_letters}")
    input()

# 5. While the word is not gauessed and attempts remain:
    # a. Show current word state (with blanks for unguessed letters)
    # b. Show guessed letters and remaining attempts
    # c. Get user input for a letter guess
    # d. Validate input (single letter, not already guessed)
    # e. Update guessed letters and attempts
    # f. Reveal letters in word if guess is correct

# 6. If word is guessed, print win message
# 7. If attempts run out, print loss message and reveal word