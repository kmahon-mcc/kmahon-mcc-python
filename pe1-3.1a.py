"""
Asks the user for their age and converts the input to an integer.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount.
Prints all the results on the screen, ensuring the output (is straightforward and user-friendly.
"""
age = int(input("How old are you? "))
if age < 0:
    print("Age must be a positive integer")
else:
    if age < 16:
        print("You are not old enough to drive.")
    else:
        print("You are old enough to drive.")
    if age < 18:
        print("You are not old enough to vote.")
    else:
        print("You are old enough to vote.")
    if age < 21:
        print("You are not old enough to drink.")
    else:
        print("You are old enough to drink.")
    if age < 65:
        print("You do not qualify for a senior discount.")
    else:
        print("You qualify for a senior discount.")