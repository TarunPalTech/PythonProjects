import logo_art
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


is_over = False

while not is_over:
    print(logo_art.logo)
    print("Welcome to the Number Guessing Game!")

    number = random.randint(1, 100)

    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while level not in ['easy', 'hard']:
        level = input("Please choose a correct option.\nChoose a difficulty. Type 'easy' or 'hard': ").lower()

    attempts = 10 if level == 'easy' else 5
    print("\n")

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")

        while True:
            try:
                guess = int(input("Make a guess: "))
                if 1 <= guess <= 100:
                    break
                print("Enter a number between 1 and 100.\n")
            except ValueError:
                print("Please enter a correct value!\n")
        
        if guess == number:
            print(f"\nYou got it! The answer was {number}.")
            break
        elif guess > number:
            print("Too high. Guess again!\n")
        else:
            print("Too low. Guess again!\n")
        attempts -= 1

        if attempts == 0:
            print("\nYou've run out of guesses.")
            break
    
    restart = input("\nDo you want to play again? {y/n}\n").lower()
    while restart not in ['y', 'n']:
        restart = input("\nPlease choose a correct option. Do you want to play again? {y/n}\n").lower()

    if restart == 'n':
        print("Good bye!")
        is_over = True
    else:
        clear()

input("Press key to close this window....")