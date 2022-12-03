#Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
from Hangman_words import word_list

#Import the logo from hangman_art.py and print it at the start of the game.
from Hangman_art import logo
print(logo)

#Import the stages from hangman_art.py and make this error go away.
from Hangman_art import stages

#Randomly choose a word.
import random
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#while loop to let the user guess again. 

end_of_game = False

lives = 6

while not end_of_game:
    #Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()
    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    #Check if user is wrong.
    if guess not in chosen_word:
      #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
          end_of_game = True
          print("You lose!")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(stages[lives])