import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print("Welcome to Multi-Round Rock, Paper, Scissors! 🎮✂️📄🪨\n")

while True:
    user_points = 0
    computer_points = 0

    for i in range(1, 4):
        print(f"\n--- Round {i} ---")
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

        while user_choice not in [0,1,2]:
            user_choice = int(input("Invalid input! Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

        computer_choice = random.randint(0,2)

        print("\nYou chose:")
        print(game_images[user_choice])
        print("Computer chose:")
        print(game_images[computer_choice])

        # Determine points
        if user_choice == computer_choice:
            user_points += 1
            computer_points += 1
            print("It's a tie this round! 🤝")
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 1 and computer_choice == 0):
            user_points += 2
            print("You win this round! 🎉")
        else:
            computer_points += 2
            print("Computer wins this round! 😢")

        print(f"Current score -> You: {user_points} | Computer: {computer_points}")

    # Game result after 3 rounds
    print("\n=== Game Over ===")
    if user_points == computer_points:
        print("It's a tie overall! 🤝")
    elif user_points > computer_points:
        print("🎉 You win the game! 🏆")
    else:
        print("Computer wins the game! 😢")

    another_round = input("\nDo you want to play another game? (y/n): ").lower()
    while another_round not in ["y", "n"]:
        another_round = input("Invalid input! Enter 'y' or 'n': ").lower()
    if another_round == 'n':
        print("\nThanks for playing! Play better next time! 😄")
        break

    print("\n---------- New Game ----------\n")