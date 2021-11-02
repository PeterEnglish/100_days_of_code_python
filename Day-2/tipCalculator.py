print("Welcome to the tip calculator.")
total = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15: "))
people = int(input("How many poeple to split the bill?"))
percentage = tip/100
total = total + percentage*total
split = "{:.2f}".format(total/people)
print("Each person should pay: $" + str(split))