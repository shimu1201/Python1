age = int(input("Enter your Age : "))
if age < 5:
    print("Free Ticket")
elif age >= 5 and age < 18:
    print("Child Ticket")
elif age >=18 and age < 60:
    print("Adult Ticket")
else:
    print("Senior citizen ticket")