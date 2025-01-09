1. START

2. PRINT "Welcome To The Tip Calculator!"

3. PROMPT the user to input the total bill amount
   a. STORE the input as a floating-point number in the variable `bill`

4. PROMPT the user to input the desired tip percentage
   a. STORE the input as an integer in the variable `tip`

5. PROMPT the user to input the number of people to split the bill
   a. STORE the input as an integer in the variable `split`

6. CALCULATE the total amount each person should pay:
   a. Multiply `bill` by `tip / 100` to get the tip amount
   b. ADD the tip amount to `bill` to get the total bill with tip
   c. DIVIDE the total bill with tip by `split` to get the amount per person
   d. FORMAT the result to 2 decimal places
   e. STORE the formatted result in the variable `total`

7. PRINT "Each person should pay: $" followed by the value of `total`

8. END
