import random

print("Welcome to the Who Will Pay the Bill Game! 🍽️💸\n")

# Fun messages to show when someone is picked
fun_messages = [
    "Better luck next time! 😏",
    "Oops! It's your turn to pay! 💸",
    "You got the lucky bill! 😂",
    "Time to open your wallet! 💰",
    "Don’t worry, it’s just a game! 😅"
]

while True:
    names = []  # Reset names each round
    i = 1
    while True:
        name = input(f"Enter name of person {i}: ")
        names.append(name)
        
        if i > 1:
            choice1 = input("Do you want to enter one more name? (y/n): ").lower()
            while choice1 not in ["y", "n"]:
                choice1 = input("Invalid input! Please enter 'y' or 'n': ").lower()
            if choice1 == 'n':
                break
        i += 1
    
    print("\nPlayers:", ", ".join(names))
    
    # Randomly select a payer
    payer = random.choice(names).upper()  # Highlight the payer in uppercase
    message = random.choice(fun_messages)
    
    print(f"\n🎉 Congratulations, {payer} will pay the bill! 🍽️💸")
    print(f"{message}\n")
    
    choice2 = input("Do you want to play another round? (y/n): ").lower()
    while choice2 not in ["y", "n"]:
        choice2 = input("Invalid input! Please enter 'y' or 'n': ").lower()
    if choice2 == 'n':
        print("\nThanks for playing! 😄 Have a great meal! 🍽️")
        break
    print("\n--- New Round ---\n")