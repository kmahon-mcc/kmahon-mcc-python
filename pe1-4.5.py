"""
Start by defining a function named factorial that takes one parameter, n, representing the number you're calculating the factorial for.
In your factorial function, first define the base case: n == 1 or n == 0, where the factorial is 1.
For the recursive step, return n * factorial(n-1) if n > 1.
Prompt the user for a non-negative integer and call factorial, printing the result.
"""
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
factorial_input = int(input("Please enter a natural number: "))
print(f"The factorial of {factorial_input} is",factorial(factorial_input))