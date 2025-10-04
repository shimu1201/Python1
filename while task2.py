status = True 
sum = 0
while status:
    num = int(input("Enter a number :"))
    sum += num

    choice = input("Do you want to add more numbers? ")
    if choice == 'n' or choice == 'no' :
        status = False
print("Total = ", sum)