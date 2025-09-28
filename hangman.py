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

    guess_count = 0
    is_playing = True
    while is_playing:
        print(hangman_images[guess_count])
        print(correct_letters)
        print(f"You have guessed the following letters: {guessed_letters}")

        #Get a guess
        guessed_letter = input("\nGuess a letter: ").lower()
        while guessed_letter in guessed_letters:
            print("You've already guessed that letter!")
            guessed_letter = input("Guess a letter: ").lower()
        guessed_letters.append(guessed_letter)

        #Correct guess!
        if guessed_letter in correct_answer:
            print(f"\nCorrect! The letter {guessed_letter} is in the word!")
            for i in range(len(correct_answer)):
                if guessed_letter == correct_answer[i]:
                    correct_letters[i] = guessed_letter
        #Wrong guess!
        else:
            print(f"\nOuch!  The letter {guessed_letter} is not in the word!")
            guess_count += 1

        #Win or Lose Conditions
        if correct_letters == correct_answer:
            print("Congratulations!  You win!")
            print(f"The word was {correct_answer}")
            is_playing = False
        elif guess_count == len(hangman_images) - 1:
            print(hangman_images[guess_count])
            print("YOU LOSE!")
            print(f"The word was {correct_answer}")
            is_playing = False

    #Run again?
    choice = input("\nWould you like to run the program again (y/n): ").lower()
    if choice.startswith("n"):
        is_running = False

print("\nThank you for playing HANGMAN.")    