from random import randint


while True:
    choice = input("Choose head or tails: ").lower()

    if choice not in ["head", "tails"]:
        print("Invalid choice!")
    else:
        result = "head" if randint(0, 1) == 0 else "tails"

        if choice == result:
            print("You won!")
        else:
            print("You lost!\n")
    play_or_not = input("Do you want to play again? y/n\n").lower()
    if play_or_not == 'n':
        break
    