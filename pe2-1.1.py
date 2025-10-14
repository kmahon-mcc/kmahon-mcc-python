"""
Import the random module and use it to generate a random number between 1 and 100.
Write a while loop that allows the user to enter a guess for the number.
Inside the loop, use the abs() function to calculate the absolute difference between the guess and the actual number.
Provide feedback based on the computed difference (e.g., "Very Hot" for close guesses).
The loop should continue until the user guesses the correct number.
"""

from random import randrange

print(
    "Let's play a guessing game!\nI'm gonna pick a number from 1-100, and you have to guess it."
)


def main():
    guess = 0
    random_number = randrange(100)
    try:
        while random_number != guess:
            guess = int(input("Guess the number: "))
            guess_prox = abs(random_number - guess)
            if guess_prox == 0:
                break
            elif guess_prox <= 5:
                print("Very hot")
            elif guess_prox <= 15:
                print("Hot")
            elif guess_prox <= 25:
                print("Cool")
            else:
                print("Cold")
        print("You win!")
    except:
        print("Please enter a valid number")
        main()


main()
