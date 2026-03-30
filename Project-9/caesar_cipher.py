from art import logo
from os import system, name

def clear():
    system("cls" if name == 'nt' else "clear")

# logo printing...
print(logo)

# We are using traditional Roman technique that's why we are not including digit and special characters in this process.

def caesar(original_text, shifted_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shifted_amount *= -1 # reverse for decoding

    for letter in original_text:
        if letter.isalpha():
            if letter.islower():
                output_text += chr((ord(letter) - ord('a') + shifted_amount) % 26 + ord('a'))
            else:
                output_text += chr((ord(letter) - ord('A') + shifted_amount) % 26 + ord('A'))
        else:
            output_text += letter

    print(f"Here is the {encode_or_decode} result: {output_text}")


# Main loop

should_continue = True

while should_continue:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt: ').lower()

    while direction not in ["decode", "encode"]:
        direction = input('Choose a correct option. Type "encode" to encrypt, type "decode" to decrypt: ').lower()

    text = input("Enter your text: ")
    while True:
        try:
            shift = int(input("Enter the shift number: ")) % 26
            break
        except ValueError:
            print("Please enter a valid digit.")

    caesar(original_text=text, shifted_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' to go again, or 'no' to quit: ").lower()
    while restart not in ["yes", "no"]:
        restart = input("Choose a correct option. Type 'yes' to go again, or 'no' to quit: ").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye!")
    else:
        clear()

input()