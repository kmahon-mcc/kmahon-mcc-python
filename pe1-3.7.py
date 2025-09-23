"""
Define time_slots as a list with times of day (e.g., "Morning", "Midday", "Afternoon", "Evening").
Use a loop to prompt the user for heart rate (in BPM) at each time slot.
Create a multi-level list heart_rates to store the time slots and their corresponding heart rates.
Calculate the average heart rate and display it.
"""
time_slots = []
heart_rates = []
heart_rate_total = 0
for i in range(6):
    time = (f"{(2*i)+8}:00")
    time_slots.append(time)
    heart_rate = input(f"Heart rate at {time}: ")
    if heart_rate.isdigit():
        heart_rates.append([time, heart_rate])
        heart_rate_total += int(heart_rate)
    else:
        print("Input must be whole number.")
heart_rate_average = int(heart_rate_total/len(time_slots))
print(f"Your average heartrate was {heart_rate_average}")