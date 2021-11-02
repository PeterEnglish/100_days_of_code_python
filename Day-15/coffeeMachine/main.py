
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources_sufficient(beverage_choice):
    ingredients = MENU[beverage_choice]['ingredients']
    has_resources = True
    for ingredient in ingredients:
        # check if the ingredient is in the resources dict
        if ingredient in resources:
            if ingredients[ingredient] > resources[ingredient]:
                print("There is more " + ingredient + " needed than in the machine resources")
                has_resources=False
                # print(ingredient + ":" + str(ingredients[ingredient]))
                # print("We have enough " + ingredient)

    return has_resources


def take_coins(beverage_choice):
    quarters_in_cents = float(input("Number of quarters: "))*0.25
    dimes_in_cents = float(input("Number of dimes: "))*0.10
    nickels_in_cents = float(input("Number of nickels:"))*0.05
    pennies_in_cents = float(input("Number of pennies:"))*0.01
    return quarters_in_cents + dimes_in_cents + nickels_in_cents + pennies_in_cents - MENU[beverage_choice]['cost']


def get_user_choice():
    choice = ""
    while choice not in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
        choice = input("What would you like? (espresso/latte/cappuccino)")
    return choice


def turn_off_machine():
    exit()


def can_deduct_resources(ingredients):
    for ingredient in ingredients:
        # print(resources[ingredient])
        # print(ingredients[ingredient])
        if ingredients[ingredient] < resources[ingredient]:
            resources[ingredient] -= ingredients[ingredient]
        else:
            return False
    return True


if __name__ == '__main__':
    while True:
        choice = get_user_choice()

        if choice == 'off':
            exit()
        elif choice == 'report':
            for key in resources:
                print("Printing Report:")
                print(key + ":" + str(resources[key]))
        else:
            if check_resources_sufficient(choice):
                change = take_coins(choice)
                if change >= 0:
                    print('That will cost ' + str(MENU[choice]['cost']) + ' Dollars')
                    print("Your change is: " + str(change) + " Dollars")
                else:
                    print("You do not have enough money!")
                    print("Refunding " + str(change+MENU[choice]['cost']) + ' Dollars')
                if can_deduct_resources(MENU[choice]['ingredients']):
                    print("Here is your " + choice + ". Enjoy!")
                else:
                    print("Machine is out of resources, please stock machine!")
            else:
                print("Machine is out of certain ingredients!")

