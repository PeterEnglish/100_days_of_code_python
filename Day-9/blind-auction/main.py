
from art import logo

print(logo)

bids = {}
bidding_finished = False
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clearConsole()


def find_highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_records:
        amount = bidding_records[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    will_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if will_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif will_continue == "yes":
        clearConsole()


