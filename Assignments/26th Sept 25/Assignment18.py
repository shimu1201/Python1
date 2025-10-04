rates = {"sedan" : 1000, "suv": 1500, "hatchback": 800}

car_type = input("Enter the car type :")
days = int(input("Enter number of days : "))

if car_type in rates:
    total = rates[car_type] * days
    if days > 5:
        discount = total * 0.10
        total -= discount
        print(f"Total rent for {days} days is : {total}")   
else:
    print("Invalid Car Type")