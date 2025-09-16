# Directions:
#Accept a numeric grade from the user and display a letter grade. The  grading scale is  90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F
#Check to see if the number given is between 0 and 100.
number_grade = int(input("What is the grade? "))
if number_grade < 0:
    letter_grade = "Error: grade must be an integer between 0 and 100"
elif number_grade <60:
    letter_grade = "F"
elif number_grade < 70:
    letter_grade = "D"
elif number_grade < 80:
    letter_grade = "C"
elif number_grade < 90:
    letter_grade = "B"
elif number_grade <100:
    letter_grade = "A"
else:
    letter_grade = "Error: grade must be an integer between 0 and 100"
print("The letter grade is: ", str(letter_grade))