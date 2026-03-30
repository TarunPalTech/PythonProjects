# 📦 Importing modules
from os import system, name
import random 
from words import words
from hangman_art import stages, logo

# To clear console screen
def clear():
    system('cls' if name == 'nt'  else 'clear')


while True:
    # To clear console....
    clear()

    # 🎨 Display game logo and welcome message
    print(logo)
    print("🎮 Welcome to the Hangman Game!")


    # 🎲 Choosing a random word
    word_chosen = random.choice(words)

    # 🐞 Debug line (uncomment only while testing)
    print(word_chosen)


    # 🔤 Creating blanks according to word length
    guessed_characters = ['_'] * len(word_chosen)

    print(f"\nCurrent word progress:- {''.join(guessed_characters)}\n")


    # ❤️ Game state variables
    game_over = False
    lives = len(stages) - 1


    # 🔁 Main game loop
    while not game_over:

        guess = input("🔤 Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single letter.")
            continue

        # ⚠️ Check if letter was already guessed
        if guess in guessed_characters:
            print("⚠️ You already entered this letter!")
            continue


        # ✅ Reveal correct letters
        for index, letter in enumerate(word_chosen):
            if guess == letter:
                guessed_characters[index] = letter


        # ❌ Handle wrong guess
        if guess not in word_chosen:
            print(stages[lives])
            lives -= 1

            print(f"❌ Your guessed character '{guess}' is wrong!")

            if lives == 0:
                print(stages[0])
                print(f"💀 You lose the game! The correct word was '{word_chosen}'.")
                game_over = True
                continue
            else:
                print(f"❤️ Remaining attempts: {lives}")


        # 📊 Display progress
        print("⭐" * 40)
        print(''.join(guessed_characters))


        # 🏆 Win condition
        if '_' not in guessed_characters:
            print("\n🏆 Congratulations! You win!")
            game_over = True
    
    while True:
        play_again = input("Do you want to play again! {y/n}: ").lower()
        if len(play_again)!=1 or not play_again.isalpha():
            print("Choose a correct option.")
            continue

        if play_again not in ["y", "n"]:
            print("Please type 'y' or 'n'.")
            continue
        break

    
    if play_again == 'n':
        print("Thank You for playing this game!")
        break