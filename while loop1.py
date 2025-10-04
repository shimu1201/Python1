"""
initlization
while condition:
    statement
    updation
"""
status = True #initlization
while status:
    num = int(input("Enter a number :"))

    choice = input("Do you want to add more numbers then press 'y' for yes and press 'n' for no : ")
    if choice == 'y' or choice =='yes' :
        status = True
    else:
        status = False
