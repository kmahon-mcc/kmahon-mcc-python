"""
Global Variables:
Conversion constants for weight (1 lb = 0.453592 kg) and height (1 in = 0.0254 m).
Main Function:
Prompt the user for their weight in pounds and height in inches.
Convert the inputs to metric units using global conversion constants.
Calculate BMI using the formula bmi = weight / (height * height).
Determine the BMI category based on standard ranges.
Display the BMI value and category.
Commenting:
Include comments to explain key parts of the code.
"""

WEIGHT_CONV = 0.453592
HEIGHT_CONV = 0.0254
weight = input("Please enter your weight in lbs: ")
height = input("Please enter your height in inches: ")


def bmi_calc(weight, height):
    try:
        bmi = (float(weight) * WEIGHT_CONV) / (float(height) * HEIGHT_CONV) ** 2
        return bmi
    except:
        print("Invalid input: please enter a number")


user_bmi = bmi_calc(weight, height)
print("Your BMI is: ", user_bmi)
try:
    if user_bmi <= 18.5:
        print("You are in the underweight category")
    elif user_bmi < 25:
        print("You are in the normal category")
    elif user_bmi < 30:
        print("You are in the overweight category")
    else:
        print("You are in the obese category")
except:
    None
