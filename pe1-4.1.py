"""
Objective: Write a Python program that includes two functions - one to calculate the area of a square and another for the area of a circle.

Instructions:

Start with Function Definitions:

Define two functions: square and circle.
Each function should take one parameter (side for square, radius for circle).
Write the square Function:

Calculate the area as side * side and display the result: "The area of the square is [result] square units."
Write the circle Function:

Calculate the area using the formula: area = π * radius * radius. Use 3.14 for π.
Display the result: "The area of the circle is [result] square units."
Test Your Functions:

Call square and circle with sample values.
"""
def square(side):
    print("The area of the square is",side**2,"units")
square(4.5)
def circle(radius):
    print("The area of the circle is",radius*radius*3.14,"units")
circle(3)