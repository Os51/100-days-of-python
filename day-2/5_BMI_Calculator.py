""" 
Body mass index (BMI) is a value derived from the mass (weight) and height of a person. 
The BMI is defined as the body mass divided by the square of the body height. 
It's expressed in units of kg/m2, resulting from mass in kilograms and height in metres.
"""
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight = int(weight)
height = float(height)

bmi = int((weight / (height ** 2)))
print(bmi)