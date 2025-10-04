marks = int(input("Enter your marks :"))

if marks >= 0 and marks <= 100:
    if marks >= 90:
        print("A Garde")
    elif marks >= 75 and marks <90:
        print("B Garde")
    elif marks >= 50 and marks <75:
        print("C Garde")
    else:
        print("Fail")
else:
    print("Invalid Marks !!!")