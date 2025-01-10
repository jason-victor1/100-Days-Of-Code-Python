import random  # Importing the random module to generate random numbers

# List of possible characters for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # List of digits
# List of special characters
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Display a welcome message
print("Welcome to the PyPassword Generator!")

# Prompt the user to input the number of letters, symbols, and numbers for the password
nr_letters = (input("How many letters would you like in your password?\n"))
nr_symbols = (input(f"How many symbols would you like?\n"))
nr_numbers = (input(f"How many numbers would you like?\n"))

# Check if the inputs are valid numbers
if not nr_letters.isdigit() or not nr_symbols.isdigit() or not nr_numbers.isdigit():
    # Print error message for invalid inputs
    print("Invalid value, enter a number instead.")
else:
    password = []  # Initialize an empty list to store password characters

    # Generate random letters and add them to the password list
    for i in range(0, int(nr_letters)):
        # Generate a random index for the letters list
        random_letter = random.randint(0, 51)
        # Add the random letter to the password
        password.append(letters[random_letter])

    # Generate random numbers and add them to the password list
    for i in range(0, int(nr_numbers)):
        # Generate a random index for the numbers list
        random_number = random.randint(0, 9)
        # Add the random number to the password
        password.append(numbers[random_number])

    # Generate random symbols and add them to the password list
    for i in range(0, int(nr_symbols)):
        # Generate a random index for the symbols list
        random_symbol = random.randint(0, 8)
        # Add the random symbol to the password
        password.append(symbols[random_symbol])

    # Shuffle the password list to randomize the order of characters
    random.shuffle(password)

    # Print the generated password
    print(f"Here is your password: {''.join(password)}")

    # Evaluate and display the strength of the password based on its length
    if len(password) <= 6:
        print("Your password is weak, try to include at least 8 characters for a stronger password.")
    elif len(password) == 7:
        print("Your password is medium, try to include at least 8 characters for a stronger password.")
    else:
        print("Your password is strong.")
