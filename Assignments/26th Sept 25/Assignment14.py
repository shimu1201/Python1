total = int(input("Enter total shopping amount : "))
if total > 1000:
    discount = total * 15 / 100
    final_amount = total - discount
    print(f"15% Discount - {final_amount}")
elif total > 500:
    discount = total * 10 / 100
    final_amount = total - discount
    print(f"10% Discount - {final_amount}")
else:
    print("No Discount")

