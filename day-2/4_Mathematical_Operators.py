print(3 + 5) # Addition
print(7 - 4) # Subtraction
print(3 * 2) # Multiplication
print(6 / 3) # Division - value returned is type "Float" and not "int".
print(type(6 / 3)) # Returns class 'float'
print(2 ** 3) # Exponent - two to the power of 3, or 2 x 2 x 2 

# With more than one operator on the same line, the calculation occurs in a specific order

"""
The order of calculation is PEMDAS:
Parentheses - ()
Exponents - **
Multiplication - *
Division - /
Addition - +
Subtraction - -

This is a little deceiving, because certain operators are not considered "more important".
In reality, the order is treated as:
() - Parenthesis
** - Exponents

For the operators on the same line, the calculation most to the left is evaluated first
* / - Multiplication and Division are equal in priority. LR applies.
+ - - Addition and Subtraction are equal in priority. LR applies.
""" 

print(3 * 3 + 3 / 3 - 3)
""" 
Step into this code, this is how the calculation happens
3 * 3 + 3 / 3 - 3
9 + 3 / 3 - 3
9 + 1.0 - 3
10.0 - 3
Answer: 7.0
"""

# If we want to change the answer to 3
print(3 * (3 + 3) / 3 - 3)

""" 
The evaluation changes:
3 * (3 + 3) / 3 - 3
3 * 6 / 3 - 3
18 / 3 - 3
6.0 - 3
Answer: 3.0
"""