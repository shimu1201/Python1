temperature = int(input("Enter temperature in Celsius: "))
if temperature < 0:
    print("Freezing")
elif temperature >=0 and temperature < 10:
    print("Cold")
elif temperature >=10 and temperature < 25:
    print("Pleasant")
else:
    print("Hot")