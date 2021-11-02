
import random
from art import logo
import os


deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card(deck):
    card = random.choice(deck)
    return card


computer_cards = [deal_card(deck), deal_card(deck)]
player_cards = [deal_card(deck), deal_card(deck)]


def check_cards(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


def play_game():
    print(logo)
    computer_cards = [deal_card(deck), deal_card(deck)]
    player_cards = [deal_card(deck), deal_card(deck)]
    is_game_over = False

    while not is_game_over:
        player_score = check_cards(player_cards)
        computer_score = check_cards(computer_cards)
        print(f"   Your cards: {player_cards}, current score: {player_cards}")
        print(f"   Computer's first card: {computer_cards[0]}")
        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                player_cards.append(deal_card(deck))
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(deck))
        computer_score = check_cards(computer_cards)

    print(f"   Your final hand: {player_cards}, final score: {player_score}")
    print(
        f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
