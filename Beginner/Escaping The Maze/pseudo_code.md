1. **START**

2. **DEFINE** the maze as a 2D grid:
   - Represent the maze where:
     - `1` = Wall
     - `0` = Open path
     - `"G"` = Goal

3. **INITIALIZE** the robot's position and direction:
   - `position = [starting_row, starting_column]` (e.g., `[1, 1]`)
   - `direction = 1` (0 = Up, 1 = Right, 2 = Down, 3 = Left)

4. **DEFINE** helper functions:
   a. **`is_goal(position)`**:
      - Return `True` if the value at `position` in the maze is `"G"`.
   b. **`is_clear(position)`**:
      - Return `True` if the value at `position` in the maze is `0` or `"G"`.
   c. **`move_forward()`**:
      - **CALCULATE** the robot's next position based on its `direction`:
        - If `direction == 0` (Up), move to `row - 1`.
        - If `direction == 1` (Right), move to `column + 1`.
        - If `direction == 2` (Down), move to `row + 1`.
        - If `direction == 3` (Left), move to `column - 1`.
   d. **`turn_left()`**:
      - Update `direction = (direction - 1) % 4`.
   e. **`turn_right()`**:
      - Update `direction = (direction + 1) % 4`.

5. **PRINT** "Starting maze navigation..."

6. **LOOP** while the robot has not reached the goal (`is_goal(position) == False`):
   a. **CALCULATE** the position directly in front of the robot using `move_forward()`.
   b. **TURN RIGHT** and **CALCULATE** the position to the robot’s right using `move_forward()`.
   c. **TURN LEFT** to restore the robot’s original direction.

7. **DECISION-MAKING**:
   a. IF the `right` position is clear (`is_clear(right) == True`):
      - **TURN RIGHT**
      - **MOVE FORWARD** to the `right` position.
   b. ELSE IF the `front` position is clear (`is_clear(front) == True`):
      - **MOVE FORWARD** to the `front` position.
   c. ELSE:
      - **TURN LEFT** to navigate around the obstacle.

8. **END LOOP** when the robot reaches the goal.

9. **PRINT** "Goal reached at position: [row, column]".

10. **END** 