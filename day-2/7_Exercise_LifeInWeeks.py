# Reference: https://waitbutwhy.com/2014/05/life-weeks.html

age = input("What is your current age? ")

age = int(age)
max_age = 90
days_in_year = 365
weeks_in_year = 52
months_in_year = 12

days = (max_age * days_in_year) - (age * days_in_year)
weeks = (max_age * weeks_in_year) - (age * weeks_in_year)
months = (max_age * months_in_year) - (age * months_in_year)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

