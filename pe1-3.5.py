"""
Prompt the user to enter five names.
Store the names in a list.
Sort the list using the Bubble Sort algorithm.
Reverse the sorted list using a Python list method.
Print both the sorted and reversed lists.
"""
names = []
for i in range(5):
    names.append(input(f"Please enter name {i+1}: "))
swapped = True
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i+1]:
            names[i], names[i+1] = names[i+1], names[i]
            swapped = True
print(names)
names.reverse()
print(names)