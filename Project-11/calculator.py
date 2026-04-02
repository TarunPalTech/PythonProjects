import calculator_art
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        print("Cannot divide by zero.")
        return a
    return a/b

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    should_continue = True

    while should_continue:
        print(calculator_art.calculator_picture)
        while True:
            try:
                num1 = float(input("What's the first number?: "))
                break
            except ValueError:
                print("Please enter a valid number.")

        while True:
            print("Available operations:")
            for operation in operations:
                print(operation)

            operation_symbol = input("Pick an operation: ")
            if operation_symbol not in operations:
                print("Invalid operation")
                continue
            
            while True:
                try:
                    num2 = float(input("What's the next number?: "))
                    break
                except ValueError:
                    print("Please enter a valid number.")

            result = operations[operation_symbol](num1, num2)

            print(f"{num1} {operation_symbol} {num2} = {result}")

            choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
            while choice not in ["y", "n"]:
                choice = input(f"Please choose a correct option. Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

            if choice == 'n':
                break
            num1 = result
            

        # to start a new calculation...
        while True:
            restart = input("Do you want to continue with a new value? {y/n}\n").lower()
            if restart == "n":
                should_continue = False
                print("Goodbye! Thank you for using  this program!")
                break
            else:
                clear()
                break
calculator()

input("Press enter to close this program.....")