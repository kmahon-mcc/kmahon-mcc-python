"""
Write a short interactive Python program of your choice that uses try and except to catch and respond to at least two specific exceptions. Your program should:

Include a main() function.
Use try and except to catch specific errors like ValueError or ZeroDivisionError.
Provide helpful messages when errors occur.
Do something meaningful or fun—be creative! You could build a number guessing game, a basic calculator, or even a simple quiz with input validation.
"""

import random


def main():
    while True:
        try:
            num1 = int(input("Lets do some simple math. Enter a number: "))
            num2 = int(input("And another: "))
            choice = input(
                "Now choose an operation. Your choices are add, subtract, multiply, divide, or capitalize: ")
            if choice == "add":
                print("Result:", num1 + num2)
            elif choice == "subtract":
                print("Result:", num1 - num2)
            elif choice == "multiply":
                print("Result:", num1 * num2)
            elif choice == "divide":
                print("Result:", num1 / num2)
            else:
                print("Result:", num1.upper(), num2.upper())
        except ValueError:
            print("Error: input needs to be a number")
        except ZeroDivisionError:
            print("Error: cannot divide by 0")
        except AttributeError:
            print("I was kidding about that, you can't capitalize a number")


main()
