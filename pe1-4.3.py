def calculate_interest(principal,interest_rate,time):
    interest = (principal*interest_rate*time)/100
    return interest
result = calculate_interest(100,5,1)
print(result)