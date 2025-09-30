"""
Select a Song: Choose a song that is well-known and suitable for a classroom setting. Avoid any song with inappropriate or offensive content.
Identify Variables: Determine at least 8 different variables that the user will provide to customize the song. These could include names, adjectives, nouns, places, etc.
Write the Function:
Define a function named custom_song that takes at least 8 parameters corresponding to the variables you've identified.
Use f-strings to incorporate these parameters into the song's lyrics.
Ensure the function prints the customized song lyrics.
Collect User Input:
Write code to collect user input for each of the 8 variables.
Use clear and descriptive prompts to guide the user.
Call the Function:
Call the custom_song function with the user inputs as named arguments.
Ensure the order of arguments matches the parameters in your function definition.
"""
adjective1_in = input("Please enter an adjective: ")
adjective2_in = input("Please enter another adjective: ")
place_in = input("Please enter a place: ")
name_in = input("Please enter a name: ")
name_in = name_in.upper()
noun1_in = input("Please enter a noun: ")
noun2_in = input("Please enter another noun: ")
noun3_in = input("Please enter a third noun: ")
bodypart_in = input("Please enter a body part: ")
furniture_in = input("Please enter a piece of furniture: ")

def ghostbusters(adjective1,adjective2,place,name,noun1,noun2,noun3,bodypart,furniture):
    print(f"\n\nIf there's something {adjective1},\nIn your {place},\nWho you gonna call?\n{name}!")
    print(f"If there's something {adjective1},\nAnd it don't look {adjective2},\nWho you gonna call?\n{name}!")
    print(f"I ain't afraid of no {noun1}!\nI ain't afraid of no {noun1}!\nIf you're seeing {noun2},")
    print(f"Runnin' through your {bodypart},\nWho you gonna call?\n{name}!\nAn invisible {noun2},")
    print(f"Sleepin' on your {furniture},\nOw, who you gonna call?\n{name}!\nI ain't afraid of no {noun1}!")
    print(f"I ain't afraid of no {noun1}!\nWho you gonna call?\n{name}!\nIf you're all {adjective2},")
    print(f"Pick up the {noun3},\nAnd call\n{name}!\nWho you gonna call?\n{name}!")
ghostbusters(adjective1_in,adjective2_in,place_in,name_in,noun1_in,noun2_in,noun3_in,bodypart_in,furniture_in)