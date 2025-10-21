"""
Start Your Python Script:
Open your Python environment and start a new script.
Use a main() function to organize your code.
Prompt for User Input:
Ask the user to enter a single character using input().
Validate the Input:
Ensure the user enters precisely one character.
Use len() to check input length.
Convert to ASCII Value:
Use the built-in function ord() to get the ASCII value.
Example:
ascii_value = ord(user_input)
Display the Result:
Print the ASCII value to the user.
Reverse Lookup:
Prompt the user to enter an ASCII value.
Ensure that the value is between 32 and 127.
Use a try-except block to handle invalid inputs.
Use the built-in function chr() to get the corresponding character.
Example:
character = chr(ascii_input)
Test Your Program:
Run your script and try various characters and ASCII values.
Submit Your Work:
Upload your script to GitHub.
Submit a link to your repository.
"""


def main():
    while True:
        chr_input = input("Please enter a single character: ")
        if len(chr_input) == 1:
            ascii_output = ord(chr_input)
            print("The ASCII value of that character is", ascii_output)
            break
        else:
            print("Invalid input")
    while True:
        try:
            ascii_input = int(
                input("Please enter a number between 32 and 127: "))
            if 32 <= ascii_input <= 127:
                chr_output = chr(ascii_input)
                print("The character with that ASCII value is", chr_output)
                break
            else:
                print("Invalid input: number must be between 32 and 127")
        except:
            print("Invalid input: must be a number between 32 and 127")


main()
