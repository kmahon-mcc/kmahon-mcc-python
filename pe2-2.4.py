"""
Set Up the Main Function: Write your program inside a main function. This is where your while loop will be implemented.
Collect Book Titles: Use a while loop to ask the customer to enter 10 book titles. Store these titles in a list.
Ensure proper capitalization: Use the title function to ensure that the first letter is capitalized before storing it in the list.
Create a Sorted List: Once all titles are collected, save them to a new list named books_sorted. This list should contain the titles in alphabetical order.
Display the Titles: Use a for loop to print each title from the sorted list on a separate line.
Test Your Program: Ensure your program runs correctly and meets all the requirements.
Upload to GitHub: Once tested, upload your program to GitHub.
Submit Your Work: Submit the link to your GitHub repository on Canvas.
"""


def main():
    books = []
    while len(books) < 10:
        if len(books) == 0:  # Asking the user for an input (changing grammar for first entry)
            new_book = input("Please enter a book title: ")
        else:
            new_book = input("please enter another book title: ")
        books.append(new_book.title())  # Adding the user input
    sorted_books = sorted(books)  # Creating a sorted list
    print("")  # Spacing
    for book in sorted_books:  # Presenting sorted list
        print(book)


main()
