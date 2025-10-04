"""
Nested if statement : when condition inside the another condition

syntax :

if condition:
    if condition:
        statement
    else:
        statement
else:
    if condition:
        statement
    else:
        statement
"""
marks = int(input("Enter your marks :"))

if marks >= 0 and marks <= 100:
    if marks >= 70:
        print("A Garde")
    elif marks >= 60 and marks <70:
        print("B Garde")
    elif marks >= 50 and marks <60:
        print("C Garde")
    elif marks >= 40 and marks <50:
        print("D Garde")
    else:
        print("Fail")
else:
    print("Invalid Marks !!!")