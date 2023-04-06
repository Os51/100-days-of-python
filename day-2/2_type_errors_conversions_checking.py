num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.")

# The above code will result in a TypeError, as concatenation only works on strings
# num_char will return a int value, from the len function
# The print statement therefore is trying to cat "str + int + str" which isn't allowed

print(type(num_char)) # returns class 'int'

# We can use type conversion, or type casting, to change the class to something else

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.") # All the data types here are now string, so the print statement will work

# Another example - type conversion

# define var (a), with an int value of "123"
a = 123
print(type(a))

# define var (a) and convert the value to a string
a = str(123)
print(type(a))

# define var (a) and convert the value to a float
a = float(123)
print(type(a))

# print the calculatation of int (70) added to float (100.5).
# though we have defined the float in quotes, the type is defined, so python doesn't treat it as a string  
print(70 + float("100.5")) # returns float value of 170.5

# remember that these are strings, so we're concatenating, not performing a mathematical equation
print(str(70) + str(100)) # returns a string value of 70100