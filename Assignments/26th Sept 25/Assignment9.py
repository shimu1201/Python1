num1 = int(input("Enter a number 1 : "))
num2 = int(input("Enter a number 2 : "))
num3 = int(input("Enter a number 3 : "))
if num1 > num2:
    if num1 > num3:
        print("Number 1 is Greater")
    else:
        print("Number 3 is Greater")
else:
    if num2 > num3:
        print("Number 2 is Greater")
    else:
        print("Number 3 is Greater")