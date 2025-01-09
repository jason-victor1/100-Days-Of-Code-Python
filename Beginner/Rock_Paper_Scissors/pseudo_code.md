# Pseudo code for Rock-Paper-Scissors game

START

# Define representations of Rock, Paper, and Scissors (ASCII art)
DEFINE rock, paper, scissors

# Prompt user for input choice (0, 1, or 2)
DISPLAY "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"
USER_INPUT choice

# Generate random choice for computer (0, 1, or 2)
SET computers_choice = RANDOM_NUMBER(0, 2)

# Validate user input
IF choice is NOT a number
    DISPLAY "Invalid input. Please choose a number between 0-2."
ELSE
    CONVERT choice to integer
    IF choice is OUTSIDE range 0-2
        DISPLAY "Invalid number. Please choose a number between 0-2."
    ELSE
        # Display user's choice with corresponding ASCII art
        IF choice == 0
            DISPLAY "You chose: Rock" + rock
        ELSE IF choice == 1
            DISPLAY "You chose: Paper" + paper
        ELSE IF choice == 2
            DISPLAY "You chose: Scissors" + scissors

        # Display computer's choice with corresponding ASCII art
        IF computers_choice == 0
            DISPLAY "The computer chose: Rock" + rock
        ELSE IF computers_choice == 1
            DISPLAY "The computer chose: Paper" + paper
        ELSE IF computers_choice == 2
            DISPLAY "The computer chose: Scissors" + scissors

        # Determine winner
        IF computers_choice == 0
            IF choice == 2
                DISPLAY "You lose, Rock wins against scissors."
            ELSE IF choice == 0
                DISPLAY "It's a draw!"
            ELSE
                DISPLAY "You win!"

        ELSE IF computers_choice == 1
            IF choice == 0
                DISPLAY "You lose, Paper wins against rock."
            ELSE IF choice == 1
                DISPLAY "It's a draw!"
            ELSE
                DISPLAY "You win!"

        ELSE IF computers_choice == 2
            IF choice == 1
                DISPLAY "You lose, Scissors win against paper."
            ELSE IF choice == 2
                DISPLAY "It's a draw!"
            ELSE
                DISPLAY "You win!"

END
