""" 
Body mass index (BMI) is a value derived from the mass (weight) and height of a person. 
The BMI is defined as the body mass divided by the square of the body height. 
It's expressed in units of kg/m2, resulting from mass in kilograms and height in metres.
"""
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round((weight / (height ** 2)))

if bmi <18.5:
    print(f"Your BMI is {bmi}. This falls into the category of underweight.")
elif bmi > 18.5 and bmi <25 :
    print(f"Your BMI is {bmi}. This falls into the category of normal weight.")
elif bmi > 25 and bmi < 30 :
    print(f"Your BMI is {bmi}. This falls into the category of slightly overweight.")
elif bmi > 30 and bmi < 35 :
    print(f"Your BMI is {bmi}. This falls into the category of obese.")
else:
    print(f"Your BMI is {bmi}. This falls into the category of clinically obese.")
