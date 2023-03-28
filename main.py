#If the bill was ₹150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = ₹33.60

print("Welcome to Tip calculator")
print("-------------------------")
print("-------------------------\n")

bill = float(input("Kitna Paisa Udhaye Khane me: ₹"))
tip_percent = float(input("Kitna percent tip doge: "))
no_of_peoples = int(input("Kitne aadmi ho: "))

tip_amount = bill * (tip_percent/100)
total_bill = bill + tip_amount
bill_per_person = round(total_bill/no_of_peoples, 2)

print(f"\nHar ek aadmi ya aurat ko ₹{bill_per_person} dena hai.")
