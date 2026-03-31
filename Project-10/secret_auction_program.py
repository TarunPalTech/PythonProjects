from hammer_art import hammer
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

should_continue = True

while should_continue:
    print(hammer)
    print("\n\nWelcome to the secret auction program!")

    bidders_and_amounts = {}

    while True:
        name = input("What is your name?: ")

        while True:
            try:
                bid = float(input("What is your bid?: $"))
                break
            except ValueError:
                print("Please enter a valid amount!")

        bidders_and_amounts[name] = bid

        other = input("Are there any other bidders? Type 'yes or no': ").lower()

        if other == "yes":
            clear()
        elif other == "no":
            break
        else:
            print("Invalid option.")

    winner = max(bidders_and_amounts, key=bidders_and_amounts.get)
    print(f"The winner is {winner} with a bid of ${bidders_and_amounts[winner]}.")

    restart = input("Do you want to continue again? (yes/no): ").lower()

    if restart == "yes":
        clear()
    else:
        should_continue = False
        print("Good Bye!")

input("Press enter to exit......")