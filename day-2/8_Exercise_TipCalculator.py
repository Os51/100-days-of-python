# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12

bill_amount = float(input("What was the total bill? $"))
amount_to_tip = int(input("What percentage would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill with? "))


tip_amount_percentage = amount_to_tip / 100
tip = bill_amount * tip_amount_percentage

bill_plus_tip = bill_amount + tip
total_bill = bill_plus_tip / no_of_people 


print("Each person should pay: ${}".format((round(total_bill, 2))))