amount = int(input("Purchase amount: "))

if amount > 500:
    discount = amount * 10 / 100
    print(f"Getting discount", discount)
else:
    print("No discount sorry!!!")

