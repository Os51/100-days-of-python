# Number manipulation

# Division normally returns values as floating points, even if it is "clean division"
print(8 / 3) # Returns 2.666666666
print(int(8 / 3)) # Returns int value of 2, due to type conversion

# Rounding returns type 'int'
print(round(8 / 3)) # Returns 3
print(type(round(8 / 3))) # Returns type "int"

# You can specify how many decimal places to, denoted by the value behind the comma
print(round(8 / 3, 2)) # Rounding to 2 decimal places, returning float '2.67'

print(8 // 3) # Floor Division, returns type int, but does not round the reslt
print(type(8 // 3))

print("-----------------------------------")

# We can use number manipulation to amend the values contained in variables, without having to write the whole calculation
result = 4 / 2 # We set the variable to a value of "2.0", which is the result of the operation 4 / 2
result /= 2 # We then say to divide the value of result by 2 again, 2 / 2 = 1.0
print(result)


score = 0
print(score)

score += 1 # "Increment" (add) 1 to variable "Score"
print("Your score is " + str(score))



score = 0
height = 1.8
isWinning = False

# printing using f-strings
print(f"Your score is: {score}. Your height is {height}... but are you winning son? \n{isWinning}")