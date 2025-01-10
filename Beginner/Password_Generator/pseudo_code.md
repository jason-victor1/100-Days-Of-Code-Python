START

PRINT "Welcome to the PyPassword Generator!"

PROMPT the user to input the number of letters for the password.
a. STORE the input as a string in the variable nr_letters.

PROMPT the user to input the number of symbols for the password.
a. STORE the input as a string in the variable nr_symbols.

PROMPT the user to input the number of numbers for the password.
a. STORE the input as a string in the variable nr_numbers.

IF any of nr_letters, nr_symbols, or nr_numbers is not a valid number:
a. PRINT "Invalid value, enter a number instead."
b. END

CONVERT nr_letters, nr_symbols, and nr_numbers to integers.

INITIALIZE an empty list password.

FOR each value from 0 to nr_letters - 1:
a. GENERATE a random index from the range of the letters list.
b. APPEND the corresponding letter to the password list.

FOR each value from 0 to nr_numbers - 1:
a. GENERATE a random index from the range of the numbers list.
b. APPEND the corresponding number to the password list.

FOR each value from 0 to nr_symbols - 1:
a. GENERATE a random index from the range of the symbols list.
b. APPEND the corresponding symbol to the password list.

SHUFFLE the password list randomly.

JOIN the elements of password into a single string and STORE it in the variable password_string.

PRINT "Here is your password: " followed by password_string.

CHECK the length of the password list:
a. IF length ≤ 6:
i. PRINT "Your password is weak, try to include at least 8 characters for a stronger password."
b. ELSE IF length == 7:
i. PRINT "Your password is medium, try to include at least 8 characters for a stronger password."
c. ELSE:
i. PRINT "Your password is strong."

END