#calculator for tips
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tipBill = int(input("What percentage tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill? "))
totalBill = ((tipBill/100) * bill) + bill
billPayment = round(totalBill / people, 2)

print(f"Each person should pay: {billPayment}")