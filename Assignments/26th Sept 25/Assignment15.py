unit = int(input("Unit consumed - "))
if unit <= 100:
    bill_amount = 5 * unit
    print(f"Your bill amount is {bill_amount}.")
elif unit > 101 and unit < 200:
    bill_amount = 7 * unit
    print(f"Your bill amount is {bill_amount}.")
elif unit > 201 and unit < 500:
    bill_amount = 10 * unit
    print(f"Your bill amount is {bill_amount}.")
else:
    bill_amount = 15 * unit
    print(f"Your bill amount is {bill_amount}.")
