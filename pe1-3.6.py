"""
Create a list representing 20 seats, numbered 1 to 20.
Display the list of available seats to the customer.
Prompt the customer to select a seat by entering its number. Entering '0' ends the purchase process.
Remove the selected seat from the list of available seats and display the updated list.
If the customer selects an invalid or already sold seat, display a friendly error message and prompt them to try again.
Ensure the program gracefully handles all scenarios and is user-friendly.
"""
available_seats = []
for i in range(20):
    available_seats.append(str(i+1))
sold_out = False
while sold_out == False:
    print(f"Seats {available_seats} are available")
    seat = (input("Please select a seat: "))
    if seat in available_seats:
        available_seats.remove(seat)
    elif seat == str(0):
        print("Transaction canceled.")
        sold_out = True
    else:
        print("Invalid selection, please try again.")
    if len(available_seats) == 0:
        print("Seats are sold out.")
        sold_out = True