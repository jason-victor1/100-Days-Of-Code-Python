1. START
2. DISPLAY ASCII art of Treasure Island and an introductory message.
3. PRINT "Welcome to Treasure Island."
4. PRINT "Your mission is to find the treasure."

5. PROMPT the user to choose between "Left" or "Right."
   a. CONVERT the input to lowercase and STORE it in variable `first`.

6. IF `first` is "right":
   a. DISPLAY ASCII art of Sonic.
   b. PRINT "Sonic got the treasure before you, try again."

7. ELSE IF `first` is "left":
   a. DISPLAY ASCII art for level-up success.
   b. PRINT "Nice, you made it to the next level!"
   c. PROMPT the user to choose between "Swim" or "Wait."
      i. CONVERT the input to lowercase and STORE it in variable `second`.

8. IF `second` is "swim":
   a. DISPLAY ASCII art of a shark.
   b. PRINT "Unfortunately, you were eaten by a Great White Shark, try again."

9. ELSE IF `second` is "wait":
   a. PRINT "Nice, you made it to the next level, you're pretty good at this!"
   b. DISPLAY ASCII art for Treasure Island level.
   c. PROMPT the user to choose between "Dig" or "Cave."
      i. CONVERT the input to lowercase and STORE it in variable `third`.

10. IF `third` is "dig":
    a. PRINT "You've found the treasure, you win!"

11. ELSE IF `third` is "cave":
    a. DISPLAY ASCII art of a bear.
    b. PRINT "You were eaten by a bear, game over."

12. END
