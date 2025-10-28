"""
Set up your program in a main() function.
Create a Python program that asks the user to input a password.
Ensure the password meets the following criteria:
Between 8 to 20 characters long.
Contains at least one uppercase letter.
Contains at least one lowercase letter.
Includes at least one number.
Includes at least one symbol from the set: !@#$%&*.
Use a while loop to keep asking for the password until all criteria are met.
Once a valid password is entered, prompt the user to enter it again for confirmation.
Use try-except blocks to handle any errors or exceptions that occur.
If the second password entry matches the first, display a success message. Otherwise, prompt the user to start the process again.
"""


def main():

    # Introduce the user to the requirements

    print("Password must contain:\n8-20 characters\nAt least one uppercase\nAt least one lowercase\nAt least one number\nAt least one special character")

    def password_set():
        special_char = ["!", "@", "#", "$", "%", "&", "*"]

        while True:
            password_input = input("\nSet your password: ")
            password_list = list(password_input)
            checks = 0        # Password must have all 5 criteria to pass
            if 8 <= len(password_list) <= 20:
                checks += 1
            else:
                print("Password must be 8-20 characters")
            if any(char.isupper() for char in password_list):
                checks += 1
            else:
                print("Password must contain a uppercase character")
            if any(char.islower() for char in password_list):
                checks += 1
            else:
                print("Password must contain an lowercase character")
            if any(char.isnumeric() for char in password_list):
                checks += 1
            else:
                print("Password must contain a number")
            if any(char in special_char for char in password_list):
                checks += 1
            else:
                print("Password must contain a special character")
            if checks == 5:
                return password_input

    try:
        password = password_set()       # Prompt the user to set their password
        while True:
            password_attempt = input("\nEnter your password: ")
            if password_attempt == password:
                print("\nLogin successful")
                break
            else:
                print("Password incorrect")
    except Exception as e:
        print("Unexpected error:", e)


main()
