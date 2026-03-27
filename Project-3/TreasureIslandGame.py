"""
Treasure Island Game – Problem Statement

You are required to create a text-based adventure game in Python called “Treasure Island”.

Story

You are a brave adventurer searching for the legendary treasure hidden on a mysterious island. Armed with a treasure map and your courage, you arrive at the island. Your mission is to find the treasure while avoiding traps, pirates, and dangerous creatures.

The game should ask the player to make choices at different stages of the adventure. Based on the player's choices, the story will move forward and lead to either winning the treasure or losing the game.

Game Flow
Level 1: Arrival at the Island

When the game starts, the player reaches the island shore.

The player must choose:

Enter the dense jungle
Explore the rocky beach
Level 2A: Jungle Path

If the player chooses the jungle, they will see two options:

Follow the river upstream
Climb the steep hill
If the player follows the river

They reach a waterfall with a hidden cave.

Choices:

Enter the dark cave
Search around the waterfall

Both paths may lead to discovering the treasure.

If the player climbs the hill

They see a pirate ship approaching.

Choices:

Hide in the jungle
Signal or approach the pirates

One choice may lead to safety and treasure, while the other leads to losing the game.

Level 2B: Beach Path

If the player chooses the beach, they see:

Inspect an abandoned boat
Explore a mysterious cave
If the player inspects the boat

It turns out to be a pirate trap, and the player loses.

If the player explores the cave

They find treasure map fragments.

Choices:

Take the left path (dark and eerie)
Take the right path (bright but suspicious)

One path leads to the treasure while the other leads to danger.

Game Requirements

Your Python program should:

Display the story using print()
Take player choices using input()
Use if, elif, and else statements to control the game flow
End the game with either:
"You won!" when the treasure is found
"Game Over" when the player loses

✅ Goal:
Design a simple interactive adventure game where the player’s choices determine the final outcome.
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')


def start_game():
    print("""
        Welcome to Treasure Island Adventure Story!
        
        Introduction:
        You are a daring adventurer searching for the legendary Treasure of the Lost Island.
        Legends say it is hidden in a secret cave, guarded by traps, riddles, and mystical creatures.
        Armed with a map, a compass, and your wits, you arrive at the mysterious island.
        Your goal: find the treasure and return safely.
    """)
    level1()


def level1():
    print("Level 1: Arrival at the Shore")
    choice1 = ""
    while choice1 not in ["1", "2"]:
        choice1 = input(
            "Choices:\n1. Enter the dense jungle.\n2. Explore the rocky beach.\n"
        )
    if choice1 == "1":
        jungle_path()
    else:
        beach_path()


# ---------------- Jungle Path ----------------
def jungle_path():
    print("You step into the dense jungle. Strange sounds surround you.")
    choice2 = ""
    while choice2 not in ["1", "2"]:
        choice2 = input(
            "Choices:\n1. Follow the river upstream.\n2. Climb the steep hill.\n"
        )
    if choice2 == "1":
        waterfall_cave()
    else:
        pirate_ship()


def waterfall_cave():
    print("You find a waterfall with a hidden cave behind it.")
    choice3 = ""
    while choice3 not in ["1", "2"]:
        choice3 = input(
            "Choices:\n1. Enter the dark cave.\n2. Search around the waterfall.\n"
        )
    if choice3 == "1":
        print(
            "You carefully navigate traps inside the cave and discover the treasure room!\nYou won!"
        )
    else:
        print(
            "You find an old pirate diary revealing a secret entrance. Following it, you discover the treasure!\nYou won!"
        )


def pirate_ship():
    print("You climb the hill and spot a pirate ship approaching.")
    choice3 = ""
    while choice3 not in ["1", "2"]:
        choice3 = input(
            "Choices:\n1. Hide in the jungle.\n2. Try to signal/fight the pirates.\n"
        )
    if choice3 == "1":
        print(
            "The pirates leave after some time. You carefully navigate through the jungle and find the treasure!\nYou won!"
        )
    else:
        print("The pirates overpower you. You lose!\nGame Over!")


# ---------------- Beach Path ----------------
def beach_path():
    print(
        "You walk along the rocky beach. It's easier to navigate but pirates may be nearby."
    )
    choice2 = ""
    while choice2 not in ["1", "2"]:
        choice2 = input(
            "Choices:\n1. Inspect the abandoned boat.\n2. Explore the mysterious cave nearby.\n"
        )
    if choice2 == "1":
        print("The boat was a trap set by pirates. You lose!\nGame Over!")
    else:
        mysterious_cave()


def mysterious_cave():
    print("You enter the mysterious cave and find fragments of a hidden treasure map.")
    choice3 = ""
    while choice3 not in ["1", "2"]:
        choice3 = input(
            "Choices:\n1. Take the left path (dark and eerie).\n2. Take the right path (bright, smells of flowers).\n"
        )
    if choice3 == "1":
        print(
            "You solve the riddles guarding the treasure chamber successfully!\nYou won!"
        )
    else:
        print("You wake a sleeping giant snake. It attacks!\nYou lose!\nGame Over!")


# ---------------- Start the Game ----------------
start_game()

input()