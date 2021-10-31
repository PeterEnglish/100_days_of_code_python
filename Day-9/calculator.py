
from art import logo

def add( n1, n2):
    return n1 + n2

def subtract( n1, n2):
    return n1 - n2

def multiply( n1, n2):
    return n1 * n2

def divide( n1, n2):
    return n1 / n2



operations = {
    '+': add,
    '-':subtract,
    '*':multiply,
    '/':divide
    
}

def calculator():
    print(logo)
    num1 = int(input("What is the first number?: "))

    

    should_continue=True

    while should_continue:

        for key in operations:
            print(key)

        operation_symbol= input("Pick an operation from the line above: ")

        num2 = int(input("What is the second number?: "))

        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation")=='y':
            num1=answer
        else:
            should_continue = False
            calculator()

calculator()