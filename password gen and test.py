import secrets
import string
import re


def menu():
    #selection screen
    print("Below are the number to help you enter options and come back to the menu.")
    print("[1] Password Generator")
    print("[2] Password Strength Tester")
    print("[0] exit")

def generate_password(length):
    # define the alphabet
    letters = string.ascii_letters
    num = string.digits
    symbol = string.punctuation
    alpha = letters + num + symbol

    # generate a password string
    password = ''
    for i in range(length):
        password += secrets.choice(alpha)
    return password

def test_password(password):
    # Check the length of the password.
    if len(password) <8:
        return False

        # Check if the password contains all of the required character types.
    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special_character = False
    for character in password:
        if character.isupper():
            has_uppercase = True
        elif character.islower():
            has_lowercase = True
        elif character.isdigit():
            has_number = True
        elif re.match(r'[_@$]', character):
            has_special_character = True

    return has_uppercase and has_lowercase and has_number and has_special_character

def main():
    while True:
        menu()
        op = int(input("enter option: "))
        if op == 1:
            password_length = int(input("Enter the length of the password: "))
            password = generate_password(password_length)
            print(password)
        elif op == 2:
            password = input("Enter the password to test: ")
            if test_password(password):

                print("The password is strong.")
            else:
                print("The password is weak.")

        elif op == 0:
            break


if __name__ == '__main__':
    main()

#debug


#end
