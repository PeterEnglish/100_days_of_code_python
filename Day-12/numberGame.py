import random
import os
num_lives = 0
difficulty = "easy"
levels={'easy':10, 'hard':5}
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def get_num_lives():
    global num_lives
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if (difficulty != 'hard'):
        difficulty='easy'
    num_lives = levels[difficulty]
    print(f"You have {num_lives} atttempts remaining to guess the number")

def compare_guesses(number):
    global num_lives
    while num_lives!=0:
    
        guess = int(input("Make a guess: "))
        if guess>number:
            print("Too high")
            num_lives -=1
        elif guess<number:
            print("Too low")
            num_lives -=1
        else:
            print(f"Congratulations, the number was {guess}! You are correct!")
            break
    if num_lives==0:
        print("You have ran out of guesses! Sorry, but you lost the game!") 

def get_random_number():
    return random.randint(1,101)

def ask_to_play_again():
    play_again = input("Do you want to play again? y or n:")
    if play_again == 'y':
        clear()
        play_game()
    else:
        exit()

def play_game():
    global num_lives
    number = get_random_number()
    print("Welcome to the Number Guessing Game!")
    get_num_lives()
    compare_guesses(number)    
    ask_to_play_again()
   


play_game()