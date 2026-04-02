import os
import random
import capstone_art

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_result(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif u_score == 0:
        return "You win with a BlackJack!"
    elif c_score == 0:
        return "Computer win with a BlackJack!"
    elif c_score > 21:
        return "You win!"
    elif u_score > 21:
        return "You lose!"
    elif c_score > u_score:
        return "You lose!"
    else:
        return "You win!"

def get_card():
    return random.choice(cards)

def get_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    
    return score


should_continue = False

while not should_continue:
    print(capstone_art.cards_img)
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(get_card())
        computer_cards.append(get_card())

    is_over = False

    computer_score = -1
    user_score = -1

    while not is_over:
        user_score = get_score(user_cards)
        computer_score = get_score(computer_cards)
        print(f"User's cards: {user_cards}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score != 0 and user_score > 21:
            is_over = True
            continue

        user_should_deal = input("Type 'y' to get another card, type 'n' to pass:").lower()
        while user_should_deal not in ['y','n']:
            user_should_deal = input("Please choose a correct option. Type 'y' to get another card, type 'n' to pass:").lower()
        
        if user_should_deal == 'n':
            is_over = True
        else:
            user_cards.append(get_card())

    while computer_score !=0 and computer_score < 17:
        computer_cards.append(get_card())
        computer_score = get_score(computer_cards)

    print(f"{get_result(user_score, computer_score)}")
    print(f"Your final cards: {user_cards}, final score: {user_score}")
    print(f"Computer final cards: {computer_cards}, final score: {computer_score}")

    # restarting the game...
    restart = input("Do you want to continue? {y/n}").lower()
    while restart not in ["y","n"]:
        restart = input("Please choose a correct option. Do you want to continue? {y/n}").lower()
    if restart == 'n':
        should_continue = True
        print("Goodbye! Thank you for playing this BlackJack Capstone!")
    else:
        clear()

input("Press enter to close this window.....")