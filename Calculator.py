
# Day 10: Calculator

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    sum = n1 + n2
    return sum

def subtract(n1, n2):
    sub = n1 - n2
    return sub

def multiply(n1, n2):
    product = n1 * n2
    return product

def divide(n1, n2):
    quotient = n1 / n2
    return quotient

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    should_continue = True
    while should_continue:

        for symbol in operations:
            print(symbol)
        
        operation_symbol = input("Pick an operation from above lines: ")

        num2 = float(input("What's the next number?: "))

        chosen_operation = operations[operation_symbol]
        answer = chosen_operation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        ask = input(f"Type y to continue calculating with {answer} or type n to start a new calculation or type e to exit the calculator: ")
        if ask == "y":
            num1 = answer
        elif ask == "n":
            should_continue = False
            calculator()
        elif ask == "e":
            should_continue = False
            print("Thank You!")
        else:
            print("No valid command given!")

calculator()