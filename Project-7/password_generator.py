import string
import secrets

chars = string.ascii_letters + string.digits + string.punctuation

while True:
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    password = "".join(secrets.choice(chars) for _ in range(length))
    print("Generated password:", password)

    selected_option = input("Would you like to generate another password? (y/n)\n").lower()

    while selected_option not in ["y", "n"]:
        selected_option = input("Choose carefully! (y/n)\n").lower()

    if selected_option == "n":
        break