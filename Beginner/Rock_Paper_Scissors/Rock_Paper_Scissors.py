import random  # Importing the random module to generate random choices for the computer

# ASCII art for Rock, Paper, and Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Prompt the user to make a choice: 0 for Rock, 1 for Paper, or 2 for Scissors
choice = (input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n0/1/2:"))

# Generate a random choice for the computer (0 for Rock, 1 for Paper, 2 for Scissors)
computers_choice = random.randint(0, 2)

# Check if the user's input is valid
if not choice.isdigit():
    # If the input is not a digit, print an error message
    print("You've entered an invalid value, try again and choose a number between 0-2.")
else:
    choice = int(choice)  # Convert the input to an integer for comparison
    if choice > 2:
        # If the user's choice is out of range, print an error message
        print(
            "You've entered an invalid number, try again and choose a number between 0-2.")
    elif choice == 0 or choice == 1 or choice == 2:
        # If the user's choice is valid, display their selection with the corresponding ASCII art
        if choice == 0:
            print(f"You chose: Rock {rock}")
        elif choice == 1:
            print(f"You chose: Paper {paper}")
        elif choice == 2:
            print(f"You chose: Scissors {scissors}")

        # Display the computer's random choice with the corresponding ASCII art
        if computers_choice == 0:
            print(f"The computer chose: Rock {rock}")
            # Determine the result based on the user's choice
            if choice == 2:
                print("You lose, Rock wins against scissors.")
            elif choice == 0:
                print("It's a draw!")
            else:
                print("You win!")

        elif computers_choice == 1:
            print(f"The computer chose: Paper {paper}")
            # Determine the result based on the user's choice
            if choice == 0:
                print("You lose, Paper wins against rock.")
            elif choice == 1:
                print("It's a draw!")
            else:
                print("You win!")

        elif computers_choice == 2:
            print(f"The computer chose: Scissors {scissors}")
            # Determine the result based on the user's choice
            if choice == 1:
                print("You lose, Scissors win against paper.")
            elif choice == 2:
                print("It's a draw!")
            else:
                print("You win!")
