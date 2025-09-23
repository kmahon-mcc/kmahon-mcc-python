"""
Create a List: Start by creating a list named days that includes all seven days of the week.
Initialize an Empty List: Create an empty list called steps to store the number of steps taken each day.
User Input: Using a loop, ask the user to enter the number of steps they took for each day.
Store Steps: Append the user's input to the steps list.
Display Daily Steps: Show the user the steps recorded for each day.
Total Steps: Calculate and display the total number of steps taken in the week.
Average Steps: Calculate and display the average steps.
"""
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
steps = []
step_total = 0
for i in range(len(days)):
    day = days[i]
    steps.append(int(input(f"How many steps did you take on {day}? ")))
for i in range(len(steps)):
    step = steps[i]
    day = days[i]
    print(f"On {day} you took {step} steps.")
    step_total += step
step_average = int(step_total/len(steps))
print(f"You took an average of {step_average} steps, for a total of {step_total}.")