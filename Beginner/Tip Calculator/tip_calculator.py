# Print a welcome message for the user
print("Welcome To The Tip Calculator!")

# Prompt the user to enter the total bill amount and convert it to a floating-point number
bill = float(input("What was the total bill?\n$:"))

# Prompt the user to enter the tip percentage they want to give and convert it to an integer
tip = int(input("What percentage tip would you like to give?\nPercent:"))

# Prompt the user to enter the number of people to split the bill and convert it to an integer
split = int(input("How many people to split the bill?\nPeople:"))

# Calculate the total amount each person should pay
# The formula calculates the tip amount, adds it to the bill, and divides the total by the number of people
# Format the result to 2 decimal places for clarity
total = ("{:.2f}".format((((bill * (tip / 100)) + bill) / split)))

# Print the amount each person needs to pay, formatted as currency
print(f"Each person should pay: ${total}")
