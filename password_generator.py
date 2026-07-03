import random
import string


def get_password_length():
    while True:
        try:
            length = int(input("Enter password length: "))

            if length >= 4:
                return length
            else:
                print("Password length should be at least 4.")

        except ValueError:
            print("Please enter a valid number.")


def password_details():
    character = string.ascii_lowercase

    upp = input("Include uppercase letters? (yes/no): ").lower()
    if upp == "yes":
        character += string.ascii_uppercase

    num = input("Include numbers? (yes/no): ").lower()
    if num == "yes":
        character += string.digits

    symb = input("Include symbols? (yes/no): ").lower()
    if symb == "yes":
        character += string.punctuation

    return character


def generate_password():
    character = password_details()
    total_string = ""

    length = get_password_length()

    for i in range(length):
        one_char = random.choice(character)
        total_string += one_char

    return total_string


def main():
    while True:
        print("\n===== Password Generator =====")
        password = generate_password()

        print(f"\nGenerated Password: {password}")

        repeat = input("\nGenerate another? (yes/no): ").lower()

        if repeat == "no":
            print("Goodbye!")
            break


main()