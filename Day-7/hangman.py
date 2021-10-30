#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guessed_letter = input("Enter your choice of letter: ")
guessed_letter = guessed_letter.lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
correct = False
for char in chosen_word:
    if guessed_letter== char:
       
        break
    else:
     
    
print("YOu have guessed incorrectly. That letter is not in the word!")
 print("You have guessed correctly! The letter '" + guessed_letter + "' is in the word!")