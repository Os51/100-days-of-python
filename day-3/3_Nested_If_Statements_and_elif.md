# Nested If/Else
- In the previous, we checked for the height of a person to determine whether they could ride the rollercoaster
- What if we needed to add another condition to this to determine how much someone would need to pay for admission, and if we had different payment amounts depending on a factor of that person, such as age?
- We can represent these conditions with a nested if/else statement

- In a normal if/else statement, we evaluate as the following:
```python
if condition:
    do this
else:
    do this instead
```

- In a nested if statement, once the first condition is passed, we can check for another condition, and then have an if/else inside of that "if" condition:
```python
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
```

- Breaking this down:
```python
if condition:
    if second condition:
        do this     # For this to trigger, both if conditions MUST be true
    else:
        do this     # This will trigger if the first if condition is True, but the second if condition is False
else:
    do this         # This will trigger if the first if condition is false. The second if condition is not evaluated.
```

- Going back to the control flow exercise:
```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you must be taller to ride the rollercoaster.")
```

- We can add another statement to check for age:
```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age <=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you must be taller to ride the rollercoaster.")
```
- We can even account for further pricing tiers if we needed to. Let's say this changes to:
    - Less than 12: $5
    - 12 - 18: $7
    - Over 18: $12
- We can represent these changes to the tiers with an **elif** statement.

# Elif Statements
```python
if condition1:
    do A
elif condition2:
    do B
else:
    do this
```
- With elif statements, we can add another statement to evaluate against if the condition of the first if statement is false. 
    - We're adding a level, or a different condition, to check against. It's different to a nested if statement as those are only evaluated if the first condition is **True**.

- Back to the example, using the changes we now need to make on the pricing tiers:

```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:                                # The first if condition is True if the age is less than 12
        print("Please pay $5.")
    elif age <=18:                              # The elif is True if the age is not less than 12, but is less than or equal to 18. It will only be evaluated if the first "if age < 12" is evaluated as False.
        print("Please pay $7.")
    else:                                       # The else statement runs if the first if and elif statements are False, therefore if the age is not less than 12, and is not less than or equal to 18.
        print("Please pay $12.")
else:
    print("Sorry, you must be taller to ride the rollercoaster.")
```

- We can add as many elif statements as we like between if and else to check against as many conditions as we have.