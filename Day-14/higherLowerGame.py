import random
from game_data import data
from art import logo


def get_random_datum():
    selection = random.randint(0, len(data)-1)
    return data.pop(selection)

def compare_datum(person1, person2):
    print(f"{person1['name']} has {person1['follower_count']}, whereas {person2['name']} has {person2['follower_count']}")
    if person1['follower_count'] > person2['follower_count']:
        print("You are correct!")
        return True
    else:
        print("You are incorrrect!")
        return False
    

def ask_question(person1, person2):
    print("")
    print(f"Does {person1['name']}, a {person1['description']} from {person1['country']}")
    print("Have more follows than:")
    print(f"{person2['name']}, a {person2['description']} from {person2['country']}")
    answer = ""
    while not answer in ['y', 'n']:
        answer = input("Type 'y' for yes, and 'n' for no: ").lower()
    if answer == 'y':
        result = compare_datum(person1, person2)
    else:
        result = compare_datum(person2, person1)
    return result

def play_game(person1, person2, score):
    result = ask_question(person1, person2)
    if result:
        score+=1
        print(f"Your score: {score}")
        play_game(person2, get_random_datum(), score)
    else:
        print(f"Game over! Your score was {score}")

print(logo)
print("Welcome to Insta-Higher lower, where you choose the account that has higher or lower likes!")
play_game(get_random_datum(), get_random_datum(), 0)