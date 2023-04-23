"""Instructions
Write a program that works out whether a given number is an odd or even number.
Even numbers can be divided by 2 with no remainder.

e.g 86 is even because 86 / 2 = 43

43 does not have any decimal places, therefore the division is clean.

e.g. 59 is odd because 59 / 2 = 36.875

36.875 is not a whole number, it has decimal places... therefore there is a remainder of 0.875 which means the division is not clean

The modulo is written as a percetange (%) sign in Python, providing the remainder after division

e.g.

6 / 2 = 3 with no remainder
therefore 6 % 2 = 0

14 / 4 = 3 * 4 + 2, remainder is 2
therefore 14 % 4 = 2
"""

number_to_check = int(input("Which number do you want to check? "))

if number_to_check % 2 != 0:
    print("This is an odd number.")
else:
    print("This is an even number.")