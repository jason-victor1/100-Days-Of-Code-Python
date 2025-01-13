# Define the maze as a 2D grid
# 1 = Wall, 0 = Open path, "S" = Starting position, "G" = Goal
maze = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, "G", 1],
    [1, 1, 1, 1, 1],
]

# Initial position of the robot in the maze
position = [1, 1]  # Starting position (row, col) corresponding to "S"
direction = 1      # Initial direction: 0 = Up, 1 = Right, 2 = Down, 3 = Left

# Helper functions for navigation


def is_goal(pos):
    """Check if the robot's current position is the goal ('G')."""
    return maze[pos[0]][pos[1]] == "G"


def is_clear(pos):
    """Check if a given position is clear (not a wall)."""
    return maze[pos[0]][pos[1]] in [0, "G"]


def move_forward():
    """Calculate the next position based on the robot's current direction."""
    if direction == 0:  # Facing Up
        return [position[0] - 1, position[1]]
    elif direction == 1:  # Facing Right
        return [position[0], position[1] + 1]
    elif direction == 2:  # Facing Down
        return [position[0] + 1, position[1]]
    elif direction == 3:  # Facing Left
        return [position[0], position[1] - 1]


def turn_left():
    """Turn the robot 90 degrees counterclockwise."""
    global direction
    direction = (direction - 1) % 4  # Update direction cyclically (0-3)


def turn_right():
    """Turn the robot 90 degrees clockwise."""
    global direction
    direction = (direction + 1) % 4  # Update direction cyclically (0-3)


# Simulate the robot navigating the maze
while not is_goal(position):  # Continue until the robot reaches the goal
    # Calculate the positions in front and to the right of the robot
    front = move_forward()  # The position directly ahead
    turn_right()            # Temporarily turn right to calculate right position
    right = move_forward()  # The position to the right of the robot
    turn_left()             # Turn back to restore original direction

    # Decision-making based on the right-hand rule
    if is_clear(right):  # If the right side is clear, turn right and move
        turn_right()
        position = move_forward()
    elif is_clear(front):  # If the front is clear, move forward
        position = move_forward()
    else:  # If neither is clear, turn left to navigate around the obstacle
        turn_left()

# Print the result when the goal is reached
print("Goal reached at position:", position)
